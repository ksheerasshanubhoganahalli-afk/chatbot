import requests

API_KEY = "sk_30b077fe76db1b4ffa3b6929e9fa2ec2"  # Replace with your actual API key
URL = "https://api.inceptionlabs.ai/v1/chat/completions"

messages = [
    {
        "role": "system",
        "content": (
            "You are a Socratic tutor. "
            "Ask questions instead of giving direct answers. "
            "Keep every reply simple, clear, natural, and human-readable."
        )
    }
]

print("Socratic Tutor Chatbot")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = requests.post(
        URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mercury-2",
            "messages": messages
        }
    )

    if response.status_code == 200:
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        print("Bot:", reply, "\n")
        messages.append({"role": "assistant", "content": reply})
    else:
        print("Error:", response.status_code)
        print(response.text)
        break