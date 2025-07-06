# 🧠 AI Chatbot Desktop App

This is a smart AI-powered chatbot built with Python and Tkinter that provides various utilities like weather updates, jokes, math solving, Wikipedia summaries, currency/unit conversion, reminders, and more. It also supports voice output (TTS) and light/dark themes.

---

## ✨ Features

- 🎙️ **Text-to-Speech (TTS)** (Enable/Disable voice, switch between Male/Female)
- 🌙 **Theme Toggle** (Dark/Light mode)
- 📅 **Reminders & Alarms**
- 🎲 **Dice Roll Support** (e.g., `roll 1d6`, `roll 2d10`)
- 🌐 **Live Weather Reports**
- 📰 **Latest News Updates** (with optional region/topic)
- 📚 **Wikipedia Summary Lookup**
- 🧮 **Math Evaluator** (supports trigonometry, exponentiation, etc.)
- 💱 **Currency Conversion**
- 📏 **Unit Conversion** (e.g., km to miles)
- 🧠 **Smart Suggestions and Help Messages**
- ✍️ **Grammar-friendly input handling**
- 📋 **Copy-to-Clipboard Support**

---

## 🛠️ Tech Stack

- **Python 3.12+**
- **Tkinter** – GUI
- **pyttsx3** – TTS (offline)
- **Requests** – API calls
- **GNews API** – News
- **OpenWeatherMap API** – Weather
- **ExchangeRate.host** – Currency exchange
- **Wikipedia API** – Encyclopedia info

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
[git clone https://github.com/yourusername/chatbot-desktop-app.git](https://github.com/sxoham/Python-Chatbot)
cd Python-Chatbot
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

**OR manually install:**

```bash
pip install requests pyttsx3
```

> Optional: Use `playsound` or `pyaudio` if using audio alerts for alarms.

---

## 📁 Project Structure

```bash
chatbot_project/
│
├── main.py                    # Tkinter UI
├── response_logic.py          # Core logic and NLP
├── long_responses.py          # Generic fallback replies
├── weather_api.py             # OpenWeatherMap handler
├── news_api.py                # GNews API
├── joke_api.py                # Joke fetcher
├── wiki_api.py                # Wikipedia search
├── translate_api.py           # Translation support
├── unit_converter.py          # Unit conversion logic
├── currency_api.py            # Currency exchange logic
├── math_solver.py             # Expression evaluation
├── alarm.py                   # Alarm scheduling
├── reminder_timer.py          # Reminder system
├── dice_api.py                # Dice roll logic
├── tts_speaker.py             # Text-to-Speech utility
└── README.md
```

---

## 🔑 API Keys Setup

- `weather_api.py`: Use [OpenWeatherMap](https://openweathermap.org/api)
- `news_api.py`: Use [GNews API](https://gnews.io/)
- `currency_api.py`: [ExchangeRate.host](https://exchangerate.host/) — no key required

> 🔐 Store your keys as variables inside each module or use a `.env` file (optional).

---

## 🧠 Example Commands

- `"What's the weather in Mumbai?"`
- `"Tell me a joke"`
- `"roll a dice"` or `"roll 3d12"`
- `"convert 100 USD to INR"`
- `"convert 5 km to miles"`
- `"set alarm for 07:30"`
- `"remind me in 2 minutes to check the oven"`
- `"translate hello to french"`
- `"Who is Virat Kohli?"`

---

## 📸 Screenshots

![UI Screenshot](./screenshot.png)

---

## 🧑‍💻 Author

**Soham Mhatre**  
📷 Developer & Photographer  
💬 [ChatGPT + Python Project]

---

