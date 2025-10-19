# Volatility Analysis: ATR vs. Moving Average

This Python script visualizes how market volatility changes over time using the **Average True Range (ATR)** compared with its **moving average**.

---

## 📊 What It Does
- Downloads historical data from Yahoo Finance using `yfinance`
- Calculates 14-day ATR and its 50-day moving average
- Highlights periods of high and low volatility
- Plots both price and volatility trends with Matplotlib

---

## 🧠 Why It Matters
Financial analysts and quants use volatility metrics to:
- Identify calm vs. turbulent market phases
- Anticipate breakouts and risk periods
- Improve portfolio risk management

---

## 🚀 How to Run
```bash
pip install yfinance pandas matplotlib
python volatility_atr_ma.py
