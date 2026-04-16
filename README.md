<div align="center">

# 🧠 MindfulAI

### Your Personal Mental Wellbeing Companion

*An AI-powered mental health assistant using evidence-based CBT techniques,
built with Streamlit & Groq LLM*
## 🚀 Live Demo
🔗 [Try the App Here](https://mindfulaii.streamlit.app)

[![Streamlit](https://img.shields.io/badge/Streamlit-1.56-FF4B4B?logo=streamlit)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3_70B-F55036?logo=groq)](https://groq.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](#license)

</div>

---

## ✨ Features

| Feature                    | Description                                                              |
| :------------------------- | :----------------------------------------------------------------------- |
| 🎭 **Mood Tracking**       | Select your current mood with emoji-based picker; visualized over time   |
| 📊 **Stress & Sleep Logs** | Quick slider/dropdown check-ins; personalized tips based on trends       |
| 📝 **Guided Journaling**   | Free-form journal entries that feed context to the AI                    |
| 🧘 **CBT-Based Prompting** | Validate → Explore → Reframe → Empower framework, hidden in natural tone |
| 🔒 **Safety Layer**        | Real-time crisis keyword detection with immediate hotline resources      |
| 📈 **Mood Trend Chart**    | Interactive Plotly sparkline in the sidebar                              |
| 💡 **Wellness Tips**       | Dynamic tips based on your stress and sleep averages                     |
| 💬 **Streaming Responses** | Token-by-token streaming for a natural chat experience                   |
| 🧠 **Context Memory**      | Conversation summarization keeps context within LLM window limits       |
| 🌙 **Premium Dark Theme**  | Glassmorphic cards, fade-up animations, Inter font                      |

---

## 📸 Preview

> The app features a polished dark UI with gradient branding, glassmorphic chat bubbles,
> animated welcome card, and a rich sidebar with mood tracking, journaling, and wellness insights.

---

## 🏗️ Architecture

```
MindfulAI/
├── app.py                  # Main Streamlit entry point
├── config.py               # Configuration & environment loading
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
├── .gitignore
│
├── .streamlit/
│   └── config.toml         # Streamlit theme configuration
│
├── assets/
│   └── style.css           # Premium dark-theme CSS
│
├── components/             # UI layer
│   ├── __init__.py
│   ├── chat.py             # Header, welcome card, message renderer
│   └── sidebar.py          # Mood picker, sliders, journal, tips, chart
│
├── prompts/                # Prompt engineering
│   ├── __init__.py
│   └── templates.py        # System prompt, context builder, summary prompt
│
├── services/               # Business logic
│   ├── __init__.py
│   ├── llm.py              # Groq API wrapper (streaming + sync)
│   └── memory.py           # Session state, context window, mood/stress logs
│
└── utils/                  # Shared utilities
    ├── __init__.py
    ├── safety.py            # Crisis keyword detection + resource card
    └── helpers.py           # Timestamps, formatters, validators
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- **Groq API Key** — get one free at [console.groq.com](https://console.groq.com)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/mindfulai.git
cd mindfulai
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

```bash
# Copy the example env file
cp .env.example .env       # macOS/Linux
copy .env.example .env     # Windows

# Edit .env and replace gsk_YOUR_KEY_HERE with your actual Groq API key
```

**Or** — paste your key directly in the app's sidebar (🔑 API Key section).

### 5. Run the app

```bash
streamlit run app.py
```

The app opens at **http://localhost:8501** 🎉

---

## ⚙️ Configuration

All settings are controlled via environment variables (`.env` file):

| Variable            | Default                    | Description                     |
| :------------------ | :------------------------- | :------------------------------ |
| `GROQ_API_KEY`      | *(required)*               | Your Groq API key               |
| `GROQ_MODEL`        | `llama-3.3-70b-versatile`  | Groq model to use               |
| `GROQ_MAX_TOKENS`   | `1024`                     | Max tokens per response         |
| `GROQ_TEMPERATURE`  | `0.7`                      | Response creativity (0.0 – 1.0) |
| `LOG_LEVEL`         | `INFO`                     | Python logging level            |

---

## 🧘 How the CBT Framework Works

The system prompt uses a 4-step cognitive-behavioral approach — invisible to the user but guiding every response:

1. **Validate** — acknowledge the user's feelings without judgment
2. **Explore** — ask one focused question to understand context
3. **Reframe** — gently offer a new perspective (cognitive restructuring)
4. **Empower** — suggest one small, actionable step

The prompt adapts dynamically based on:
- Current mood selection
- Stress level trends
- Sleep quality
- Journal entries
- Conversation history

---

## 🔒 Safety

MindfulAI includes a real-time safety layer:

- **15+ crisis keywords** are matched against user input with regex
- If triggered, the AI immediately shows **crisis hotline numbers** for USA, India, UK, and international
- The AI **does not** attempt to counsel through acute crisis — it directs to professionals
- A permanent disclaimer footer reinforces that this is **not** a substitute for professional care

---

## 🚢 Deployment

### Streamlit Cloud (Easiest)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Set **Main file path**: `app.py`
5. Add your `GROQ_API_KEY` in **Secrets** (Settings → Secrets):
   ```toml
   GROQ_API_KEY = "gsk_your_actual_key"
   ```
6. Click **Deploy** ✅

### Render

1. Create a new **Web Service** on [render.com](https://render.com)
2. Connect your GitHub repo
3. Set:
   - **Build command**: `pip install -r requirements.txt`
   - **Start command**: `streamlit run app.py --server.port $PORT --server.headless true`
4. Add `GROQ_API_KEY` as an environment variable
5. Deploy ✅

### Railway

1. Create a new project on [railway.app](https://railway.app)
2. Connect your GitHub repo
3. Add a `Procfile`:
   ```
   web: streamlit run app.py --server.port $PORT --server.headless true
   ```
4. Add `GROQ_API_KEY` in Variables
5. Deploy ✅

---

## 🛠️ Development

```bash
# Run with auto-reload (default)
streamlit run app.py

# Enable debug logging
LOG_LEVEL=DEBUG streamlit run app.py
```

### Project modules

| Module              | Responsibility                                    |
| :------------------ | :------------------------------------------------ |
| `config.py`         | Loads `.env`, defines all constants and settings   |
| `services/llm.py`   | Groq API calls with streaming and error handling  |
| `services/memory.py` | Session state, context window, summarization     |
| `prompts/templates.py` | System prompt, context builder, summary prompt |
| `utils/safety.py`   | Crisis detection and resource card                |
| `utils/helpers.py`   | Shared utility functions                         |
| `components/chat.py` | Header, welcome card, message renderer           |
| `components/sidebar.py` | Sidebar UI (mood, stress, sleep, journal, tips) |

---

## ⚠️ Disclaimer

> **MindfulAI is an AI companion, not a licensed therapist or medical professional.**
> It does not provide diagnoses, treatment plans, or medication advice.
> If you are experiencing a mental health crisis, please contact your local emergency services
> or a crisis hotline immediately.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<div align="center">
  <sub>Built with 💜 using Streamlit + Groq</sub>
</div>
