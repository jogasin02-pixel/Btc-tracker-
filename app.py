import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd

# Page Configuration
st.set_page_config(page_title="BTC Pro Trap Dashboard", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

# 1. Fetch Trap Data (Real-time from Binance)
@st.cache_data(ttl=10)
def check_trap_status():
    try:
        # Get last 24h data
        url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=24"
        data = requests.get(url).json()
        df = pd.DataFrame(data, columns=['t', 'o', 'high', 'low', 'c', 'v', 'ct', 'q', 'n', 'tb', 'tq', 'i'])
        
        current_price = float(df['c'].iloc[-1])
        daily_high = float(df['high'].max())
        daily_low = float(df['low'].min())
        
        range_spread = daily_high - daily_low
        pos_in_range = (current_price - daily_low) / range_spread
        
        if pos_in_range > 0.85:
            return "⚠️ BEARISH TRAP ZONE (Operators Selling - Look for SELL/SHORT)", "red", current_price
        elif pos_in_range < 0.15:
            return "⚠️ BULLISH TRAP ZONE (Operators Buying - Look for BUY/LONG)", "green", current_price
        else:
            return "⚖️ NEUTRAL ZONE (Wait for Breakout)", "gray", current_price
    except:
        return "🔄 Loading Status...", "gray", 0

# Display Status
status, color, price = check_trap_status()
if color == "red":
    st.error(f"### {status} | Current Price: ${price:,.2f}")
elif color == "green":
    st.success(f"### {status} | Current Price: ${price:,.2f}")
else:
    st.warning(f"### {status} | Current Price: ${price:,.2f}")

# 2. TradingView Widget
tv_widget = """
<div class="tradingview-widget-container">
  <div id="tradingview_chart"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({
  "width": "100%", "height": 550, "symbol": "BINANCE:BTCUSDT",
  "interval": "15", "timezone": "Etc/UTC", "theme": "dark",
  "style": "1", "locale": "en", "toolbar_bg": "#f1f3f6",
  "enable_publishing": false, "allow_symbol_change": true,
  "container_id": "tradingview_chart"
});
  </script>
</div>
"""
components.html(tv_widget, height=550)

if st.button("🔄 Refresh Analysis"):
    st.rerun()
  
