import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd

# Page Configuration
st.set_page_config(page_title="BTC Pro Live Operator Trap & Chart", layout="wide")

st.title("🚀 BTC Live Operator Trap & Pro Chart")
st.markdown("---")

# 1. Real-time Operator Trap & Position Calculator (Binance Live Data)
@st.cache_data(ttl=5)
def get_live_operator_status():
    try:
        url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=24"
        data = requests.get(url).json()
        df = pd.DataFrame(data, columns=['t', 'o', 'high', 'low', 'c', 'v', 'ct', 'q', 'n', 'tb', 'tq', 'i'])
        
        current_price = float(df['c'].iloc[-1])
        daily_high = float(df['high'].max())
        daily_low = float(df['low'].min())
        
        spread = daily_high - daily_low
        pos = (current_price - daily_low) / spread if spread > 0 else 0.5
        
        if pos > 0.80:
            return "🚨 BEARISH OPERATOR TRAP (SELL / SHORT ZONE)", "Operators are trapping buyers near 24h High. Look for a downward reversal.", "red", current_price, daily_high, daily_low
        elif pos < 0.20:
            return "🚀 BULLISH OPERATOR TRAP (BUY / LONG ZONE)", "Operators are trapping sellers near 24h Low. Look for an upward bounce.", "green", current_price, daily_high, daily_low
        else:
            return "⚖️ NEUTRAL MARKET ZONE (WAIT FOR BREAKOUT)", "Price is in the middle of the daily range. Wait to reach High/Low extremes.", "yellow", current_price, daily_high, daily_low
    except:
        return "🔄 Connecting to Live Feed...", "Fetching live data...", "gray", 0, 0, 0

title, desc, color, price, high, low = get_live_operator_status()

# Displaying Clear Action Boxes at the Top
if color == "red":
    st.error(f"### {title}\n* **Live Price:** ${price:,.2f} | **24h High (Resistance):** ${high:,.2f}\n* **Action Guide:** {desc}")
elif color == "green":
    st.success(f"### {title}\n* **Live Price:** ${price:,.2f} | **24h Low (Support):** ${low:,.2f}\n* **Action Guide:** {desc}")
else:
    st.warning(f"### {title}\n* **Live Price:** ${price:,.2f} | **Range:** ${low:,.2f} - ${high:,.2f}\n* **Action Guide:** {desc}")

st.markdown("---")
st.subheader("📊 Live TradingView Pro Chart (Real-time Feed)")

# 2. TradingView Live Interactive Chart (Same as TradingView website)
tv_widget = """
<div class="tradingview-widget-container">
  <div id="tradingview_chart"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({
  "width": "100%",
  "height": 600,
  "symbol": "BINANCE:BTCUSDT",
  "interval": "15",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "container_id": "tradingview_chart"
});
  </script>
</div>
"""

components.html(tv_widget, height=600)

# Refresh Button for Live Status Update
if st.button("🔄 Refresh Trap Status"):
    st.rerun()
    
