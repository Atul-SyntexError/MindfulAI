"""
Configuration management for the Mental Wellbeing Agent.
Loads environment variables and provides application-wide settings.
"""

from __future__ import annotations

import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# ── Load .env ───────────────────────────────────────────────────────────────
load_dotenv()

# ── API ─────────────────────────────────────────────────────────────────────
GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
GROQ_MAX_TOKENS: int = int(os.getenv("GROQ_MAX_TOKENS", "1024"))
GROQ_TEMPERATURE: float = float(os.getenv("GROQ_TEMPERATURE", "0.7"))

# ── App metadata ────────────────────────────────────────────────────────────
APP_TITLE = "MindfulAI"
APP_SUBTITLE = "Your Personal Mental Wellbeing Companion"
APP_VERSION = "1.0.0"

# ── Memory ──────────────────────────────────────────────────────────────────
MAX_CONVERSATION_TURNS: int = 40  # pairs kept in context window
SUMMARY_THRESHOLD: int = 20       # summarise after this many pairs

# ── Safety ──────────────────────────────────────────────────────────────────
CRISIS_KEYWORDS: list[str] = [
    "kill myself", "end my life", "want to die", "suicide",
    "self-harm", "hurt myself", "no reason to live", "better off dead",
    "can't go on", "ending it all", "don't want to be alive",
    "cut myself", "overdose", "jump off", "hang myself",
]

CRISIS_RESOURCES = {
    "🇺🇸 USA": "988 Suicide & Crisis Lifeline — call or text **988**",
    "🇮🇳 India": "iCall — **9152987821** · Vandrevala Foundation — **1860-2662-345**",
    "🇬🇧 UK": "Samaritans — **116 123**",
    "🌍 International": "befrienders.org/need-to-talk",
}

# ── Mood options ────────────────────────────────────────────────────────────
MOOD_OPTIONS: dict[str, str] = {
    "😊 Happy": "happy",
    "😌 Calm": "calm",
    "😟 Anxious": "anxious",
    "😢 Sad": "sad",
    "😠 Angry": "angry",
    "😩 Stressed": "stressed",
    "😴 Exhausted": "exhausted",
    "🤔 Confused": "confused",
}

MOOD_COLORS: dict[str, str] = {
    "happy": "#4ade80",
    "calm": "#60a5fa",
    "anxious": "#fbbf24",
    "sad": "#818cf8",
    "angry": "#f87171",
    "stressed": "#fb923c",
    "exhausted": "#94a3b8",
    "confused": "#c084fc",
}

STRESS_LEVELS = ["1 — Very Low", "2", "3", "4", "5 — Moderate", "6", "7", "8", "9", "10 — Extreme"]
SLEEP_HOURS = [f"{h} hrs" for h in range(0, 13)]

# ── Logging ─────────────────────────────────────────────────────────────────
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s | %(name)-18s | %(levelname)-7s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger("mindfulai")
