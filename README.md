# 🚀 TeamMasters AI Stock Sentiment Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Supabase](https://img.shields.io/badge/Supabase-Backend-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

**TeamMasters AI** is a full-stack AI-powered stock sentiment analysis dashboard that enables users to analyze financial news, evaluate market sentiment, and track stock price trends in real time.

This application integrates **machine learning-based sentiment analysis**, **real-time financial APIs**, and **interactive data visualization** into a modern, user-friendly dashboard.

The system supports **multi-user authentication**, **database persistence**, and **dynamic UI rendering**, making it a complete end-to-end software solution.

---

## ✨ Features

- 🔐 User Authentication (Signup, Login, Logout)
- 🔁 Password Reset via Email (Secure recovery flow)
- 👤 Editable User Profile (Username update functionality)
- 👥 Multi-user support with personalized dashboards
- 🧠 AI-based Sentiment Analysis using VADER
- 📰 Real-time Financial News Retrieval (NewsAPI)
- 📈 Stock Price Data Integration (yfinance)
- 📊 Interactive Data Visualization (Plotly)
- 🎯 Sentiment Score Gauge (Real-time sentiment indicator)
- 💾 Persistent Search History (Supabase Database)
- ✏️ Update/Delete Stored Records
- 🗂️ Full CRUD Database Operations
- 🎨 Modern Dashboard UI with responsive design (Streamlit)
- 🔄 Session State Management for seamless UX

---

## 🏗️ System Architecture

The application follows a modular architecture:

- **Frontend:** Streamlit UI
- **Backend:** Supabase (Authentication + Database)
- **Data Sources:**
  - NewsAPI (news articles)
  - yfinance (stock prices)
- **AI Processing:**
  - VADER Sentiment Analyzer
- **Visualization:**
  - Plotly charts and gauge indicators

---

## 🛠️ Tech Stack

| Technology | Purpose |
|----------|--------|
| Python | Core Programming |
| Streamlit | Frontend UI |
| Supabase | Authentication & Database |
| NewsAPI | Fetch Financial News |
| VADER | Sentiment Analysis |
| yfinance | Stock Data |
| Plotly | Data Visualization |

---


## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/AbishekPokhrel/TeamMasters-AI-Stock-Sentiment-Dashboard.git
cd TeamMasters-AI-Stock-Sentiment-Dashboard
