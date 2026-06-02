from controller import run
import json

TASKS = {
    "1": "Classify the sentiment of the text (positive, negative, or neutral)",
    "2": "Summarize the text in one sentence",
    "3": "Extract the main topic from the text",
}


def main():
    print("\n=== Constraint-Based LLM Output Controller ===\n")
    print("Pick a task:")
    for key, desc in TASKS.items():
        print(f"  {key}. {desc}")

    choice = input("\nEnter task number (1-3): ").strip()
    task = TASKS.get(choice)

    if not task:
        print("Invalid choice. Exiting.")
        return

    user_input = input("Enter your text: ").strip()

    if not user_input:
        print("No input provided. Exiting.")
        return

    print("\nRunning...\n")
    result = run(task=task, user_input=user_input)

    print("=== Output ===")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
