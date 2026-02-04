from flask import Flask, render_template, request
from log_analyzer import generate_incident_summary
from log_analyzer import (
    compress_logs,
    detect_anomaly,
    generate_incident_summary,
    build_attack_timeline
)



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    raw_logs = request.form["logs"]

    # 1️⃣ Compression (for cost + display)
    compression_result = compress_logs(raw_logs)

    # 2️⃣ Detection MUST use RAW logs
    anomaly = detect_anomaly(raw_logs)

    # 3️⃣ Explanation from anomaly result
    explanation = generate_incident_summary(anomaly)

    timeline = build_attack_timeline(raw_logs)
    incident_summary = generate_incident_summary(anomaly)



    return render_template(
        "result.html",
        compressed=compression_result["compressed"],
        original_tokens=compression_result["original_tokens"],
        compressed_tokens=compression_result["compressed_tokens"],
        latency=compression_result["latency"],
        anomaly=anomaly,
        explanation=explanation,
        timeline=timeline,
        incident_summary=incident_summary
    )


if __name__ == "__main__":
    app.run(debug=True)
