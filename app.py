import streamlit as st
import requests
import time

# Page Configuration
st.set_page_config(page_title="BTC Auto Scalp Signal", layout="centered")

st.title("⚡ BTC Auto Scalp Signal & Trap Bot")
st.markdown("---")

# Function to analyze market and give direct Buy/Sell signal
def get_auto_signal():
    try:
        # Fetching Binance 1-minute Kline / Candlestick data
        url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=15"
        res = requests.get(url, timeout=3).json()
        
        closes = [float(candle[4]) for candle in res]
        current_price = closes[-1]
        prev_price = closes[-2]
        
        # Simple Momentum & Scalp Logic
        diff = current_price - prev_price
        
        # Calculating a basic momentum from last candles
        gains = [closes[i] - closes[i-1] for i in range(1, len(closes)) if closes[i] > closes[i-1]]
        losses = [closes[i-1] - closes[i] for i in range(1, len(closes)) if closes[i] < closes[i-1]]
        
        avg_gain = sum(gains) / len(gains) if gains else 0.001
        avg_loss = sum(losses) / len(losses) if losses else 0.001
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        # Decision Making
        if rsi >= 75 or diff < -30:
            signal = "🚨 SELL / SHORT NOW!"
            box_type = "error"
            reason = f"Market is overbought (RSI: {rsi:.1f}). Operators might dump. Quick short move expected."
        elif rsi <= 25 or diff > 30:
            signal = "🔥 BUY / LONG NOW!"
            box_type = "success"
            reason = f"Market is oversold / pumping (RSI: {rsi:.1f}). Operators are lifting the price. Good for a quick long scalp."
        else:
            signal = "⏳ WAIT / ACCUMULATION ZONE"
            box_type = "warning"
            reason = f"No clear small move yet (RSI: {rsi:.1f}). Wait for a sudden spike or drop."
            
        return current_price, signal, reason, box_type
    except Exception as e:
        return 0.0, "🔄 Connecting...", "Fetching live ticks...", "warning"

price, signal, reason, box_type = get_auto_signal()

# Display Live Price
st.markdown(f"### 🔴 Live Price: **${price:,.2f}**" if price > 0 else "### 🔴 Connecting...")
st.markdown("---")

# Display Direct Action Signal
st.markdown("### 🎯 Direct Robot Command:")
if box_type == "error":
    st.error(f"# {signal}\n\n**Reason:** {reason}")
elif box_type == "success":
    st.success(f"# {signal}\n\n**Reason:** {reason}")
else:
    st.warning(f"# {signal}\n\n**Reason:** {reason}")

st.markdown("---")
st.markdown("*(यह बोट हर 3 सेकंड में अपने आप मार्केट को पढ़कर नया सिग्नल देगा)*")

# Auto Refresh every 3 seconds to keep checking small moves
time.sleep(3)
st.rerun()
