# 📄 GitHub README File

Create a file called `README.md` and paste this:

```markdown
# 🎓 Socratic Tutor Chatbot

A simple terminal-based chatbot powered by **Inception Labs API** that acts as a **Socratic tutor** — it never gives direct answers, instead it guides you by asking questions.

---

## 📸 Demo

```
Socratic Tutor Chatbot
Type 'exit' to stop.

You: What is gravity?
Bot: That is a great question! When you drop a ball, what do you think happens to it?

You: It falls down
Bot: Yes! Now, why do you think it falls down instead of floating up?

You: Because of something pulling it
Bot: Exactly! So what do you think is doing the pulling?
```

---

## 🚀 Features

- 🎭 **Socratic Role** — Guides through questions, never gives direct answers
- 💬 **Chat History** — Remembers previous messages in the conversation
- 🧠 **Powered by Inception Labs** — Uses `mercury-2` model
- 🖥️ **Terminal Based** — Runs in your command prompt / terminal
- 🐍 **Simple Python** — Easy to understand and modify

---

## 📦 Requirements

- Python 3.7+
- `requests` library

---

## ⚡ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/socratic-chatbot.git
cd socratic-chatbot
```

### 2. Install dependencies

```bash
pip install requests
```

### 3. Get your API key

1. Go to [https://platform.inceptionlabs.ai/](https://platform.inceptionlabs.ai/)
2. Create an account or login
3. Go to **API Keys** section
4. Generate a new API key
5. Copy it

### 4. Set your API key

Open `chatbot.py` and replace:

```python
API_KEY = "YOUR_REAL_API_KEY"
```

with your actual API key.

---

## ▶️ Usage

```bash
python chatbot.py
```

Then just type your questions and the bot will guide you!

```text
Socratic Tutor Chatbot
Type 'exit' to stop.

You: What is photosynthesis?
Bot: Good question! What do you think plants use sunlight for?
```

Type `exit` to stop the chatbot.

---

## 📁 Project Structure

```
socratic-chatbot/
│
├── chatbot.py       # Main chatbot code
├── README.md        # This file
└── .gitignore       # Git ignore file
```

---

## 🛠️ How It Works

1. You type a message in the terminal
2. The message is sent to **Inception Labs API**
3. The API processes it using the **Socratic tutor** role
4. The bot replies with a guiding question
5. The conversation continues

---

## 🔧 Customization

### Change the role

Edit the system message in `chatbot.py`:

```python
"content": (
    "You are a Socratic tutor. "
    "Ask questions instead of giving direct answers. "
    "Keep every reply simple, clear, natural, and human-readable."
)
```

### Change the model

Change this line in `chatbot.py`:

```python
"model": "mercury-2"
```

to any other model available on Inception Labs.

---

## ❓ FAQ

### Why am I getting an error?

| Error | Fix |
|-------|-----|
| `401 Unauthorized` | Check your API key |
| `Connection Error` | Check your internet connection |
| `Invalid model` | Check available models on Inception Labs |

### Can I add more roles?

Yes! Just modify the `messages` list in the code.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- [Inception Labs](https://platform.inceptionlabs.ai/) for the API
- Inspired by the Socratic method of teaching

---

## 📬 Contact

If you have questions or suggestions, feel free to open an issue or reach out!

**GitHub**: )
```

---

## Also create a `.gitignore` file

```
__pycache__/
*.pyc
.env
venv/
```

---

## 📋 Quick Setup

```bash
# 1. Create repository on GitHub
# 2. Clone it
git clone https://github.com/YOUR_USERNAME/socratic-chatbot.git
cd socratic-chatbot

# 2. Add your files
# 3. Push to GitHub
git add .
git commit -m "Initial commit"
git push origin main
```

---

**Replace `YOUR_USERNAME` with your actual GitHub username!** 🚀
