import re
import time


# =========================
# LOG COMPRESSION HANDLER
# =========================

def compress_logs(raw_logs):
    start_time = time.time()

    try:
        from scaledown_client import compress_with_scaledown

        context = (
            "You are compressing system authentication logs. "
            "Preserve IP addresses, authentication outcomes, and event order."
        )

        result = compress_with_scaledown(context, raw_logs)

        compressed = result.get("compressed_prompt", raw_logs[:1000])
        original_tokens = result.get(
            "original_prompt_tokens", len(raw_logs.split())
        )
        compressed_tokens = result.get(
            "compressed_prompt_tokens", len(compressed.split())
        )

    except Exception:
        compressed = raw_logs[:1000]
        original_tokens = len(raw_logs.split())
        compressed_tokens = len(compressed.split())

    latency = int((time.time() - start_time) * 1000)

    return {
        "compressed": compressed,
        "original_tokens": original_tokens,
        "compressed_tokens": compressed_tokens,
        "latency": latency,
    }


# =========================
# ANOMALY DETECTION ENGINE
# =========================

def detect_anomaly(raw_logs):
    logs = raw_logs.lower()

    # Always initialize first
    severity_score = 0
    issues = []
    attack_labels = []

    # Classic SSH patterns
    failed_password_count = logs.count("failed password")
    invalid_user_count = logs.count("invalid user")

    # PAM / SSH patterns
    auth_failure_count = logs.count("authentication failure")
    too_many_failures_count = logs.count("too many authentication failures")

    # Extract IPs
    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', logs)
    unique_ips = set(ips)

    # ---- Detection Rules ----

    # Failed password brute force
    if failed_password_count >= 5:
        issues.append(
            f"Multiple failed password attempts detected ({failed_password_count})"
        )
        attack_labels.append("SSH Brute Force")
        severity_score += min(failed_password_count * 3, 30)

    # PAM-based brute force
    if auth_failure_count >= 5 or too_many_failures_count >= 3:
        issues.append(
            f"Repeated SSH authentication failures detected "
            f"(auth failures: {auth_failure_count})"
        )
        attack_labels.append("SSH Brute Force")
        severity_score += 35

    # Privileged account escalation
    if auth_failure_count >= 10 and "user=root" in logs:
        issues.append("Critical account (root) targeted repeatedly")
        attack_labels.append("Privileged Account Targeting")
        severity_score += 30

    # Invalid username probing
    if invalid_user_count >= 3:
        issues.append("Repeated attempts using invalid usernames")
        attack_labels.append("Credential Stuffing / User Enumeration")
        severity_score += 20

    # IP diversity
    if len(unique_ips) >= 2:
        issues.append(
            f"Suspicious activity from multiple IP addresses ({len(unique_ips)})"
        )
        attack_labels.append("Distributed Login Attempt")
        severity_score += min(len(unique_ips) * 5, 20)

    # Deduplicate labels
    attack_labels = list(set(attack_labels))

    # ---- Risk Classification ----
    if severity_score >= 70:
        risk = "HIGH"
    elif severity_score >= 40:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    confidence = min(60 + severity_score // 2, 95)

    if issues:
        return {
            "risk": risk,
            "severity": severity_score,
            "confidence": confidence,
            "issues": issues,
            "attack_labels": attack_labels,
            "action": (
                "Block offending IPs, restrict root SSH access, "
                "and enforce multi-factor authentication"
            ),
        }

    return {
        "risk": "LOW",
        "severity": 10,
        "confidence": 50,
        "issues": ["No strong indicators of malicious activity"],
        "attack_labels": [],
        "action": "Continue monitoring",
    }


# =========================
# INCIDENT SUMMARY
# =========================

def generate_incident_summary(anomaly):
    if anomaly["risk"] == "HIGH":
        return (
            "A high-risk security incident was detected involving repeated "
            "authentication failures and suspicious access patterns. "
            "The behavior is consistent with a brute-force or credential "
            "stuffing attack. Immediate mitigation actions are recommended."
        )

    if anomaly["risk"] == "MEDIUM":
        return (
            "Suspicious authentication activity was observed that may "
            "indicate early-stage attack behavior. Increased monitoring "
            "is advised."
        )

    return (
        "No significant security threats were detected during log analysis. "
        "The system appears to be operating within normal parameters."
    )


# =========================
# ATTACK TIMELINE
# =========================

def build_attack_timeline(raw_logs):
    timeline = []

    for line in raw_logs.splitlines():
        lower = line.lower()

        if "failed password" in lower or "authentication failure" in lower:
            timeline.append(("FAILED", line))
        elif "invalid user" in lower:
            timeline.append(("FAILED", line))
        elif "accepted password" in lower:
            timeline.append(("SUCCESS", line))
        elif "disconnecting" in lower:
            timeline.append(("INFO", line))

    return timeline[:15]
