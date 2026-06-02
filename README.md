# Constraint-Based LLM Output Controller

A minimal Python tool that takes user input, applies a strict prompt template, and forces structured JSON output from an LLM.

## What it does

- Takes user input
- Applies a strict prompt template
- Forces valid JSON output every time

## Project Structure

```
llm-output-controller/
├── controller.py     # Core logic — calls the API, parses JSON
├── templates.py      # Strict prompt template builder
├── main.py           # Entry point — CLI interface
├── requirements.txt
└── README.md
```

## Setup

```bash
# 1. Clone / create the repo
git init
git add .
git commit -m "initial commit"

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your API key
export ANTHROPIC_API_KEY=your_key_here  # Windows: set ANTHROPIC_API_KEY=your_key_here
```

## Run

```bash
python main.py
```

## Example Output

```json
{
  "status": "success",
  "result": "positive",
  "confidence": 0.97,
  "reasoning": "The text expresses clear enthusiasm and satisfaction."
}
```

## How it works

1. `templates.py` — defines a strict prompt that instructs the model to return ONLY JSON
2. `controller.py` — sends the prompt to Claude, parses the response, handles errors
3. `main.py` — simple CLI that lets the user pick a task and enter text
