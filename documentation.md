# Security Monitoring Agent – Project Documentation

---

## 1. Introduction

The **Security Monitoring Agent** is a log-based security analysis system designed to detect suspicious authentication activity in Linux systems.

The project combines:
- **Rule-based security detection** for accuracy and explainability
- **GenAI-assisted log compression** for efficiency and scalability
- **A modern web interface** for usability and presentation

The system is intended for:
- Security monitoring demonstrations
- Educational use
- Hackathon and prototype environments

---

## 2. Problem Statement

Security teams frequently analyze large volumes of system logs to detect attacks such as:
- SSH brute-force attempts
- Credential stuffing
- Privileged account abuse
- Unauthorized access attempts

### Challenges
- Logs are verbose and unstructured
- Manual inspection is slow and error-prone
- Using AI everywhere is expensive and unreliable
- Black-box AI decisions reduce trust in alerts

---

## 3. Solution Overview

This project addresses the problem by:

1. Compressing logs using **GenAI** to reduce size while preserving meaning  
2. Applying **deterministic detection rules** to identify suspicious patterns  
3. Scoring and classifying risk based on observed behavior  
4. Presenting results visually in a **SOC-style dashboard**

This hybrid approach balances **efficiency, explainability, and realism**.

---

## 4. System Architecture

### High-Level Flow

```
User Inputs Logs
↓
ScaleDown API (AI-based compression)
↓
Log Analyzer (Rule-based detection)
↓
Severity & Risk Scoring
↓
Attack Classification
↓
Timeline Reconstruction
↓
Web Dashboard Output
```


---

## 5. Component Breakdown

### 5.1 Flask Application (`app.py`)

**Responsibilities**
- Accept log input from the UI
- Coordinate analysis steps
- Pass results to HTML templates
- Serve the web dashboard

**Key Actions**
- Receives raw logs
- Calls compression and detection functions
- Aggregates results into a single response object

---

### 5.2 Log Analyzer (`log_analyzer.py`)

This module is the **core detection engine**.

**Responsibilities**
- Parse authentication-related log entries
- Count failed and successful login attempts
- Identify privileged account targeting
- Track IP diversity
- Build an attack timeline
- Assign severity and confidence scores

**Detection Logic Examples**
- Multiple failed logins → suspicious behavior
- Root account targeted → higher severity
- Multiple IPs involved → increased confidence
- Local privilege escalation attempts → medium risk
- Distributed SSH brute force → high risk

This module is **fully rule-based**, ensuring:
- Predictable behavior
- No hallucinated explanations
- Easy debugging and tuning

---

### 5.3 ScaleDown API Integration (`scaledown_client.py`)

This module integrates **GenAI** into the system.

**Purpose**
- Compress large log inputs
- Preserve security-relevant information
- Reduce token usage and processing cost

**Why AI is used here**
- Log compression is semantic, not deterministic
- AI excels at summarization and context preservation
- Compression improves scalability without affecting detection accuracy

**What the API does NOT do**
- Detect threats
- Assign risk
- Generate explanations

---

### 5.4 Frontend Templates (`index.html`, `result.html`)

#### `index.html`
- Accepts raw logs from the user
- Provides a clean input interface

#### `result.html`
- Displays analysis results
- Risk level and severity cards
- Token reduction metrics
- Incident summary
- Attack classification
- Attack timeline
- Dark mode with persistence

The UI is designed to resemble a **Security Operations Center (SOC) dashboard**.

---

## 6. AI Usage Explanation

### Where AI is used
- Log compression only

### Why this design was chosen
- Detection requires precision and consistency
- AI hallucinations are unacceptable in security alerts
- Rule-based detection ensures trust
- AI improves efficiency without compromising correctness

This approach mirrors **real-world security engineering practices**.

---

## 7. Risk Scoring Model

The system assigns:
- **Severity Score (0–100)**
- **Risk Level** (LOW / MEDIUM / HIGH)
- **Detection Confidence (%)**

### Factors Considered
- Number of failed authentication attempts
- Targeted accounts (root vs normal user)
- IP address diversity
- Authentication method (SSH, su, PAM)
- Local vs remote activity

### Example Classification

| Scenario | Risk Level |
|--------|-----------|
| Normal admin activity | LOW |
| Local privilege escalation attempts | MEDIUM |
| SSH brute-force attack | HIGH |
| Root credential stuffing | HIGH |

---

## 8. Attack Classification Labels

The system assigns descriptive labels such as:
- SSH Brute Force
- Privileged Account Targeting
- Credential Abuse
- Local Privilege Escalation
- Distributed Authentication Attack

These labels improve **analyst readability** and **incident reporting clarity**.

---

## 9. Attack Timeline Reconstruction

The attack timeline:
- Extracts relevant log entries
- Classifies each event (FAILED / SUCCESS / INFO)
- Displays events chronologically

This helps analysts understand:
- Attack progression
- Escalation attempts
- Final outcomes

---

## 10. Limitations

Current limitations include:
- Single-host log analysis
- No real-time log streaming
- No network packet analysis
- No cross-host correlation
- No persistent alert storage

These are intentional trade-offs for a prototype system.

---

## 11. Future Enhancements

Planned improvements include:
- MITRE ATT&CK technique mapping
- Multi-host correlation
- Streaming log ingestion
- SIEM export (JSON / syslog)
- Behavioral baselining
- Alert prioritization

---

## 12. Security & Ethical Considerations

- All logs used are public or synthetic
- No private or personal data is processed
- No live systems are monitored
- Designed for education and demonstration only

---

## 13. Conclusion

The **Security Monitoring Agent** demonstrates:
- Responsible use of GenAI
- Explainable security detection
- Realistic SOC-style analysis
- Clean separation of AI and detection logic

The project prioritizes **clarity over complexity** and **trust over automation**.

---


