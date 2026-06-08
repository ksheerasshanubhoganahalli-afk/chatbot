
## 📄 README.md

```markdown
# 🎓 Socratic Tutor Chatbot

A simple terminal chatbot powered by **Inception LLM API** using the **mercury-2** model.
It acts as a **Socratic Tutor** — guiding users by asking questions instead of giving direct answers.

---

## ✨ Features

- 🎭 Socratic Tutor role
- 💬 Maintains conversation history
- 🖥️ Runs in terminal
- 🔒 Uses environment variables for API key

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- API key from [InceptionLabs](https://platform.inceptionlabs.ai/)

### Installation

1. Clone the repo:

```bash
git clone https://github.com/ksheerasshanubhoganahalli-afk/chatbot.git
cd chatbot
```

2. Install requests:

```bash
pip install requests python-dotenv
```

3. Create `.env` file and add your API key:

```
INCEPTION_API_KEY=your_api_key_here
```

---

## ▶️ Usage

```bash
python chatbot.py
```

### Example

```
Socratic Tutor Chatbot
Type 'exit' to stop.

You: What is gravity?
Bot: Great question! What do you think happens when you drop a ball?

You: It falls down
Bot: Right! Why do you think it falls down instead of going up?

You: exit
Goodbye!
```

---

## 📁 Files

| File | Description |
|------|-------------|
| `chatbot.py` | Main chatbot with Socratic Tutor role |
| `.env` | API key file (not uploaded to GitHub) |

---

## ❓ Troubleshooting

| Error | Solution |
|-------|----------|
| `401 Unauthorized` | Check your API key in `.env` |
| `Connection Error` | Check your internet |
| `ModuleNotFoundError` | Run `pip install requests python-dotenv` |

---

## 📝 License

MIT License

---

## 🙏 Acknowledgments

- [InceptionLabs](https://platform.inceptionlabs.ai/) for the API
```

---

## 📄 chatbot.py

```python
import requests
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("INCEPTION_API_KEY")

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

print("=" * 50)
print("  🎓 Socratic Tutor Chatbot")
print("  Powered by Inception LLM (mercury-2)")
print("=" * 50)
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if not user_input.strip():
        continue

    messages.append({"role": "user", "content": user_input})

    try:
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
            print(f"Bot: {reply}\n")
            messages.append({"role": "assistant", "content": reply})
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            break

    except Exception as e:
        print(f"Error: {e}")
        break
```

---

## 📄 .env

```
INCEPTION_API_KEY=your_api_key_here
```

---

---

## 📋 How to Push to Your Repo

Open terminal and run:

```bash
cd chatbot

git init
git add .
git commit -m "Socratic Tutor Chatbot"
git branch -M main
git remote add origin https://github.com/ksheerasshanubhoganahalli-afk/chatbot.git
git push -u origin main
```

---

## 📋 Final Folder Structure

```
chatbot/
├── chatbot.py       # Main chatbot
├── .env             # API key
└── README.md        # Project description
```

---
