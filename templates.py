STRICT_JSON_TEMPLATE = """
You are a structured output engine. You MUST respond ONLY with valid JSON.
No explanation. No markdown. No extra text. Just raw JSON.

Always strictly JSON output as follows always!
Task: {task}
User Input: {user_input}

Respond ONLY in this exact JSON format:
{{
  "status": "success" | "error",
  "result": "<your answer here>",
  "confidence": <float 0.0 to 1.0>,
  "reasoning": "<one sentence why>"
}}
"""

def build_prompt(task: str, user_input: str) -> str:
    return STRICT_JSON_TEMPLATE.format(task=task, user_input=user_input)
