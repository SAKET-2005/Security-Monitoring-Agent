import requests
import json
import os

SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")
SCALEDOWN_URL = "https://api.scaledown.xyz/compress/raw/"

def compress_with_scaledown(context, prompt):
    headers = {
        "x-api-key": SCALEDOWN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "context": context,
        "prompt": prompt,
        "scaledown": {
            "rate": "auto"
        }
    }

    response = requests.post(
        SCALEDOWN_URL,
        headers=headers,
        data=json.dumps(payload),
        timeout=20
    )

    response.raise_for_status()
    return response.json()
