# 💰 Finance Tracker

A full-stack financial dashboard with stock portfolio tracking and financial news integration.

## 🌍 Live Demo
[Finance Tracker](https://finance-tracker-lac-omega.vercel.app/)

## ✨ Features
- **Personal Finance** — Track income and expenses with categories
- **Stock Portfolio** — Real-time stock prices and profit/loss calculation
- **Financial News** — Latest news filtered by stock symbol
- **Dashboard UI** — Professional dark theme financial dashboard

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Database | SQLite |
| Stock Data | yfinance (no API key required) |
| News Data | NewsAPI |
| Deployment | Vercel (frontend), Render (backend) |

## 🚀 Running Locally

### Prerequisites
- Python 3.10+
- Git

### Setup
1. Clone the repository:
\```
git clone https://github.com/YourUsername/finance-tracker.git
\```

2. Create virtual environment:
\```
python -m venv venv
venv\Scripts\activate
\```

3. Install dependencies:
\```
pip install -r requirements.txt
\```

4. Create `.env` file (see `.env.example`):
\```
NEWS_API_KEY=your_key
\```

5. Run the server:
\```
python backend/app.py
\```

6. Open `frontend/index.html` with Live Server

## 📡 API Endpoints

### Finance
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/transactions` | Get all transactions |
| POST | `/transactions` | Add transaction |
| DELETE | `/transactions/<id>` | Delete transaction |
| GET | `/transactions/summary` | Get balance summary |

### Stocks
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/portfolio` | Get portfolio with live prices |
| POST | `/portfolio` | Add stock |
| DELETE | `/portfolio/<id>` | Delete stock |
| GET | `/portfolio/price` | Get single stock price |

### News
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/news` | Get financial news |
| GET | `/news/stock` | Get stock specific news |

## 👨‍💻 Author
Ritesh Nallapareddy
