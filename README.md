# 🛡️ Security Monitoring Agent (GenAI-Assisted)

A **security monitoring agent** that analyzes system authentication logs, detects suspicious behavior, and presents explainable security insights through a modern web dashboard.

This project was built for a **GenAI for GenZ Hackathon** and demonstrates **responsible use of GenAI** combined with **deterministic security detection**.

---

## 🚀 Features

- 🔍 **Authentication Log Analysis**
  - SSH login failures
  - PAM authentication failures
  - Privileged account (`root`) targeting
  - Invalid user probing
  - Multi-IP attack patterns

- 🧠 **GenAI-Powered Log Compression**
  - Uses the **ScaleDown API**
  - Preserves security-critical context
  - Reduces token usage by **70–80%**

- ⚙️ **Rule-Based Threat Detection**
  - Deterministic and explainable logic
  - Severity scoring (0–100)
  - Risk levels: **LOW / MEDIUM / HIGH**

- 🏷️ **Attack Classification**
  - SSH Brute Force
  - Privileged Account Targeting
  - Credential Stuffing / User Enumeration
  - Distributed Login Attempt

- 🕒 **Attack Timeline**
  - Chronological reconstruction of events
  - Highlights failed, successful, and informational actions

- 🎨 **SOC-Style Dashboard**
  - Dark mode with persistence
  - Subtle animations & hover effects
  - Risk-aware visual indicators

---

## 🧩 Architecture

Raw Logs
↓
AI-based Log Compression (ScaleDown API)
↓
Rule-Based Detection Engine
↓
Severity & Risk Scoring
↓
Attack Classification
↓
Timeline Reconstruction
↓
Web Dashboard (Flask + Bootstrap)


---

## 🤖 How AI Is Used

AI is **intentionally used only where it adds value**.

### ✅ AI is used for:
- Semantic compression of logs
- Reducing token count and processing cost
- Preserving important security signals

### ❌ AI is NOT used for:
- Threat detection
- Risk classification
- Explanation generation

Detection and explanations are **rule-based** to ensure accuracy, explainability, and avoid hallucinations.

---

## 🔐 Detection Philosophy

This project follows **real-world security operations (SOC) practices**.

| Scenario | Risk Level |
|--------|-----------|
| Distributed SSH brute force | HIGH |
| Root account brute force | HIGH |
| Local privilege escalation attempts | MEDIUM |
| Normal admin activity | LOW |

Not all suspicious activity is immediately classified as HIGH — **context matters**.

---

## 📂 Project Structure
```
security-agent/
│
├── app.py # Flask application
├── log_analyzer.py # Detection & analysis engine
├── scaledown_client.py # ScaleDown API integration
├── templates/
│ ├── index.html # Log input page
│ └── result.html # Analysis dashboard
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/security-monitoring-agent.git
cd security-monitoring-agent
```
## 🛠️ Setup & Installation

### 2️⃣ Create a virtual environment
```bash
python -m venv .venv
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Set the ScaleDown API key
- Set an environment variable:

**Windows (PowerShell)**
```powershell
setx SCALEDOWN_API_KEY "your_api_key_here"
```
**Linux / macOS**
```bash
export SCALEDOWN_API_KEY=your_api_key_here
```

### ▶️ Running the Application
```bash
python app.py
```

**Open your browser at:**
```cpp
http://127.0.0.1:5000
```

## 🧪 Testing the System
You can test the system using:

- Public SSH honeypot logs

- Sample `auth.log` files

- Generated realistic authentication logs

**Example log patterns**
```text
Failed password for root from 192.168.1.10
pam_unix(sshd:auth): authentication failure
Too many authentication failures for root
```
Paste logs directly into the input box.


## 📊 Output Explanation
- Risk Level → Overall threat classification

- Severity Score → Impact score (0–100)

- Detection Confidence → Signal-based confidence

- Attack Classification → Type of detected behavior

- Compressed Logs → AI-optimized representation

- Attack Timeline → Chronological event view

- Suggested Action → Mitigation guidance

## 🚧 Limitations & Future Work
**Current limitations**
- Single-host log analysis

- No network telemetry (PCAP, NetFlow)

- No cross-host correlation

**Future improvements**
- MITRE ATT&CK mapping

- Multi-host correlation

- Streaming log ingestion

- Alert export (JSON / SIEM)

- Behavioral baselining

## 📜 License
This project is licensed under the MIT License.

## 🙌 Acknowledgements
- ScaleDown AI for log compression

- Open-source SSH honeypot datasets

- Security community best practices

## 📬 Contact
**Built as part of a GenAI for GenZ Hackathon.**

Feel free to explore, fork, or contribute.


