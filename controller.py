import json
import os
import urllib.request
import urllib.error

API_URL = "https://openrouter.ai/api/v1/chat/completionss"
API_KEY = "sk-oaeffefr-v1-ec681wewabqefqfefg53hwe2erhrehrn6eah3er7he4hehe1h6rh27heewfwfhwbifqybfiewbfqefef2b4517e4b9af48edf3fnwbfiwefuqbfkqebfiqbfc814308f021a0250a26eb0bc4851"
MODEL = "openrouter/owl-alpha"


def run(task: str, user_input: str) -> dict:
    from templates import build_prompt
    prompt = build_prompt(task, user_input)

    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 512,
    }).encode("utf-8")

    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
        }
    )

    try:
        with urllib.request.urlopen(req) as res:
            status = res.status
            body = res.read()
            data = json.loads(body)
            raw = data["choices"][0]["message"]["content"].strip()

    except urllib.error.HTTPError as e:
        body = e.read().decode()
        return {
            "status": "error",
            "result": None,
            "confidence": 0.0,
            "reasoning": f"HTTP {e.code}: {body}"
        }
    except Exception as e:
        return {
            "status": "error",
            "result": None,
            "confidence": 0.0,
            "reasoning": f"API call failed: {str(e)}"
        }

    try:
        clean = raw.replace("```json", "").replace("```", "").strip()
        return json.loads(clean)
    except json.JSONDecodeError:
        return {
            "status": "error",
            "result": None,
            "confidence": 0.0,
            "reasoning": f"Model returned non-JSON output: {raw[:100]}"
        }