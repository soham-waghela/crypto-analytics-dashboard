# Real-Time Crypto Analytics Dashboard

An end-to-end cryptocurrency analytics platform built using Python, PostgreSQL, Streamlit, and CoinGecko API.

This project automatically fetches live cryptocurrency market data, stores historical snapshots in PostgreSQL, performs financial analytics, and visualizes insights through an interactive Streamlit dashboard.

---

# Project Architecture

CoinGecko API  
↓  
Python ETL Pipeline  
↓  
PostgreSQL Database  
↓  
Pandas Analytics Engine  
↓  
Streamlit Dashboard  
↓  
Interactive Financial Visualizations

---

# Features

- Live cryptocurrency market data ingestion
- Automated ETL pipeline using Task Scheduler
- Historical crypto price tracking
- PostgreSQL database integration
- Interactive Streamlit dashboard
- Cryptocurrency filtering system
- Market capitalization analysis
- Market share distribution
- Historical price trend analysis
- Normalized performance comparison
- Returns analysis
- Volatility analysis
- Correlation matrix analytics
- Auto-refreshing dashboard

---

# Technologies Used

## Programming & Analytics
- Python
- Pandas
- NumPy

## Database
- PostgreSQL
- SQLAlchemy
- psycopg2

## Dashboard & Visualization
- Streamlit
- Matplotlib

## APIs
- CoinGecko API

## Automation
- Windows Task Scheduler

---

# Financial Analytics Implemented

## Returns Calculation

The dashboard calculates percentage returns using:

Return = (Current Price - Previous Price) / Previous Price

---

## Volatility Analysis

Volatility is measured using the standard deviation of returns.

Higher volatility indicates higher risk.

---

## Correlation Analysis

The correlation matrix measures how cryptocurrencies move relative to each other.

- 1 → Perfect positive correlation
- 0 → No correlation
- -1 → Perfect negative correlation

---

# Database Schema

Table: `crypto_prices`

| Column | Description |
|---|---|
| id | Unique row identifier |
| coin_name | Cryptocurrency name |
| symbol | Coin ticker symbol |
| current_price | Current market price |
| market_cap | Cryptocurrency market capitalization |
| fetched_at | Timestamp of data collection |

---

# Automated Data Pipeline

The project uses Windows Task Scheduler to automatically execute the ETL pipeline every 5 minutes.

Pipeline Flow:

Task Scheduler  
↓  
Batch File  
↓  
Python Fetch Script  
↓  
CoinGecko API  
↓  
PostgreSQL Database  
↓  
Streamlit Dashboard

---

# Installation & Setup

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/crypto-analytics-dashboard.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL="postgresql://postgres:YOUR_PASSWORD@localhost:5432/crypto_dashboard"
```

---

## Run Data Ingestion Script

```bash
python scripts/fetch_crypto_data.py
```

---

## Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Project Structure

```text
crypto-analytics-dashboard/
│
├── dashboard/
│   └── app.py
│
├── scripts/
│   └── fetch_crypto_data.py
│
├── images/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── run_fetch.bat
```

---


# Key Skills Demonstrated

- API Integration
- ETL Pipeline Development
- PostgreSQL Database Design
- Data Engineering Concepts
- Financial Time-Series Analytics
- Interactive Dashboard Development
- Automation & Scheduling
- Quantitative Analysis
- Python Data Analytics

---

