# /home/admin/pichat/chat_ai.py

import os
import subprocess
import datetime

# Model options
models = {
    "1": "deepseek-r1:1.5b",
    "2": "deepseek-r1:8b"
}

log_file = "/home/admin/pichat/chat_log.txt"

def choose_model():
    print("\nChoose a model:")
    for key, model in models.items():
        print(f"[{key}] {model}")
    choice = input("Enter number: ").strip()
    model_name = models.get(choice)
    if not model_name:
        print("Invalid choice.")
        return choose_model()
    return model_name

# Initial model selection
model_name = choose_model()

print(f"\n✅ Running model: {model_name}")
print("Type 'exit' to stop, 'change' to switch models.")
print("---- Chat started ----\n")

with open(log_file, "a") as f:
    f.write(f"\n\n==== Chat with {model_name} on {datetime.datetime.now()} ====\n")

# Chat loop
while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        break

    if user_input.lower() == "change":
        model_name = choose_model()
        with open(log_file, "a") as f:
            f.write(f"\n\n==== Switched to {model_name} on {datetime.datetime.now()} ====\n")
        print(f"\n✅ Now using model: {model_name}")
        continue

    with open(log_file, "a") as f:
        f.write(f"\nYou: {user_input}\n")

    result = subprocess.run(
        ["ollama", "run", model_name],
        input=user_input.encode(),
        capture_output=True
    )

    response = result.stdout.decode().strip()
    print(f"AI: {response}")

    with open(log_file, "a") as f:
        f.write(f"AI: {response}\n")
