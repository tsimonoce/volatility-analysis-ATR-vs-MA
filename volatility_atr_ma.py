

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# --- 1️⃣ Download price data ---
symbol = "AAPL"  # you can change this to any ticker (e.g. 'TSLA', 'BTC-USD')
data = yf.download(symbol, start="2023-01-01")

# --- 2️⃣ Calculate ATR (Average True Range) ---
high = data['High']
low = data['Low']
close = data['Close']

data['TR'] = high.combine(low, lambda h, l: h - l)
data['TR1'] = abs(high - close.shift(1))
data['TR2'] = abs(low - close.shift(1))
data['TrueRange'] = data[['TR', 'TR1', 'TR2']].max(axis=1)
data['ATR_14'] = data['TrueRange'].rolling(14).mean()

# --- 3️⃣ Calculate Moving Average of ATR (volatility trendline) ---
data['ATR_MA_50'] = data['ATR_14'].rolling(50).mean()

# --- 4️⃣ Plot ---
plt.figure(figsize=(12,8))

# Price chart
plt.subplot(2,1,1)
plt.plot(data['Close'], label=f'{symbol} Price', color='blue')
plt.title(f"{symbol} Price and Volatility (ATR vs. Moving Average)")
plt.legend()
plt.grid(True, alpha=0.3)

# Volatility chart
plt.subplot(2,1,2)
plt.plot(data['ATR_14'], label='ATR (14-day)', color='orange')
plt.plot(data['ATR_MA_50'], label='ATR 50-day MA', color='red', linestyle='--')

# Highlight when volatility is above or below its moving average
plt.fill_between(data.index, data['ATR_14'], data['ATR_MA_50'],
                 where=(data['ATR_14'] > data['ATR_MA_50']),
                 color='green', alpha=0.2, label='High volatility')
plt.fill_between(data.index, data['ATR_14'], data['ATR_MA_50'],
                 where=(data['ATR_14'] < data['ATR_MA_50']),
                 color='gray', alpha=0.2, label='Low volatility')

plt.legend()
plt.xlabel("Date")
plt.ylabel("Volatility (ATR)")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
