# ⟐ METROPOLIS AI

### A Cyberpunk Data Analytics Learning Platform

[![Python](https://img.shields.io/badge/Python-3.9+-00ff88?style=flat-square&logo=python&logoColor=00ff88)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-00d4ff?style=flat-square&logo=streamlit&logoColor=00d4ff)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-bf00ff?style=flat-square&logo=scikitlearn&logoColor=bf00ff)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-ffee00?style=flat-square)](LICENSE)

> A gamified Streamlit app that teaches **Data Cleaning**, **EDA**, **Machine Learning**, and **Data Science theory** through a cyberpunk-themed 5-mission campaign and 4 arcade mini-games — with real Python code execution, boss fights, high scores, and a downloadable PDF certificate.

---

## What Is This?

Metropolis AI drops you into a failing cyberpunk city as a data operative. Instead of reading tutorials, you write real Pandas commands to clean corrupted datasets, explore interactive Plotly charts to find anomalies, tune a Random Forest to defeat a rogue AI, and prove your theory knowledge under pressure.

Every line of code you type actually executes in a sandboxed environment. Every chart is interactive. Every game tracks your score.

---

## The Campaign (5 Levels)

| Level | Mission | What You Learn | Core Tech |
|-------|---------|----------------|-----------|
| **01** | Data Forensics | Cleaning: duplicates, missing values, outliers | Pandas |
| **02** | Anomaly Hunt | Exploratory data analysis with interactive scatter plots | Plotly |
| **03** | Rogue AI Boss Fight | Train a classifier, tune hyperparameters, beat the AI | scikit-learn |
| **04** | Intel Briefing | Data science theory and best practices | Quiz |
| **05** | Final Debrief | Performance stats + downloadable PDF certificate | fpdf2 |

## The Arcade (4 Mini-Games)

| Game | What It Tests | How It Works |
|------|--------------|-------------|
| **🛡️ SQL Injection Defense** | Security awareness | 15 waves of queries — identify attacks vs safe SQL. 3 lives. |
| **⚡ Speed Code Challenge** | Pandas fluency | 10 prompts, type the correct one-liner. Syntax matters. |
| **📦 Data Type Sorter** | Python fundamentals | Classify values (`3.14`, `None`, `{'a':1}`) into correct types. |
| **📊 Correlation Guesser** | Statistical intuition | Estimate Pearson r from scatter plots. ±0.15 tolerance. |

All arcade games are available anytime — no level gates. High scores tracked in the sidebar.

---

## Features

- **Real code execution** — Pandas commands run in a sandboxed environment against actual DataFrames
- **Live data health monitor** — Watch duplicates, nulls, and outliers change as you clean
- **Interactive Plotly charts** — Hover, zoom, and explore to find hidden anomalies
- **ML Boss Fight** — Tune Random Forest hyperparameters, see radar chart + confusion matrix + feature importance
- **Attempt history tracking** — F1-score graph across boss fight attempts
- **Progressive hints** — Get more specific help the more you struggle
- **XP, ranks, badges, inventory** — Full RPG progression from Initiate to Master Architect
- **4 arcade mini-games** — SQL defense, speed coding, type sorting, correlation guessing
- **High score tracking** — Per-game best scores displayed in the sidebar
- **Session timer + mission log** — Timestamped record of everything you do
- **PDF certificate** — Styled landscape certificate with verification hash
- **LinkedIn share block** — Copy-paste ready stats for posting
- **Cyberpunk glassmorphism UI** — Orbitron font, neon accents, scanline overlays, animated gradients
- **Reset button** — Start fresh anytime

---

## Quick Start

```bash
# Clone
git clone https://github.com/lokesh-kaluvala/metrpolis-ai-game.git
cd metrpolis-ai-game

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run metropolis_ai.py
```

Opens at `http://localhost:8501`.

**Requirements:** Python 3.9+

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| App Framework | Streamlit |
| Data Manipulation | Pandas, NumPy |
| Visualization | Plotly (scatter, radar, heatmap, bar) |
| Machine Learning | scikit-learn (Random Forest, StandardScaler, metrics) |
| PDF Generation | fpdf2 |
| Styling | Custom CSS (Glassmorphism, Orbitron, Share Tech Mono) |

---

## Project Structure

```
metrpolis-ai-game/
├── metropolis_ai.py      # Complete application (single file)
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── LICENSE               # MIT License
└── .gitignore
```

---

## Deploy to Streamlit Cloud

1. Fork or push this repo to your GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo
4. Set main file to `metropolis_ai.py`
5. Deploy — no config needed

---

## Skills Demonstrated

- **Python** — State management, sandboxed code execution, data generation
- **Pandas** — DataFrame cleaning, filtering, groupby, aggregation
- **Data Visualization** — Plotly scatter plots, radar charts, confusion matrices, feature importance, correlation plots
- **Machine Learning** — Random Forest, hyperparameter tuning, train/test splitting, stratification, evaluation metrics (Accuracy, F1, Precision, Recall)
- **SQL** — Injection pattern recognition (UNION, tautology, command execution, time-based blind)
- **Statistics** — Correlation estimation, data type classification
- **UI/UX** — Custom CSS theming, glassmorphism, responsive layout, gamification
- **PDF Generation** — Programmatic certificate creation
- **Security** — Input sanitization, sandboxed execution environment

---

## License

MIT

---

Built with Streamlit, scikit-learn, and a lot of neon green.
