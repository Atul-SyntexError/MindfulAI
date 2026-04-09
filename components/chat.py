"""
Chat UI component — renders conversation history and handles user input.
"""

from __future__ import annotations

import streamlit as st

from config import APP_SUBTITLE, APP_TITLE
from services.memory import get_messages
from utils.helpers import timestamp_now


# ── Header ──────────────────────────────────────────────────────────────────

def render_header() -> None:
    """Render the main page header."""
    st.markdown(
        f"""
        <div style="text-align:center;padding:2rem 0 1rem">
            <div style="font-size:3.2rem;margin-bottom:0.25rem">🧠</div>
            <h1 style="margin:0;font-size:2.4rem;font-weight:700;
                color:#4dc9b0;letter-spacing:-0.3px">
                {APP_TITLE}
            </h1>
            <p style="color:#9aa0a6;margin:0.4rem 0 0;font-size:1.05rem;font-weight:400">
                {APP_SUBTITLE}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Welcome card ────────────────────────────────────────────────────────────

def render_welcome() -> None:
    """Show a welcome card when the conversation is empty."""
    st.markdown(
        """
        <div class="welcome-card">
            <h3 style="margin:0 0 0.6rem">👋 Welcome — I'm glad you're here</h3>
            <p style="margin:0 0 1rem;color:#9aa0a6;line-height:1.6">
                I'm your personal wellbeing companion. I use evidence-based techniques
                to help you work through difficult feelings, build healthier thought patterns,
                and feel a little more grounded each day.
            </p>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem">
                <div class="feature-chip">🎭 &nbsp;Mood tracking</div>
                <div class="feature-chip">📝 &nbsp;Guided journaling</div>
                <div class="feature-chip">🧘 &nbsp;CBT techniques</div>
                <div class="feature-chip">📊 &nbsp;Wellness insights</div>
            </div>
            <p style="margin:1rem 0 0;font-size:0.85rem;color:#6b7280">
                💡 <em>Start by selecting your mood in the sidebar, then tell me what's on your mind.</em>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Message history ─────────────────────────────────────────────────────────

def render_messages() -> None:
    """Render the full chat history with styled bubbles."""
    messages = get_messages()

    if not messages:
        render_welcome()
        return

    for msg in messages:
        with st.chat_message(msg.role, avatar="🙂" if msg.role == "user" else "🧠"):
            st.markdown(msg.content)
            st.caption(msg.timestamp)


# ── Chat input ──────────────────────────────────────────────────────────────

def render_chat_input() -> str | None:
    """Render the chat input and return the user's text (or None)."""
    return st.chat_input(
        placeholder="Tell me what's on your mind…",
    )
