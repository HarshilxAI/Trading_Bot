# 🚀 Binance Futures Testnet Trading Bot

A Python-based Command Line Interface (CLI) application that places **Market** and **Limit** orders on the **Binance USDT-M Futures Testnet**.

This project was developed as part of a Python Developer Internship Assignment. It demonstrates API integration, modular software design, input validation, logging, and exception handling.

---

### 📌 Features

✅ Place **Market Orders**

✅ Place **Limit Orders**

✅ Supports both **BUY** and **SELL**

✅ Command Line Interface (CLI)

✅ Input Validation

✅ API Request & Response Logging

✅ Exception Handling

✅ Modular Code Structure

---

### 📂 Project Structure

```text
Trading_Bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py            
│   ├── orders.py            
│   ├── validators.py        
│   └── logging_config.py    
│
├── logs/
│   └── trading.log
│
├── cli.py                   
├── .env                     
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

---

### 🛠 Tech Stack

- Python 3.x
- python-binance
- python-dotenv
- argparse
- logging

---

### ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Trading_Bot.git
```

```bash
cd Trading_Bot
```

### 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔑 Configure API Keys

Create a file named

```text
.env
```

Add your Binance Futures Testnet credentials.

```env
API_KEY=YOUR_API_KEY
SECRET_KEY=YOUR_SECRET_KEY
```

---

### ▶️ Running the Application

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000
```

---

### 📝 Example Output

```
========== ORDER REQUEST ==========
Symbol      : BTCUSDT
Side        : BUY
Type        : MARKET
Quantity    : 0.001

========== ORDER RESPONSE ==========
Order ID      : 123456789
Status        : FILLED
Executed Qty  : 0.001
Average Price : 118500.25

✅ Order Placed Successfully
```

---

### 📄 Logging

Every API request and response is automatically stored inside

```text
logs/trading.log
```

Example

```
2026-07-07 11:40:01 | INFO | Creating Binance Client
2026-07-07 11:40:03 | INFO | Sending MARKET Order
2026-07-07 11:40:05 | INFO | Order Executed Successfully
```

---

### ✅ Validation

The application validates user inputs before sending requests to Binance.

Validation includes:

- Trading Symbol
- Order Side (BUY / SELL)
- Order Type (MARKET / LIMIT)
- Quantity
- Price (Required for LIMIT Orders)

---

### ⚠️ Error Handling

The application gracefully handles:

- Invalid Inputs
- Invalid API Credentials
- Binance API Errors
- Network Failures
- Unexpected Exceptions

---

### 📋 Requirements

Install dependencies using

```bash
pip install -r requirements.txt
```

Main packages used

- python-binance
- python-dotenv

---

### 📷 Sample Workflow

```text
User

↓

CLI

↓

Validate Input

↓

Create Binance Client

↓

Place Order

↓

Receive Response

↓

Display Result

↓

Save Logs
```

---

### 🔒 Security

- API Keys are stored inside `.env`
- `.env` is ignored using `.gitignore`
- No sensitive information is stored in the repository

---

### 🚧 Future Improvements

- Stop-Limit Orders
- OCO Orders
- Interactive CLI Menu
- Dashboard UI
- Trade History
- Order Cancellation
- Portfolio Monitoring

---

### 📜 License

This project was created for educational purposes and an internship assessment.
