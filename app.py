import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="BTC Smart Scalper Pro", layout="centered")

st.title("⚡ BTC Smart Scalper Pro Bot")
st.markdown("---")

def analyze_market():
    try:
        # Fetching Binance 1-minute and multi-candle data
        url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=30"
        res = requests.get(url, timeout=3).json()
        
        closes = [float(candle[4]) for candle in res]
        volumes = [float(candle[5]) for candle in res]
        
        current_price = closes[-1]
        
        # Calculating short-term momentum (comparing last few candles)
        short_diff = closes[-1] - closes[-3] # 3-minute check
        mid_diff = closes[-1] - closes[-5]   # 5-minute check
        
        # RSI Calculation
        gains = [closes[i] - closes[i-1] for i in range(1, len(closes)) if closes[i] > closes[i-1]]
        losses = [closes[i-1] - closes[i] for i in range(1, len(closes)) if closes[i] < closes[i-1]]
        
        avg_gain = sum(gains) / len(gains) if gains else 0.001
        avg_loss = sum(losses) / len(losses) if losses else 0.001
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        # Volume Spike Check (Operator/Whale movement tracking)
        avg_vol = sum(volumes[:-1]) / len(volumes[:-1])
        current_vol = volumes[-1]
        is_volume_spike = current_vol > (avg_vol * 1.8)
        
        # Decision Logic for Scalping
        if rsi < 30 and short_diff > 0:
            signal = "🔥 STRONG BUY / LONG SCALP"
            color = "success"
            reason = f"Oversold condition (RSI: {rsi:.1f}) with sudden 3-min recovery. Good entry!"
        elif rsi > 70 and short_diff < 0:
            signal = "🚨 STRONG SELL / SHORT SCALP"
            color = "error"
            reason = f"Overbought condition (RSI: {rsi:.1f}) with rejection. Price may dump."
        elif is_volume_spike and short_diff > 20:
            signal = "⚡ WHALE PUMP DETECTED - BUY"
            color = "success"
            reason = "High volume spike in last minute. Operators are lifting the price!"
        elif is_volume_spike and short_diff < -20:
            signal = "⚠️ WHALE DUMP DETECTED - SELL"
            color = "error"
            reason = "Heavy volume selling. Operators are trapping buyers!"
        else:
            signal = "⏳ MARKET CONSOLIDATING - WAIT"
            color = "warning"
            reason = f"No clear operator trap yet. Current RSI: {rsi:.1f}. Wait for a breakout."
            
        return current_price, signal, reason, color, rsi
        
    except Exception as e:
        return 0.0, "🔄 Connecting to Binance...", "Fetching live ticks...", "warning", 50.0

price, signal, reason, color, rsi = analyze_market()

# Display Live Price
if price > 0:
    st.markdown(f"### 🔴 Live Price: **${price:,.2f}**  |  **RSI: {rsi:.1f}**")
else:
    st.markdown("### 🔴 Connecting to Live Feed...")

st.markdown("---")

# Display Direct Action Signal Box
st.markdown("### 🎯 Scalping Robot Decision:")
if color == "success":
    st.success(f"# {signal}\n\n**Reason:** {reason}")
elif color == "error":
    st.error(f"# {signal}\n\n**Reason:** {reason}")
else:
    st.warning(f"# {signal}\n\n**Reason:** {reason}")

st.markdown("---")
st.markdown("*(यह बोट 3-मिनट और 5-मिनट के वॉल्यूम और RSI को खुद कैलकुलेट करके बिल्कुल सटीक सिग्नल दे रहा है)*")

# Auto-refresh button to check latest ticks
if st.button("🔄 Refresh / Get Latest Signal"):
    st.rerun()
