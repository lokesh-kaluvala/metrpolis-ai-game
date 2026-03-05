"""
╔══════════════════════════════════════════════════════════════════════╗
║  METROPOLIS AI v3.0 — Cyberpunk Data Analytics Learning Platform     ║
║  Now with ARCADE: SQL Defense, Speed Coding, Data Sorter,            ║
║  Correlation Guesser, plus the full 5-level campaign.                ║
╚══════════════════════════════════════════════════════════════════════╝

Requirements:
    pip install streamlit plotly pandas numpy scikit-learn fpdf2

Run:
    streamlit run metropolis_ai.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import re
import io
import json
import time
import hashlib
import random
import datetime
import traceback
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, f1_score, precision_score, recall_score,
    confusion_matrix,
)
from sklearn.preprocessing import StandardScaler
from fpdf import FPDF

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎨 CYBERPUNK CSS v3
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CYBER_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Share+Tech+Mono&family=Rajdhani:wght@300;400;500;600;700&display=swap');

    :root {
        --neon-green: #00ff88;
        --neon-blue: #00d4ff;
        --neon-pink: #ff0080;
        --neon-red: #ff3344;
        --neon-yellow: #ffee00;
        --neon-purple: #bf00ff;
        --bg-dark: #060610;
        --glass-bg: rgba(0, 255, 136, 0.03);
        --glass-border: rgba(0, 255, 136, 0.12);
        --text-primary: #d0d0d8;
        --text-dim: #555570;
    }

    .stApp {
        background: var(--bg-dark);
        background-image:
            radial-gradient(ellipse at 15% 50%, rgba(0,255,136,0.04) 0%, transparent 50%),
            radial-gradient(ellipse at 85% 20%, rgba(0,212,255,0.03) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 85%, rgba(191,0,255,0.02) 0%, transparent 50%);
    }
    .stApp > header { background: transparent !important; }

    .stApp::after {
        content: '';
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: repeating-linear-gradient(
            0deg, transparent, transparent 2px,
            rgba(0,255,136,0.006) 2px, rgba(0,255,136,0.006) 4px
        );
        pointer-events: none;
        z-index: 1000;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(4,4,12,0.98) 0%, rgba(8,8,20,0.98) 100%) !important;
        border-right: 1px solid var(--glass-border) !important;
    }
    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        font-family: 'Orbitron', monospace !important;
        color: var(--neon-green) !important;
        text-shadow: 0 0 8px rgba(0,255,136,0.3);
        letter-spacing: 2px;
    }
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown li {
        font-family: 'Share Tech Mono', monospace !important;
        color: var(--text-primary) !important;
        font-size: 0.82rem;
    }

    .cyber-glass {
        background: linear-gradient(135deg, rgba(0,255,136,0.03), rgba(0,212,255,0.02));
        border: 1px solid var(--glass-border);
        border-radius: 6px;
        padding: 1.4rem;
        margin: 0.6rem 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 0 12px rgba(0,255,136,0.04), inset 0 0 20px rgba(0,255,136,0.015);
        position: relative;
        overflow: hidden;
    }
    .cyber-glass::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 50px; height: 1px;
        background: linear-gradient(90deg, var(--neon-green), transparent);
    }
    .cyber-glass::after {
        content: '';
        position: absolute;
        bottom: 0; right: 0;
        width: 50px; height: 1px;
        background: linear-gradient(270deg, var(--neon-blue), transparent);
    }

    .cyber-glass-danger {
        background: linear-gradient(135deg, rgba(255,51,68,0.04), rgba(255,0,128,0.02));
        border: 1px solid rgba(255,51,68,0.2);
        border-radius: 6px;
        padding: 1.4rem;
        margin: 0.6rem 0;
        box-shadow: 0 0 12px rgba(255,51,68,0.06);
        position: relative;
        overflow: hidden;
    }
    .cyber-glass-danger::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 50px; height: 1px;
        background: linear-gradient(90deg, var(--neon-red), transparent);
    }

    .cyber-glass-success {
        background: linear-gradient(135deg, rgba(0,255,136,0.06), rgba(0,212,255,0.03));
        border: 1px solid rgba(0,255,136,0.25);
        border-radius: 6px;
        padding: 1.4rem;
        margin: 0.6rem 0;
        box-shadow: 0 0 20px rgba(0,255,136,0.08);
    }

    .cyber-glass-purple {
        background: linear-gradient(135deg, rgba(191,0,255,0.05), rgba(0,212,255,0.02));
        border: 1px solid rgba(191,0,255,0.2);
        border-radius: 6px;
        padding: 1.4rem;
        margin: 0.6rem 0;
        box-shadow: 0 0 12px rgba(191,0,255,0.06);
        position: relative;
    }
    .cyber-glass-purple::before {
        content: '';
        position: absolute;
        top: 0; left: 0;
        width: 50px; height: 1px;
        background: linear-gradient(90deg, var(--neon-purple), transparent);
    }

    .stMarkdown h1 {
        font-family: 'Orbitron', monospace !important;
        color: var(--neon-green) !important;
        text-shadow: 0 0 15px rgba(0,255,136,0.25);
        letter-spacing: 3px;
        font-weight: 800 !important;
    }
    .stMarkdown h2 {
        font-family: 'Orbitron', monospace !important;
        color: var(--neon-blue) !important;
        text-shadow: 0 0 12px rgba(0,212,255,0.25);
        letter-spacing: 2px;
    }
    .stMarkdown h3 {
        font-family: 'Rajdhani', sans-serif !important;
        color: var(--neon-green) !important;
        font-weight: 600 !important;
    }
    .stMarkdown p, .stMarkdown li {
        font-family: 'Share Tech Mono', monospace !important;
        color: var(--text-primary) !important;
        font-size: 0.88rem;
        line-height: 1.65;
    }
    .stMarkdown code {
        background: rgba(0,255,136,0.08) !important;
        color: var(--neon-green) !important;
        border: 1px solid rgba(0,255,136,0.15) !important;
        border-radius: 3px;
        padding: 1px 5px;
        font-family: 'Share Tech Mono', monospace !important;
    }

    .stButton > button {
        font-family: 'Orbitron', monospace !important;
        background: transparent !important;
        color: var(--neon-green) !important;
        border: 1px solid var(--neon-green) !important;
        border-radius: 4px !important;
        padding: 0.55rem 1.4rem !important;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 0.78rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 8px rgba(0,255,136,0.08);
    }
    .stButton > button:hover {
        background: rgba(0,255,136,0.08) !important;
        box-shadow: 0 0 20px rgba(0,255,136,0.25) !important;
        transform: translateY(-1px);
    }

    .stTextInput input, .stTextArea textarea {
        font-family: 'Share Tech Mono', monospace !important;
        background: rgba(0,255,136,0.02) !important;
        border: 1px solid rgba(0,255,136,0.15) !important;
        color: var(--neon-green) !important;
        border-radius: 4px !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: var(--neon-green) !important;
        box-shadow: 0 0 12px rgba(0,255,136,0.15) !important;
    }

    .stSlider [data-testid="stThumbValue"] {
        font-family: 'Share Tech Mono', monospace !important;
        color: var(--neon-green) !important;
    }

    .stProgress > div > div {
        background: linear-gradient(90deg, var(--neon-green), var(--neon-blue)) !important;
        box-shadow: 0 0 8px rgba(0,255,136,0.3);
        border-radius: 4px;
    }

    [data-testid="stMetric"] {
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
        border-radius: 6px;
        padding: 0.8rem;
    }
    [data-testid="stMetricLabel"] {
        font-family: 'Rajdhani', sans-serif !important;
        color: var(--text-dim) !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    [data-testid="stMetricValue"] {
        font-family: 'Orbitron', monospace !important;
        color: var(--neon-green) !important;
        text-shadow: 0 0 8px rgba(0,255,136,0.25);
    }

    .stTabs [data-baseweb="tab-list"] { gap: 4px; }
    .stTabs [data-baseweb="tab"] {
        font-family: 'Rajdhani', sans-serif !important;
        color: var(--text-dim) !important;
        background: transparent;
    }
    .stTabs [aria-selected="true"] {
        color: var(--neon-green) !important;
        border-bottom: 2px solid var(--neon-green) !important;
    }

    .neon-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--neon-green), transparent);
        margin: 1.2rem 0;
        box-shadow: 0 0 6px rgba(0,255,136,0.25);
    }
    .landing-title {
        font-family: 'Orbitron', monospace;
        font-size: 3.2rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #00ff88, #00d4ff, #bf00ff, #00ff88);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradient-shift 6s ease-in-out infinite;
        letter-spacing: 8px;
    }
    @keyframes gradient-shift {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    .subtitle-glow {
        font-family: 'Share Tech Mono', monospace;
        text-align: center;
        color: #555570;
        font-size: 0.95rem;
        letter-spacing: 5px;
        text-transform: uppercase;
    }

    .terminal-output {
        background: rgba(0,0,0,0.6);
        border: 1px solid rgba(0,255,136,0.15);
        border-radius: 4px;
        padding: 1rem;
        font-family: 'Share Tech Mono', monospace;
        font-size: 0.82rem;
        color: var(--neon-green);
        white-space: pre-wrap;
        overflow-x: auto;
        max-height: 300px;
        overflow-y: auto;
    }
    .terminal-output .error { color: var(--neon-red); }
    .terminal-output .info { color: var(--neon-blue); }

    .stat-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 0.8rem;
        margin: 0.8rem 0;
    }
    .stat-item {
        background: rgba(0,255,136,0.03);
        border: 1px solid rgba(0,255,136,0.1);
        border-radius: 6px;
        padding: 0.8rem;
        text-align: center;
    }
    .stat-item .label {
        font-family: 'Rajdhani', sans-serif;
        color: var(--text-dim);
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stat-item .value {
        font-family: 'Orbitron', monospace;
        color: var(--neon-green);
        font-size: 1.3rem;
        text-shadow: 0 0 8px rgba(0,255,136,0.3);
    }

    .arcade-card {
        background: linear-gradient(135deg, rgba(191,0,255,0.04), rgba(0,212,255,0.03));
        border: 1px solid rgba(191,0,255,0.15);
        border-radius: 8px;
        padding: 1.2rem;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .arcade-card:hover {
        border-color: rgba(191,0,255,0.4);
        box-shadow: 0 0 20px rgba(191,0,255,0.15);
    }
    .arcade-card .game-icon { font-size: 2rem; }
    .arcade-card .game-title {
        font-family: 'Orbitron', monospace;
        color: var(--neon-purple);
        font-size: 0.8rem;
        letter-spacing: 1px;
        margin-top: 0.4rem;
    }
    .arcade-card .game-desc {
        font-family: 'Share Tech Mono', monospace;
        color: var(--text-dim);
        font-size: 0.7rem;
        margin-top: 0.3rem;
    }
    .arcade-card .game-xp {
        font-family: 'Rajdhani', sans-serif;
        color: var(--neon-yellow);
        font-size: 0.75rem;
        margin-top: 0.3rem;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
</style>
"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧠 STATE MANAGEMENT v3
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEFAULT_STATE = {
    "initialized": False,
    "user_name": "AGENT",
    "user_xp": 0,
    "current_level": 0,   # 0=landing, 1-5=campaign, 10=arcade hub,
                           # 11=sql, 12=speed, 13=sorter, 14=correlation
    "unlocked_badges": [],
    "inventory": [],
    "mission_log": [],
    # Campaign
    "level1_complete": False, "level1_step": 0, "level1_attempts": 0, "level1_dataset": None,
    "level2_complete": False, "level2_attempts": 0, "anomaly_dataset": None, "anomaly_id": None,
    "level3_complete": False, "level3_attempts": 0, "boss_history": [],
    "level4_complete": False, "level4_answers": {},
    "level5_complete": False,
    # Arcade — SQL Defense
    "sql_wave": 0, "sql_score": 0, "sql_best": 0, "sql_lives": 3, "sql_active": False,
    # Arcade — Speed Code
    "speed_round": 0, "speed_score": 0, "speed_best": 0, "speed_active": False,
    "speed_start_time": None, "speed_current_q": None,
    # Arcade — Data Sorter
    "sorter_score": 0, "sorter_best": 0, "sorter_round": 0, "sorter_active": False,
    # Arcade — Correlation Guesser
    "corr_score": 0, "corr_best": 0, "corr_round": 0, "corr_active": False,
    "corr_data": None, "corr_true_r": None,
    # Arcade totals
    "arcade_games_played": 0,
    "session_start": None,
}


def init_state():
    for key, val in DEFAULT_STATE.items():
        if key not in st.session_state:
            if isinstance(val, (list, dict)):
                st.session_state[key] = type(val)(val)
            else:
                st.session_state[key] = val
    if st.session_state.session_start is None:
        st.session_state.session_start = datetime.datetime.now().isoformat()


def add_xp(amount, reason=""):
    st.session_state.user_xp += amount
    log_event(f"+{amount} XP" + (f" ({reason})" if reason else ""))


def log_event(msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    st.session_state.mission_log.append(f"[{ts}] {msg}")
    if len(st.session_state.mission_log) > 150:
        st.session_state.mission_log = st.session_state.mission_log[-150:]


def get_rank():
    xp = st.session_state.user_xp
    for thresh, name, tier in [
        (2000, "⬡ MASTER ARCHITECT", 7), (1500, "⬢ SYSTEM OVERLORD", 6),
        (1000, "◈ NEURAL HACKER", 5), (600, "◇ GRID ANALYST", 4),
        (350, "△ CYBER SCOUT", 3), (150, "△ DATA SCOUT", 2), (1, "○ INITIATE", 1),
    ]:
        if xp >= thresh: return name, tier
    return "◌ UNLINKED", 0


def get_sync_pct():
    return sum([st.session_state.level1_complete, st.session_state.level2_complete,
                st.session_state.level3_complete, st.session_state.level4_complete,
                st.session_state.level5_complete]) / 5


def get_session_duration():
    if st.session_state.session_start:
        start = datetime.datetime.fromisoformat(st.session_state.session_start)
        delta = datetime.datetime.now() - start
        return f"{int(delta.total_seconds()//60)}m {int(delta.total_seconds()%60)}s"
    return "0m 0s"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧩 UI COMPONENTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def glass_card(content, variant="default"):
    cls_map = {"default": "cyber-glass", "danger": "cyber-glass-danger",
               "success": "cyber-glass-success", "purple": "cyber-glass-purple"}
    st.markdown(f'<div class="{cls_map.get(variant, "cyber-glass")}">{content}</div>', unsafe_allow_html=True)

def neon_divider():
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

def terminal_output(text, style="normal"):
    cls = {"error": "error", "info": "info"}.get(style, "")
    escaped = text.replace("<", "&lt;").replace(">", "&gt;")
    st.markdown(f'<div class="terminal-output"><span class="{cls}">{escaped}</span></div>', unsafe_allow_html=True)

def stat_grid(stats):
    items = "".join(f'<div class="stat-item"><div class="label">{l}</div><div class="value">{v}</div></div>' for l, v in stats)
    st.markdown(f'<div class="stat-grid">{items}</div>', unsafe_allow_html=True)

def mission_header(level_num, title, subtitle):
    icons = {1: "⟐", 2: "◈", 3: "⬡", 4: "◆", 5: "★", 10: "🕹️", 11: "🛡️", 12: "⚡", 13: "📦", 14: "📊"}
    st.markdown(f"## {icons.get(level_num, '●')} {title}")
    neon_divider()
    glass_card(f'<p style="color:#00d4ff; margin:0;"><strong>BRIEFING:</strong> {subtitle}</p>')

def safe_exec_user_code(code_str, df):
    dangerous = ["import os", "import sys", "exec(", "eval(", "__",
                  "open(", "subprocess", "shutil", "pathlib", "glob", "socket", "requests", "import "]
    code_lower = code_str.lower().strip()
    for d in dangerous:
        if d in code_lower and d != "import ":
            return df, f"BLOCKED: '{d}' is not allowed.", False
    if "import " in code_lower:
        if not any(s in code_lower for s in ["import pandas", "import numpy"]):
            return df, "BLOCKED: Only pandas/numpy imports allowed.", False
    env = {"df": df.copy(), "pd": pd, "np": np}
    try:
        exec(code_str, env)
        result_df = env.get("df", df)
        if not isinstance(result_df, pd.DataFrame):
            return df, "Warning: df is no longer a DataFrame.", False
        return result_df, f"OK. Shape: {result_df.shape[0]} x {result_df.shape[1]}", True
    except SyntaxError:
        try:
            result = eval(code_str, env)
            if isinstance(result, pd.DataFrame):
                return result, f"OK. Shape: {result.shape[0]} x {result.shape[1]}", True
            return df, f"Result: {type(result).__name__} (df unchanged)", True
        except Exception as e:
            return df, f"Error: {e}", False
    except Exception as e:
        return df, f"Error: {e}", False


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊 DATA GENERATORS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def generate_corrupted_dataset():
    np.random.seed(42)
    n = 80
    df = pd.DataFrame({
        "sensor_id": [f"S-{i:03d}" for i in range(n)],
        "timestamp": pd.date_range("2087-01-01", periods=n, freq="h"),
        "temperature_c": np.round(np.random.normal(22, 5, n), 1),
        "humidity_pct": np.round(np.random.uniform(30, 80, n), 1),
        "power_kw": np.round(np.random.exponential(50, n), 2),
        "sector": np.random.choice(["Alpha", "Beta", "Gamma", "Delta"], n),
        "status": np.random.choice(["online", "standby", "error"], n, p=[0.7, 0.2, 0.1]),
    })
    df.loc[7, "temperature_c"] = 500.0
    df.loc[23, "temperature_c"] = -273.5
    df.loc[41, "temperature_c"] = 999.9
    df.loc[58, "temperature_c"] = -300.0
    df.loc[[3, 15, 28, 44, 52, 67], "humidity_pct"] = np.nan
    df.loc[[10, 33, 71], "power_kw"] = np.nan
    df.loc[[5, 20], "sector"] = np.nan
    dups = df.iloc[[5, 12, 20, 35]].copy()
    df = pd.concat([df, dups], ignore_index=True)
    return df

def generate_anomaly_dataset():
    np.random.seed(99)
    n = 150
    ids = [f"NODE-{i:04d}" for i in range(n)]
    cx = np.concatenate([np.random.normal(30,7,50), np.random.normal(70,9,50), np.random.normal(50,5,47)])
    cy = np.concatenate([np.random.normal(60,6,50), np.random.normal(40,8,50), np.random.normal(82,4,47)])
    cx = np.append(cx, [95.0, 5.0, 50.0])
    cy = np.append(cy, [5.0, 95.0, 5.0])
    power = np.round(np.random.uniform(10, 100, n), 1)
    sectors = np.random.choice(["Alpha", "Beta", "Gamma", "Delta"], n)
    df = pd.DataFrame({"node_id": ids, "grid_load_x": np.round(cx,2), "grid_load_y": np.round(cy,2),
                        "power_output": power, "sector": sectors})
    return df, ids[147]

def generate_cyber_attack_dataset():
    np.random.seed(2087)
    n = 1000
    ps = np.random.exponential(500,n)+np.random.normal(0,50,n)
    lat = np.random.gamma(2,10,n); nc = np.random.poisson(15,n)
    ent = np.random.beta(2,5,n); pr = np.random.uniform(0,1,n)
    ie = np.random.binomial(1,0.4,n); psc = np.random.poisson(3,n)
    sd = np.random.exponential(30,n)
    logit = -2.5+0.0015*ps+0.04*lat+0.08*nc+3.5*ent-1.2*pr+0.6*ie+0.15*psc-0.01*sd+np.random.normal(0,0.6,n)
    label = (1/(1+np.exp(-logit)) > 0.5).astype(int)
    return pd.DataFrame({"packet_size": np.round(ps,1), "latency_ms": np.round(lat,2),
        "num_connections": nc, "entropy": np.round(ent,4), "payload_ratio": np.round(pr,4),
        "is_encrypted": ie, "port_scan_count": psc, "session_duration": np.round(sd,2), "is_attack": label})


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🏠 LANDING PAGE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def render_landing():
    st.markdown("")
    st.markdown('<div class="landing-title">METROPOLIS AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-glow">Neural Analytics Training System v3.0</div>', unsafe_allow_html=True)
    st.markdown("")
    glass_card("""
        <p style="text-align:center; color:#888; font-size:0.85rem; line-height:1.9;">
        The city's neural grid is failing. Corrupted datasets, rogue AIs, cyber-attacks.<br>
        <span style="color:#00ff88;">5-mission campaign + 4 arcade mini-games. Real Python. Real ML.</span></p>
    """)
    st.markdown("")
    cols = st.columns(9)
    items = [("01","CLEAN","Pandas"),("02","HUNT","EDA"),("03","BOSS","ML"),
             ("04","QUIZ","Theory"),("05","CERT","Report"),("","",""),
             ("🛡️","SQL DEF",""),("⚡","SPEED",""),("📊","CORR","")]
    for col, (n, t, d) in zip(cols, items):
        if n:
            with col:
                glass_card(f"""<div style="text-align:center;">
                    <span style="font-family:'Orbitron',monospace;color:#555;font-size:1.1rem;">{n}</span><br>
                    <span style="font-family:'Rajdhani',sans-serif;color:#00d4ff;font-size:0.65rem;">{t}</span>
                    </div>""")
    st.markdown("")
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        name = st.text_input("CODENAME", value="", placeholder="Enter operative handle...", label_visibility="collapsed")
        st.markdown("")
        if st.button("⟐  INITIALIZE NEURAL LINK  ⟐", use_container_width=True):
            if not name.strip():
                st.warning("Enter a codename.")
            else:
                st.session_state.initialized = True
                st.session_state.user_name = name.strip().upper()[:20]
                st.session_state.current_level = 1
                add_xp(10, "Neural Link established")
                log_event(f"Operative {st.session_state.user_name} connected")
                st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧹 LEVEL 1-5 (CAMPAIGN) — Same as v2 but compact
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LEVEL1_TASKS = [
    {"title": "MISSION 1.1 — Purge Duplicates", "briefing": "Remove **duplicate rows**.",
     "hint": "`df = df.drop_duplicates()`",
     "validator": lambda b, a: a.shape[0] < b.shape[0] and a.duplicated().sum() == 0,
     "error_msg": "Duplicates still present.", "xp": 60},
    {"title": "MISSION 1.2 — Patch Missing Values", "briefing": "Handle **NaN values** — drop or fill.",
     "hint": "`df = df.dropna()` or `df = df.fillna(0)`",
     "validator": lambda b, a: a.isnull().sum().sum() < b.isnull().sum().sum(),
     "error_msg": "Missing values remain.", "xp": 60},
    {"title": "MISSION 1.3 — Neutralize Outliers", "briefing": "Filter temperature to **-50 to 60** range.",
     "hint": "`df = df[(df['temperature_c'] > -50) & (df['temperature_c'] < 60)]`",
     "validator": lambda b, a: a["temperature_c"].max() <= 60 and a["temperature_c"].min() >= -50,
     "error_msg": "Outliers remain.", "xp": 80},
]

def render_level1():
    mission_header(1, "LEVEL 1 — DATA FORENSICS",
        "Corrupted sensor dataset. Issue <strong>real Pandas commands</strong> to clean it.")
    step = st.session_state.level1_step
    if st.session_state.level1_dataset is None:
        st.session_state.level1_dataset = generate_corrupted_dataset()
    df = st.session_state.level1_dataset
    h1, h2, h3, h4 = st.columns(4)
    h1.metric("Rows", df.shape[0]); h2.metric("Duplicates", int(df.duplicated().sum()))
    h3.metric("Missing", int(df.isnull().sum().sum()))
    h4.metric("Outliers", int(((df["temperature_c"]>60)|(df["temperature_c"]<-50)).sum()) if "temperature_c" in df.columns else 0)
    with st.expander("View Dataset"): st.dataframe(df.head(20), use_container_width=True, height=300)
    neon_divider()
    if step >= len(LEVEL1_TASKS):
        if not st.session_state.level1_complete:
            st.session_state.level1_complete = True
            if "Data Surgeon" not in st.session_state.unlocked_badges: st.session_state.unlocked_badges.append("Data Surgeon")
            st.session_state.inventory.append("Clean Dataset v1"); log_event("Level 1 complete")
        glass_card('<div style="text-align:center;"><span style="font-size:2rem;">🏅</span><br><span style="color:#00ff88;font-family:Orbitron,monospace;">DATA SURGEON BADGE</span></div>', "success")
        if st.button("PROCEED TO LEVEL 2", key="l1n"): st.session_state.current_level = 2; st.rerun()
        return
    task = LEVEL1_TASKS[step]
    st.markdown(f"### {task['title']}"); st.markdown(task["briefing"])
    with st.expander("Hint"): st.code(task["hint"], language="python")
    user_code = st.text_area("Pandas command:", key=f"l1c_{step}", height=70, placeholder="e.g. df = df.drop_duplicates()")
    if st.button("EXECUTE", key=f"l1e_{step}"):
        if not user_code.strip(): st.warning("Enter a command."); return
        st.session_state.level1_attempts += 1
        before = df.copy(); result, output, ok = safe_exec_user_code(user_code, df)
        terminal_output(f">>> {user_code}\n{output}", "info" if ok else "error")
        if ok:
            try: passed = task["validator"](before, result)
            except: passed = False
            if passed:
                st.session_state.level1_dataset = result; add_xp(task["xp"], task["title"])
                st.session_state.level1_step = step + 1; st.success(f"PATCH APPLIED — +{task['xp']} XP"); st.rerun()
            else: st.error(task["error_msg"])
        else: st.error("Execution failed.")


def render_level2():
    mission_header(2, "LEVEL 2 — ANOMALY HUNT", "Find the rogue node hiding in the power grid scatter plot.")
    if st.session_state.level2_complete:
        glass_card('<div style="text-align:center;"><span style="font-size:2rem;">🔍</span><br><span style="color:#00d4ff;font-family:Orbitron,monospace;">GRID ANALYST BADGE</span></div>', "success")
        if st.button("PROCEED TO LEVEL 3", key="l2n"): st.session_state.current_level = 3; st.rerun()
        return
    if st.session_state.anomaly_dataset is None:
        df, aid = generate_anomaly_dataset(); st.session_state.anomaly_dataset = df; st.session_state.anomaly_id = aid
    else: df = st.session_state.anomaly_dataset; aid = st.session_state.anomaly_id
    fig = px.scatter(df, x="grid_load_x", y="grid_load_y", color="sector", size="power_output",
        hover_data=["node_id","power_output"], color_discrete_sequence=["#00ff88","#00d4ff","#bf00ff","#ffee00"])
    fig.update_layout(plot_bgcolor="rgba(8,8,18,0.9)", paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Share Tech Mono",color="#999"), height=500,
        xaxis=dict(gridcolor="rgba(0,255,136,0.04)"), yaxis=dict(gridcolor="rgba(0,255,136,0.04)"))
    st.plotly_chart(fig, use_container_width=True)
    np.random.seed(7); decoys = np.random.choice(df["node_id"].values[:140], 5, replace=False).tolist()
    choices = sorted(set([aid]+decoys)); np.random.shuffle(choices)
    selected = st.radio("Select anomaly node:", choices, index=None, key="l2r")
    if st.button("SUBMIT", key="l2s"):
        st.session_state.level2_attempts += 1
        if selected == aid:
            add_xp(200, "Anomaly found"); st.session_state.level2_complete = True
            if "Grid Analyst" not in st.session_state.unlocked_badges: st.session_state.unlocked_badges.append("Grid Analyst")
            st.session_state.inventory.append("Anomaly Report"); log_event("Level 2 complete")
            st.success(f"ANOMALY: {aid} — +200 XP"); st.balloons(); st.rerun()
        elif selected: st.error(f"{selected} is clean. Check the extreme corners.")
        else: st.warning("Select a node.")
        if st.session_state.level2_attempts >= 3: st.info("Hint: highest grid_load_x, lowest grid_load_y.")


def render_level3():
    mission_header(3, "LEVEL 3 — THE ROGUE AI", "Train a Random Forest. <span style='color:#00d4ff;'>Target: F1 &gt; 0.88</span>")
    AI = {"acc": 0.85, "f1": 0.83, "pre": 0.84, "rec": 0.82}
    if st.session_state.level3_complete:
        glass_card('<div style="text-align:center;"><span style="font-size:2.5rem;">🏆</span><br><span style="color:#00ff88;font-family:Orbitron,monospace;">ROGUE AI SLAYER</span></div>', "success")
        if st.button("PROCEED TO LEVEL 4", key="l3n"): st.session_state.current_level = 4; st.rerun()
        return
    c1,c2,c3,c4 = st.columns(4)
    n_est = c1.slider("n_estimators",50,500,150,25,key="bn"); md = c2.slider("max_depth",3,30,12,key="bm")
    mss = c3.slider("min_samples_split",2,20,2,key="bs"); msl = c4.slider("min_samples_leaf",1,15,1,key="bl")
    with st.expander("Advanced"):
        scale = st.checkbox("StandardScaler",False,key="bsc"); ts = st.slider("Test size",0.15,0.40,0.25,0.05,key="bt")
    if st.button("EXECUTE MODEL", use_container_width=True, key="br"):
        st.session_state.level3_attempts += 1
        with st.spinner("Training..."):
            df = generate_cyber_attack_dataset(); X = df.drop("is_attack",axis=1); y = df["is_attack"]
            Xtr,Xte,ytr,yte = train_test_split(X,y,test_size=ts,random_state=42,stratify=y)
            if scale: sc = StandardScaler(); Xtr = sc.fit_transform(Xtr); Xte = sc.transform(Xte)
            clf = RandomForestClassifier(n_estimators=n_est,max_depth=md,min_samples_split=mss,min_samples_leaf=msl,random_state=42,n_jobs=-1)
            clf.fit(Xtr,ytr); yp = clf.predict(Xte)
            ua=round(accuracy_score(yte,yp),4); uf=round(f1_score(yte,yp),4)
            up=round(precision_score(yte,yp),4); ur=round(recall_score(yte,yp),4)
        st.session_state.boss_history.append({"n":st.session_state.level3_attempts,"f1":uf,"acc":ua})
        m1,m2,m3,m4 = st.columns(4)
        m1.metric("Accuracy",f"{ua:.4f}",f"{ua-AI['acc']:+.4f}"); m2.metric("F1",f"{uf:.4f}",f"{uf-AI['f1']:+.4f}")
        m3.metric("Precision",f"{up:.4f}",f"{up-AI['pre']:+.4f}"); m4.metric("Recall",f"{ur:.4f}",f"{ur-AI['rec']:+.4f}")
        cats=["Accuracy","F1","Precision","Recall"]
        fig=go.Figure()
        fig.add_trace(go.Scatterpolar(r=[ua,uf,up,ur,ua],theta=cats+[cats[0]],fill='toself',name="YOU",line=dict(color='#00d4ff',width=2),fillcolor='rgba(0,212,255,0.12)'))
        fig.add_trace(go.Scatterpolar(r=[AI["acc"],AI["f1"],AI["pre"],AI["rec"],AI["acc"]],theta=cats+[cats[0]],fill='toself',name="ROGUE AI",line=dict(color='#ff3344',width=2),fillcolor='rgba(255,51,68,0.12)'))
        fig.update_layout(polar=dict(bgcolor="rgba(8,8,18,0.9)",radialaxis=dict(range=[0.5,1.0],gridcolor="rgba(0,255,136,0.08)",color="#555")),
            paper_bgcolor="rgba(0,0,0,0)",font=dict(family="Share Tech Mono",color="#999"),height=400)
        st.plotly_chart(fig, use_container_width=True)
        if uf > 0.88:
            add_xp(400,"Boss defeated"); st.session_state.level3_complete = True
            if "Rogue AI Slayer" not in st.session_state.unlocked_badges: st.session_state.unlocked_badges.append("Rogue AI Slayer")
            st.session_state.inventory.append("AI Core Fragment"); log_event(f"Boss defeated F1={uf}")
            st.success(f"ROGUE AI NEUTRALIZED! F1={uf}"); st.balloons()
        else:
            st.error(f"F1={uf} — Need > 0.88")
            hints=["Increase n_estimators to 200+","Tune max_depth 8-15","Try n_est=300,depth=12","Enable StandardScaler","Sweet spot: 250-400 trees, depth 10-15"]
            st.info(f"Tip: {hints[min(st.session_state.level3_attempts-1,len(hints)-1)]}")


QUIZ = [
    {"q":"Best metric for **imbalanced classes**?","o":["Accuracy","F1-Score","R-Squared","MAE"],"a":"F1-Score",
     "e":"Accuracy misleads with imbalanced data. F1 balances precision/recall."},
    {"q":"What does `df.groupby('sector').agg({'sales':'mean'})` do?",
     "o":["Filters by sector","Average sales per sector","Sorts by sector","Drops duplicates"],
     "a":"Average sales per sector","e":"groupby splits, agg computes mean per group."},
    {"q":"Increasing max_depth causes:","o":["Underfitting","Overfitting","Faster training","Less memory"],
     "a":"Overfitting","e":"Deeper trees memorize noise."},
    {"q":"Worst missing value approach?","o":["Drop rows","Fill with median","Fill with 0 everywhere","KNN imputation"],
     "a":"Fill with 0 everywhere","e":"Zero introduces bias; median/KNN preserve distribution."},
    {"q":"Best chart for two continuous variables?","o":["Bar","Pie","Scatter","Histogram"],
     "a":"Scatter","e":"Scatter plots show correlations and outliers."},
    {"q":"stratify=y in train_test_split ensures:","o":["50/50 split","Class proportions preserved","Sorted data","Numeric only"],
     "a":"Class proportions preserved","e":"Critical for imbalanced datasets."},
]

def render_level4():
    mission_header(4, "LEVEL 4 — INTEL BRIEFING", "Score 5/6 to pass.")
    if st.session_state.level4_complete:
        glass_card('<div style="text-align:center;"><span style="font-size:2rem;">🧠</span><br><span style="color:#bf00ff;font-family:Orbitron,monospace;">INTEL OFFICER BADGE</span></div>', "success")
        if st.button("PROCEED TO LEVEL 5", key="l4n"): st.session_state.current_level = 5; st.rerun()
        return
    ans = st.session_state.level4_answers
    for i, q in enumerate(QUIZ):
        st.markdown(f"**Q{i+1}.** {q['q']}")
        c = st.radio(f"Q{i+1}:", q["o"], index=None, key=f"q_{i}", label_visibility="collapsed")
        if c: ans[str(i)] = c
        st.markdown("---")
    if st.button("SUBMIT", key="l4s"):
        if len(ans) < len(QUIZ): st.warning(f"Answer all. ({len(ans)}/{len(QUIZ)})"); return
        correct = sum(1 for i, q in enumerate(QUIZ) if ans.get(str(i)) == q["a"])
        for i, q in enumerate(QUIZ):
            ok = ans.get(str(i)) == q["a"]
            st.markdown(f"{'✅' if ok else '❌'} **Q{i+1}:** {q['a']} — *{q['e']}*")
        if correct >= 5:
            add_xp(250,"Intel passed"); st.session_state.level4_complete = True
            if "Intel Officer" not in st.session_state.unlocked_badges: st.session_state.unlocked_badges.append("Intel Officer")
            st.success(f"PASSED — {correct}/6, +250 XP"); st.balloons()
        else: st.error(f"{correct}/6 — Need 5+"); st.session_state.level4_answers = {}


def generate_certificate_pdf(name, xp, badges, duration):
    pdf = FPDF(); pdf.add_page("L"); pw, ph = pdf.w, pdf.h
    pdf.set_fill_color(8,8,18); pdf.rect(0,0,pw,ph,"F")
    pdf.set_draw_color(0,255,136); pdf.set_line_width(1.5); pdf.rect(10,10,pw-20,ph-20,"D")
    pdf.set_line_width(0.4); pdf.rect(14,14,pw-28,ph-28,"D")
    pdf.set_font("Helvetica","B",34); pdf.set_text_color(0,255,136); pdf.set_y(28)
    pdf.cell(0,18,"METROPOLIS AI",align="C",new_x="LMARGIN",new_y="NEXT")
    pdf.set_font("Helvetica","",12); pdf.set_text_color(0,212,255)
    pdf.cell(0,8,"Neural Analytics Training System - Certificate of Mastery",align="C",new_x="LMARGIN",new_y="NEXT")
    yl = pdf.get_y()+6; pdf.set_line_width(0.3); pdf.line(50,yl,pw-50,yl); pdf.set_y(yl+10)
    pdf.set_font("Helvetica","",12); pdf.set_text_color(180,180,190)
    pdf.cell(0,8,"This certifies that",align="C",new_x="LMARGIN",new_y="NEXT")
    pdf.set_font("Helvetica","B",26); pdf.set_text_color(0,255,136)
    pdf.cell(0,14,name,align="C",new_x="LMARGIN",new_y="NEXT")
    pdf.set_y(pdf.get_y()+3); pdf.set_font("Helvetica","",11); pdf.set_text_color(180,180,190)
    pdf.cell(0,7,"has completed all missions of the Metropolis AI Training Program",align="C",new_x="LMARGIN",new_y="NEXT")
    pdf.set_y(pdf.get_y()+8); pdf.set_font("Helvetica","B",11); pdf.set_text_color(0,212,255)
    pdf.cell(0,7,f"Rank: MASTER ARCHITECT | XP: {xp} | Badges: {len(badges)} | Session: {duration}",align="C",new_x="LMARGIN",new_y="NEXT")
    pdf.set_y(pdf.get_y()+4); pdf.set_font("Helvetica","",9); pdf.set_text_color(140,140,160)
    pdf.cell(0,6,f"Badges: {'  |  '.join(badges)}",align="C",new_x="LMARGIN",new_y="NEXT")
    ds = datetime.datetime.now().strftime("%B %d, %Y %H:%M")
    vh = hashlib.sha256(f"{name}{xp}{ds}".encode()).hexdigest()[:16].upper()
    pdf.set_y(pdf.get_y()+8); pdf.set_font("Helvetica","",10); pdf.set_text_color(100,100,120)
    pdf.cell(0,6,f"Issued: {ds}  |  Verify: MET-{vh}",align="C",new_x="LMARGIN",new_y="NEXT")
    pdf.set_y(ph-25); pdf.set_font("Helvetica","B",9); pdf.set_text_color(0,212,255)
    pdf.cell(0,6,"[ VERIFIED BY METROPOLIS CENTRAL AI AUTHORITY ]",align="C")
    return bytes(pdf.output())

def render_level5():
    mission_header(5, "LEVEL 5 — FINAL DEBRIEF", "Review performance and download your certificate.")
    all_done = all([st.session_state.level1_complete, st.session_state.level2_complete,
                    st.session_state.level3_complete, st.session_state.level4_complete])
    if not all_done:
        st.warning("Complete all campaign missions first.")
        for k,n in [("level1_complete","L1"),("level2_complete","L2"),("level3_complete","L3"),("level4_complete","L4")]:
            if not st.session_state[k]: st.markdown(f"- 🔒 {n}")
        return
    if not st.session_state.level5_complete:
        add_xp(300,"Master Architect"); st.session_state.level5_complete = True
        if "Master Architect" not in st.session_state.unlocked_badges: st.session_state.unlocked_badges.append("Master Architect")
    glass_card("""<div style="text-align:center;padding:1.5rem;">
        <span style="font-size:4rem;">🏆</span><br>
        <span style="font-family:Orbitron,monospace;font-size:1.8rem;color:#00ff88;text-shadow:0 0 30px rgba(0,255,136,0.4);">MASTER ARCHITECT</span><br><br>
        <span style="color:#aaa;font-family:'Share Tech Mono',monospace;">All missions complete. Metropolis is safe.</span></div>""", "success")
    neon_divider(); dur = get_session_duration(); rk, _ = get_rank()
    stat_grid([("XP",str(st.session_state.user_xp)),("Rank",rk.split(" ",1)[1]),
               ("Badges",str(len(st.session_state.unlocked_badges))),("Session",dur),
               ("Boss Tries",str(st.session_state.level3_attempts)),("Arcade Played",str(st.session_state.arcade_games_played))])
    neon_divider()
    pdf = generate_certificate_pdf(st.session_state.user_name, st.session_state.user_xp, st.session_state.unlocked_badges, dur)
    st.download_button("DOWNLOAD CERTIFICATE", data=pdf, file_name=f"metropolis_{st.session_state.user_name}.pdf",
                       mime="application/pdf", use_container_width=True)
    with st.expander("LinkedIn Share Text"):
        st.code(f"Completed Metropolis AI — cyberpunk data analytics platform!\n"
                f"Rank: {rk} | XP: {st.session_state.user_xp} | Badges: {', '.join(st.session_state.unlocked_badges)}\n"
                f"Skills: Pandas, Plotly, scikit-learn, EDA, ML\n#DataScience #Python #MachineLearning")


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🕹️ ARCADE HUB
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def render_arcade_hub():
    st.markdown("## 🕹️ ARCADE — SIDE MISSIONS")
    neon_divider()
    glass_card("""<p style="color:#bf00ff;margin:0;">
        <strong>THE UNDERGROUND.</strong> Four mini-games to sharpen your skills and earn bonus XP.
        No level requirements — play anytime. High scores tracked.</p>""", "purple")
    st.markdown("")

    games = [
        ("🛡️", "SQL INJECTION DEFENSE", "Identify & block SQL injection attacks", f"Best: {st.session_state.sql_best} pts", 11),
        ("⚡", "SPEED CODE CHALLENGE", "Write correct Pandas syntax under pressure", f"Best: {st.session_state.speed_best} pts", 12),
        ("📦", "DATA TYPE SORTER", "Classify values into correct data types", f"Best: {st.session_state.sorter_best} pts", 13),
        ("📊", "CORRELATION GUESSER", "Estimate correlation from scatter plots", f"Best: {st.session_state.corr_best} pts", 14),
    ]

    cols = st.columns(4)
    for col, (icon, title, desc, score, lvl) in zip(cols, games):
        with col:
            glass_card(f"""<div style="text-align:center;">
                <span class="game-icon" style="font-size:2.5rem;">{icon}</span><br>
                <span style="font-family:Orbitron,monospace;color:#bf00ff;font-size:0.75rem;letter-spacing:1px;">{title}</span><br>
                <span style="font-family:'Share Tech Mono',monospace;color:#777;font-size:0.7rem;">{desc}</span><br>
                <span style="font-family:Rajdhani,sans-serif;color:#ffee00;font-size:0.8rem;">{score}</span>
                </div>""", "purple")
            if st.button(f"PLAY", key=f"arcade_{lvl}", use_container_width=True):
                st.session_state.current_level = lvl
                st.session_state.arcade_games_played += 1
                st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛡️ GAME 1: SQL INJECTION DEFENSE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SQL_QUERIES = [
    {"query": "SELECT * FROM users WHERE id = 5", "safe": True, "explain": "Simple parameterized lookup — safe."},
    {"query": "SELECT * FROM users WHERE name = '' OR '1'='1'", "safe": False, "explain": "Classic tautology injection — always true condition."},
    {"query": "SELECT email FROM contacts WHERE dept = 'engineering'", "safe": True, "explain": "Normal filtered query — safe."},
    {"query": "DROP TABLE users; --", "safe": False, "explain": "Destructive DROP TABLE command with comment bypass."},
    {"query": "SELECT * FROM orders WHERE id = 1 UNION SELECT password FROM admin", "safe": False, "explain": "UNION-based injection stealing admin passwords."},
    {"query": "INSERT INTO logs (action) VALUES ('login')", "safe": True, "explain": "Standard insert — safe."},
    {"query": "SELECT * FROM products WHERE price < 100", "safe": True, "explain": "Normal filter — safe."},
    {"query": "'; DELETE FROM users WHERE '1'='1", "safe": False, "explain": "Injected DELETE wiping all user records."},
    {"query": "UPDATE inventory SET stock = stock - 1 WHERE id = 42", "safe": True, "explain": "Parameterized update — safe."},
    {"query": "SELECT * FROM users WHERE id = 1; EXEC xp_cmdshell('net user hacker pass /add')", "safe": False, "explain": "Command execution via xp_cmdshell — critical RCE."},
    {"query": "SELECT name FROM employees WHERE role = 'admin'", "safe": True, "explain": "Simple role filter — safe."},
    {"query": "' UNION SELECT credit_card, cvv FROM payments --", "safe": False, "explain": "UNION injection exfiltrating payment data."},
    {"query": "SELECT COUNT(*) FROM sessions WHERE active = true", "safe": True, "explain": "Aggregate count — safe."},
    {"query": "1; WAITFOR DELAY '0:0:10' --", "safe": False, "explain": "Time-based blind injection for detection evasion."},
    {"query": "SELECT * FROM products JOIN categories ON products.cat_id = categories.id", "safe": True, "explain": "Normal JOIN query — safe."},
]

def render_sql_defense():
    mission_header(11, "SQL INJECTION DEFENSE",
        "Incoming database queries. Identify which are <span style='color:#ff3344;'>SQL injection attacks</span> "
        "and which are <span style='color:#00ff88;'>safe</span>. 3 lives. How far can you go?")

    if st.button("← BACK TO ARCADE", key="sql_back"):
        st.session_state.sql_active = False; st.session_state.current_level = 10; st.rerun()

    # Reset / Start
    if not st.session_state.sql_active:
        st.markdown("")
        stat_grid([("High Score", str(st.session_state.sql_best)), ("Total XP from SQL", f"{st.session_state.sql_score}")])
        st.markdown("")
        if st.button("START NEW GAME", key="sql_start", use_container_width=True):
            st.session_state.sql_active = True
            st.session_state.sql_wave = 0
            st.session_state.sql_score = 0
            st.session_state.sql_lives = 3
            st.rerun()
        return

    wave = st.session_state.sql_wave
    lives = st.session_state.sql_lives
    score = st.session_state.sql_score

    # Game over?
    if lives <= 0 or wave >= len(SQL_QUERIES):
        st.session_state.sql_active = False
        if score > st.session_state.sql_best:
            st.session_state.sql_best = score
        result = "GAME OVER — Firewall breached!" if lives <= 0 else "ALL WAVES CLEARED!"
        xp_earned = score * 2
        add_xp(xp_earned, f"SQL Defense: {score} pts")
        glass_card(f"""<div style="text-align:center;">
            <span style="font-size:2rem;">{'💀' if lives<=0 else '🛡️'}</span><br>
            <span style="color:{'#ff3344' if lives<=0 else '#00ff88'};font-family:Orbitron,monospace;font-size:1.1rem;">{result}</span><br>
            <span style="color:#aaa;">Score: {score} | +{xp_earned} XP</span></div>""",
            "danger" if lives<=0 else "success")
        if st.button("PLAY AGAIN", key="sql_again"): st.rerun()
        return

    # Current wave
    q = SQL_QUERIES[wave]
    hearts = "❤️" * lives + "🖤" * (3 - lives)

    st.markdown(f"### Wave {wave+1}/{len(SQL_QUERIES)}  |  Score: {score}  |  {hearts}")
    neon_divider()

    st.markdown("**Incoming query:**")
    terminal_output(q["query"], "info")

    st.markdown("")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ SAFE — ALLOW", use_container_width=True, key=f"sql_safe_{wave}"):
            if q["safe"]:
                st.session_state.sql_score += 10
                st.session_state.sql_wave += 1
                st.success(f"Correct! {q['explain']}"); time.sleep(0.8); st.rerun()
            else:
                st.session_state.sql_lives -= 1
                st.session_state.sql_wave += 1
                st.error(f"WRONG! That was an attack. {q['explain']}"); time.sleep(0.8); st.rerun()
    with c2:
        if st.button("🛡️ ATTACK — BLOCK", use_container_width=True, key=f"sql_block_{wave}"):
            if not q["safe"]:
                st.session_state.sql_score += 15  # Bonus for catching attacks
                st.session_state.sql_wave += 1
                st.success(f"Attack blocked! {q['explain']}"); time.sleep(0.8); st.rerun()
            else:
                st.session_state.sql_lives -= 1
                st.session_state.sql_wave += 1
                st.error(f"WRONG! That was safe. {q['explain']}"); time.sleep(0.8); st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚡ GAME 2: SPEED CODE CHALLENGE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SPEED_QUESTIONS = [
    {"q": "Remove all rows where column 'age' is NaN", "answers": [
        "df.dropna(subset=['age'])", "df = df.dropna(subset=['age'])", "df[df['age'].notna()]", "df = df[df['age'].notna()]"]},
    {"q": "Get the mean of column 'salary' grouped by 'dept'", "answers": [
        "df.groupby('dept')['salary'].mean()", "df.groupby('dept').agg({'salary':'mean'})"]},
    {"q": "Rename column 'old_name' to 'new_name'", "answers": [
        "df.rename(columns={'old_name':'new_name'})", "df = df.rename(columns={'old_name':'new_name'})",
        "df.rename(columns={'old_name': 'new_name'})", "df = df.rename(columns={'old_name': 'new_name'})"]},
    {"q": "Sort dataframe by 'price' descending", "answers": [
        "df.sort_values('price',ascending=False)", "df = df.sort_values('price',ascending=False)",
        "df.sort_values('price', ascending=False)", "df = df.sort_values('price', ascending=False)",
        "df.sort_values(by='price',ascending=False)", "df.sort_values(by='price', ascending=False)"]},
    {"q": "Select rows where 'status' is 'active'", "answers": [
        "df[df['status']=='active']", "df[df['status'] == 'active']",
        "df.query(\"status == 'active'\")", "df.query('status == \"active\"')"]},
    {"q": "Create new column 'total' = 'price' * 'qty'", "answers": [
        "df['total']=df['price']*df['qty']", "df['total'] = df['price'] * df['qty']",
        "df['total'] = df['price']*df['qty']"]},
    {"q": "Count unique values in column 'category'", "answers": [
        "df['category'].nunique()", "df['category'].value_counts()", "len(df['category'].unique())"]},
    {"q": "Drop column 'temp_col' from dataframe", "answers": [
        "df.drop(columns=['temp_col'])", "df = df.drop(columns=['temp_col'])",
        "df.drop('temp_col',axis=1)", "df = df.drop('temp_col',axis=1)",
        "df.drop('temp_col', axis=1)", "df = df.drop('temp_col', axis=1)"]},
    {"q": "Fill NaN values in 'score' with the column median", "answers": [
        "df['score'].fillna(df['score'].median())", "df['score'] = df['score'].fillna(df['score'].median())"]},
    {"q": "Get first 10 rows of dataframe", "answers": ["df.head(10)", "df.iloc[:10]", "df[:10]"]},
]

def render_speed_code():
    mission_header(12, "SPEED CODE CHALLENGE",
        "Write the correct Pandas one-liner for each prompt. Spelling and syntax matter. 10 rounds.")

    if st.button("← BACK TO ARCADE", key="sp_back"):
        st.session_state.speed_active = False; st.session_state.current_level = 10; st.rerun()

    if not st.session_state.speed_active:
        stat_grid([("High Score", str(st.session_state.speed_best))])
        if st.button("START", key="sp_start", use_container_width=True):
            st.session_state.speed_active = True; st.session_state.speed_round = 0; st.session_state.speed_score = 0
            st.rerun()
        return

    rd = st.session_state.speed_round
    if rd >= len(SPEED_QUESTIONS):
        st.session_state.speed_active = False
        sc = st.session_state.speed_score
        if sc > st.session_state.speed_best: st.session_state.speed_best = sc
        xp = sc * 3; add_xp(xp, f"Speed Code: {sc}/{len(SPEED_QUESTIONS)}")
        glass_card(f"""<div style="text-align:center;">
            <span style="font-size:2rem;">⚡</span><br>
            <span style="color:#00ff88;font-family:Orbitron,monospace;">COMPLETE: {sc}/{len(SPEED_QUESTIONS)}</span><br>
            <span style="color:#aaa;">+{xp} XP</span></div>""", "success")
        if st.button("PLAY AGAIN", key="sp_again"): st.rerun()
        return

    q = SPEED_QUESTIONS[rd]
    st.markdown(f"### Round {rd+1}/{len(SPEED_QUESTIONS)}  |  Score: {st.session_state.speed_score}")
    neon_divider()
    st.markdown(f"**Task:** {q['q']}")
    ans = st.text_input("Your code:", key=f"sp_ans_{rd}", placeholder="df.something(...)")

    if st.button("SUBMIT", key=f"sp_sub_{rd}"):
        clean = ans.strip().rstrip(";")
        # Normalize spaces for comparison
        normalized = re.sub(r'\s+', '', clean)
        matched = any(re.sub(r'\s+', '', a) == normalized for a in q["answers"])
        if matched:
            st.session_state.speed_score += 1
            st.success("Correct!"); st.session_state.speed_round += 1; time.sleep(0.5); st.rerun()
        else:
            st.error(f"Not quite. Accepted: `{q['answers'][0]}`")
            st.session_state.speed_round += 1; time.sleep(1); st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 GAME 3: DATA TYPE SORTER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DTYPE_ITEMS = [
    ("42", "int"), ("3.14", "float"), ("'hello'", "str"), ("True", "bool"),
    ("None", "NoneType"), ("[1, 2, 3]", "list"), ("{'a': 1}", "dict"),
    ("(1, 2)", "tuple"), ("0.001", "float"), ("'2087-01-01'", "str"),
    ("-273", "int"), ("False", "bool"), ("{'x', 'y'}", "set"),
    ("''", "str"), ("0", "int"), ("1.0", "float"), ("NaN", "float"),
    ("[True, False]", "list"), ("()", "tuple"), ("{'key': [1,2]}", "dict"),
    ("b'bytes'", "bytes"), ("999_999", "int"), ("1+2j", "complex"),
    ("range(10)", "range"),
]

def render_sorter():
    mission_header(13, "DATA TYPE SORTER",
        "What Python data type is each value? Classify correctly. 12 rounds.")

    if st.button("← BACK TO ARCADE", key="sort_back"):
        st.session_state.sorter_active = False; st.session_state.current_level = 10; st.rerun()

    if not st.session_state.sorter_active:
        stat_grid([("High Score", str(st.session_state.sorter_best))])
        if st.button("START", key="sort_start", use_container_width=True):
            st.session_state.sorter_active = True; st.session_state.sorter_round = 0; st.session_state.sorter_score = 0
            st.rerun()
        return

    rd = st.session_state.sorter_round
    total_rounds = 12
    if rd >= total_rounds:
        st.session_state.sorter_active = False
        sc = st.session_state.sorter_score
        if sc > st.session_state.sorter_best: st.session_state.sorter_best = sc
        xp = sc * 4; add_xp(xp, f"Sorter: {sc}/{total_rounds}")
        glass_card(f"""<div style="text-align:center;">
            <span style="font-size:2rem;">📦</span><br>
            <span style="color:#00ff88;font-family:Orbitron,monospace;">SCORE: {sc}/{total_rounds}</span><br>
            <span style="color:#aaa;">+{xp} XP</span></div>""", "success")
        if st.button("PLAY AGAIN", key="sort_again"): st.rerun()
        return

    # Pick items deterministically based on round
    rng = np.random.RandomState(42 + rd)
    idx = rng.randint(0, len(DTYPE_ITEMS))
    value, correct_type = DTYPE_ITEMS[idx]

    # Build options (always include correct + 3 random)
    all_types = list(set(t for _, t in DTYPE_ITEMS))
    options = [correct_type]
    others = [t for t in all_types if t != correct_type]
    rng.shuffle(others)
    options.extend(others[:3])
    rng.shuffle(options)

    st.markdown(f"### Round {rd+1}/{total_rounds}  |  Score: {st.session_state.sorter_score}")
    neon_divider()

    glass_card(f"""<div style="text-align:center;">
        <span style="font-family:'Share Tech Mono',monospace;color:#ffee00;font-size:1.8rem;">{value}</span><br>
        <span style="color:#888;font-size:0.8rem;">What type is this value?</span></div>""")

    choice = st.radio("Select type:", options, index=None, key=f"sort_q_{rd}", label_visibility="collapsed")

    if st.button("SUBMIT", key=f"sort_sub_{rd}"):
        if choice == correct_type:
            st.session_state.sorter_score += 1
            st.success(f"Correct! `{value}` is `{correct_type}`")
        else:
            st.error(f"Wrong. `{value}` is `{correct_type}`, not `{choice}`")
        st.session_state.sorter_round += 1
        time.sleep(0.6); st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📊 GAME 4: CORRELATION GUESSER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def generate_corr_data(target_r):
    """Generate scatter data with approximately the target correlation."""
    n = 80
    rng = np.random.RandomState(int(abs(target_r * 10000)) + st.session_state.corr_round)
    x = rng.randn(n)
    noise = rng.randn(n)
    y = target_r * x + np.sqrt(1 - target_r**2) * noise
    return x, y

def render_correlation():
    mission_header(14, "CORRELATION GUESSER",
        "Look at the scatter plot and estimate the Pearson correlation coefficient (r). "
        "Get within ±0.15 to score. 8 rounds.")

    if st.button("← BACK TO ARCADE", key="corr_back"):
        st.session_state.corr_active = False; st.session_state.current_level = 10; st.rerun()

    if not st.session_state.corr_active:
        stat_grid([("High Score", str(st.session_state.corr_best))])
        if st.button("START", key="corr_start", use_container_width=True):
            st.session_state.corr_active = True; st.session_state.corr_round = 0; st.session_state.corr_score = 0
            st.session_state.corr_data = None; st.session_state.corr_true_r = None
            st.rerun()
        return

    rd = st.session_state.corr_round
    total = 8
    if rd >= total:
        st.session_state.corr_active = False
        sc = st.session_state.corr_score
        if sc > st.session_state.corr_best: st.session_state.corr_best = sc
        xp = sc * 5; add_xp(xp, f"Correlation: {sc}/{total}")
        glass_card(f"""<div style="text-align:center;">
            <span style="font-size:2rem;">📊</span><br>
            <span style="color:#00ff88;font-family:Orbitron,monospace;">SCORE: {sc}/{total}</span><br>
            <span style="color:#aaa;">+{xp} XP</span></div>""", "success")
        if st.button("PLAY AGAIN", key="corr_again"): st.rerun()
        return

    # Generate new data for this round
    if st.session_state.corr_data is None or st.session_state.get("_corr_rd_gen") != rd:
        possible_r = [-0.95, -0.7, -0.4, -0.1, 0.05, 0.3, 0.6, 0.85, 0.95, -0.55, 0.45, -0.8]
        rng = np.random.RandomState(rd * 7 + 3)
        true_r = possible_r[rng.randint(0, len(possible_r))]
        x, y = generate_corr_data(true_r)
        st.session_state.corr_data = (x.tolist(), y.tolist())
        st.session_state.corr_true_r = round(float(np.corrcoef(x, y)[0, 1]), 2)
        st.session_state._corr_rd_gen = rd

    x, y = st.session_state.corr_data
    true_r = st.session_state.corr_true_r

    st.markdown(f"### Round {rd+1}/{total}  |  Score: {st.session_state.corr_score}")
    neon_divider()

    fig = px.scatter(x=x, y=y, labels={"x": "Variable X", "y": "Variable Y"})
    fig.update_traces(marker=dict(color="#00d4ff", size=6, opacity=0.7))
    fig.update_layout(
        plot_bgcolor="rgba(8,8,18,0.9)", paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Share Tech Mono", color="#999"),
        xaxis=dict(gridcolor="rgba(0,255,136,0.04)", showticklabels=False, title="X"),
        yaxis=dict(gridcolor="rgba(0,255,136,0.04)", showticklabels=False, title="Y"),
        height=350, margin=dict(t=20, b=40))
    st.plotly_chart(fig, use_container_width=True)

    guess = st.slider("Your estimate of r:", -1.0, 1.0, 0.0, 0.05, key=f"corr_sl_{rd}")

    if st.button("SUBMIT", key=f"corr_sub_{rd}"):
        diff = abs(guess - true_r)
        if diff <= 0.15:
            st.session_state.corr_score += 1
            st.success(f"Close enough! True r = {true_r:.2f}, you guessed {guess:.2f} (diff: {diff:.2f})")
        else:
            st.error(f"Off target. True r = {true_r:.2f}, you guessed {guess:.2f} (diff: {diff:.2f})")
        st.session_state.corr_round += 1
        st.session_state.corr_data = None
        time.sleep(0.7); st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🖥️ SIDEBAR v3
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def render_sidebar():
    with st.sidebar:
        st.markdown("# ⟐ COMMAND CENTER")
        neon_divider()
        rk, _ = get_rank(); sync = get_sync_pct()
        st.markdown(f"**OPERATIVE:** `{st.session_state.user_name}`")
        st.markdown(f"**RANK:** {rk}")
        st.markdown(f"**XP:** `{st.session_state.user_xp}`")
        st.markdown(f"**SESSION:** `{get_session_duration()}`")
        neon_divider()
        st.markdown("### Campaign")
        st.progress(sync, text=f"{sync*100:.0f}%")
        for key, num, name, unlocked in [
            ("level1_complete",1,"Data Forensics",True),
            ("level2_complete",2,"Anomaly Hunt",st.session_state.level1_complete),
            ("level3_complete",3,"Rogue AI",st.session_state.level2_complete),
            ("level4_complete",4,"Intel Briefing",st.session_state.level3_complete),
            ("level5_complete",5,"Final Debrief",st.session_state.level4_complete)]:
            done = st.session_state.get(key, False)
            st.markdown(f"- {'✅' if done else ('🔓' if unlocked else '🔒')} LVL {num} · {name}")

        neon_divider()
        st.markdown("### Arcade High Scores")
        st.markdown(f"- 🛡️ SQL Defense: `{st.session_state.sql_best}`")
        st.markdown(f"- ⚡ Speed Code: `{st.session_state.speed_best}`")
        st.markdown(f"- 📦 Type Sorter: `{st.session_state.sorter_best}`")
        st.markdown(f"- 📊 Correlation: `{st.session_state.corr_best}`")

        if st.session_state.unlocked_badges:
            neon_divider()
            st.markdown("### Badges")
            for b in st.session_state.unlocked_badges: st.markdown(f"🏅 **{b}**")

        neon_divider()
        st.markdown("### Navigate")
        nav = ["Level 1: Data Forensics"]
        if st.session_state.level1_complete: nav.append("Level 2: Anomaly Hunt")
        if st.session_state.level2_complete: nav.append("Level 3: Rogue AI")
        if st.session_state.level3_complete: nav.append("Level 4: Intel Briefing")
        if st.session_state.level4_complete: nav.append("Level 5: Final Debrief")
        nav.append("🕹️ ARCADE")

        cur = st.session_state.current_level
        if cur >= 10:
            default_idx = len(nav) - 1
        elif cur >= 1:
            default_idx = max(0, min(cur - 1, len(nav) - 2))
        else:
            default_idx = 0

        choice = st.radio("Go to:", nav, index=default_idx, key="nav", label_visibility="collapsed")
        lmap = {"Level 1: Data Forensics":1,"Level 2: Anomaly Hunt":2,"Level 3: Rogue AI":3,
                "Level 4: Intel Briefing":4,"Level 5: Final Debrief":5,"🕹️ ARCADE":10}
        target = lmap.get(choice, cur)
        # Don't override if we're inside an arcade game (11-14) and nav shows ARCADE (10)
        if target == 10 and cur in (11, 12, 13, 14):
            pass
        elif target != cur:
            st.session_state.current_level = target
            st.rerun()

        neon_divider()
        if st.button("RESET ALL", key="rst"):
            for k in list(st.session_state.keys()): del st.session_state[k]
            st.rerun()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🚀 MAIN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    st.set_page_config(page_title="METROPOLIS AI", page_icon="⟐", layout="wide",
        initial_sidebar_state="expanded" if st.session_state.get("initialized") else "collapsed")
    st.markdown(CYBER_CSS, unsafe_allow_html=True)
    init_state()
    if not st.session_state.initialized: render_landing(); return
    render_sidebar()
    renderers = {
        1: render_level1, 2: render_level2, 3: render_level3, 4: render_level4, 5: render_level5,
        10: render_arcade_hub, 11: render_sql_defense, 12: render_speed_code,
        13: render_sorter, 14: render_correlation,
    }
    renderers.get(st.session_state.current_level, render_landing)()

if __name__ == "__main__":
    main()
