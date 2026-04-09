"""
Sidebar component — mood check-in, wellness inputs, stats, and session controls.
"""

from __future__ import annotations

import plotly.graph_objects as go
import streamlit as st

from config import (
    APP_TITLE,
    APP_VERSION,
    MOOD_COLORS,
    MOOD_OPTIONS,
    SLEEP_HOURS,
    STRESS_LEVELS,
)
from services.memory import (
    clear_messages,
    get_mood_labels,
    get_mood_log,
    get_sleep_log,
    get_stress_log,
    log_journal,
    log_mood,
    log_sleep,
    log_stress,
)


def render_sidebar() -> dict:
    """
    Render the sidebar and return a dict of the user's current check-in data:
    ``{"mood", "stress", "sleep", "journal"}``.
    """
    with st.sidebar:
        # ── Branding ────────────────────────────────────────────────────
        st.markdown(
            f"""
            <div style="text-align:center;padding:0.5rem 0 1rem">
                <span style="font-size:2.2rem">🧠</span>
                <h2 style="margin:0;color:#4dc9b0;
                    font-weight:700;letter-spacing:-0.3px">{APP_TITLE}</h2>
                <span style="font-size:0.75rem;color:#9aa0a6">v{APP_VERSION}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.divider()

        # ── Mood check-in ──────────────────────────────────────────────
        st.markdown("#### 🎭 How are you feeling?")
        mood_label = st.selectbox(
            "Current mood",
            options=list(MOOD_OPTIONS.keys()),
            index=None,
            placeholder="Select your mood…",
            label_visibility="collapsed",
        )
        mood_value: str | None = MOOD_OPTIONS.get(mood_label) if mood_label else None  # type: ignore[arg-type]

        # ── Stress & Sleep ─────────────────────────────────────────────
        st.markdown("#### 📊 Quick Check-in")
        col1, col2 = st.columns(2)
        with col1:
            stress_raw = st.select_slider(
                "Stress",
                options=STRESS_LEVELS,
                value="5 — Moderate",
            )
        with col2:
            sleep_raw = st.selectbox("Sleep", SLEEP_HOURS, index=7)

        stress_val = int(str(stress_raw).split()[0])
        sleep_val = int(str(sleep_raw).split()[0])

        # ── Journal ────────────────────────────────────────────────────
        st.markdown("#### 📝 Journal")
        journal_text = st.text_area(
            "What's on your mind today?",
            placeholder="Write freely — this is your safe space…",
            height=100,
            label_visibility="collapsed",
        )

        # ── Save check-in ─────────────────────────────────────────────
        if st.button("💾  Save Check-in", use_container_width=True, type="primary"):
            if mood_value:
                log_mood(mood_value)
            log_stress(stress_val)
            log_sleep(sleep_val)
            if journal_text.strip():
                log_journal(journal_text.strip())
            st.toast("✅ Check-in saved!", icon="💚")

        st.divider()

        # ── Mini mood chart ────────────────────────────────────────────
        mood_data = get_mood_log()
        if mood_data:
            st.markdown("#### 📈 Mood Trend")
            _render_mood_chart(mood_data)

        # ── Wellness tips ──────────────────────────────────────────────
        stress_log = get_stress_log()
        sleep_log = get_sleep_log()
        if stress_log or sleep_log:
            st.markdown("#### 💡 Personalized Tips")
            _render_tips(stress_log, sleep_log)

        st.divider()

        # ── API key input ──────────────────────────────────────────────
        st.markdown("#### 🔑 API Key")
        key_input = st.text_input(
            "Groq API Key",
            type="password",
            placeholder="gsk_…",
            label_visibility="collapsed",
            value=st.session_state.get("groq_api_key", ""),
        )
        if key_input:
            st.session_state["groq_api_key"] = key_input

        # ── Session controls ───────────────────────────────────────────
        st.divider()
        if st.button("🗑️  New Conversation", use_container_width=True):
            clear_messages()
            st.rerun()

    return {
        "mood": mood_value,
        "stress": stress_val,
        "sleep": sleep_val,
        "journal": journal_text.strip() if journal_text else None,
    }


# ── Private helpers ─────────────────────────────────────────────────────────

def _render_mood_chart(mood_data: list[dict]) -> None:
    """Render a small Plotly dot chart of recent moods."""
    moods = [d["mood"] for d in mood_data[-10:]]
    mood_to_score = {
        "happy": 5, "calm": 4, "confused": 3,
        "anxious": 2, "stressed": 2, "exhausted": 1,
        "sad": 1, "angry": 1,
    }
    scores = [mood_to_score.get(m, 3) for m in moods]
    colors = [MOOD_COLORS.get(m, "#94a3b8") for m in moods]

    fig = go.Figure(go.Scatter(
        x=list(range(1, len(scores) + 1)),
        y=scores,
        mode="lines+markers",
        marker=dict(size=10, color=colors),
        line=dict(color="#3a3f4a", width=2),
        hovertext=moods,
        hoverinfo="text",
    ))
    fig.update_layout(
        height=140,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False, range=[0, 6]),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def _render_tips(stress_log: list[int], sleep_log: list[int]) -> None:
    """Show contextual wellness tips based on recent data."""
    if stress_log:
        avg_stress = sum(stress_log[-5:]) / len(stress_log[-5:])
        if avg_stress >= 7:
            st.info("🧘 Your stress has been high lately. Try a 5-minute breathing exercise before bed.", icon="🌬️")
        elif avg_stress >= 4:
            st.info("🚶 A short walk outside can help reset your stress levels.", icon="🌿")
        else:
            st.success("Your stress levels look manageable — keep it up!", icon="✨")

    if sleep_log:
        avg_sleep = sum(sleep_log[-5:]) / len(sleep_log[-5:])
        if avg_sleep < 5:
            st.warning("😴 You've been sleeping under 5 hours. Prioritizing rest can make a big difference.", icon="🌙")
        elif avg_sleep < 7:
            st.info("💤 Aim for 7-8 hours — even 30 minutes more helps.", icon="🛌")
