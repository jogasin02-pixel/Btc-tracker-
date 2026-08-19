import streamlit as st
import streamlit.components.v1 as components
import requests
import time

# Page Configuration
st.set_page_config(page_title="BTC Operator Trap & Scalping Pro", layout="wide")

st.title("⚡ Bitcoin Operator Trap & Scalping Dashboard")
st.markdown("---")

# Python API to calculate Operator Traps & Scalping Zones in real-time
@st.cache_data(ttl=3)
def get_operator_scalp_data():
    try:
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
        res = requests.get(url, timeout=3).json()
        price = float(res['lastPrice'])
        high = float(res['highPrice'])
        low = float(res['lowPrice'])
        
        spread = high - low
        pos = (price - low) / spread if spread > 0 else 0.5
        
        if pos >= 0.80:
            status = "🚨 BEARISH TRAP (OPERATOR DUMP ZONE)"
            advice = "Big operators are trapping buyers near resistance for a small scalp reversal. Look to **SELL / SHORT**."
            box_type = "error"
        elif pos <= 0.20:
            status = "🚀 BULLISH TRAP (OPERATOR PUMP ZONE)"
            advice = "Big operators are trapping sellers near support for a quick upward bounce. Look to **BUY / LONG**."
            box_type = "success"
        else:
            status = "⚖️ SCALPING ACCUMULATION ZONE"
            advice = "Price is moving inside the range. Catch short scalps on minor support/resistance touches."
            box_type = "warning"
            
        return price, high, low, status, advice, box_type
    except:
        return 0.0, 0.0, 0.0, "🔄 Connecting to Feed...", "Please wait...", "warning"

price, high, low, status, advice, box_type = get_operator_scalp_data()

# Metrics Display
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Live Price", f"${price:,.2f}" if price > 0 else "Loading...")
with col2:
    st.metric("24h High", f"${high:,.2f}" if high > 0 else "Loading...")
with col3:
    st.metric("24h Low", f"${low:,.2f}" if low > 0 else "Loading...")

# Operator & Scalp Action Box
st.markdown("### 🎯 Operator & Scalp Status")
if box_type == "error":
    st.error(f"### {status}\n* **Action Strategy:** {advice}")
elif box_type == "success":
    st.success(f"### {status}\n* **Action Strategy:** {advice}")
else:
    st.warning(f"### {status}\n* **Action Strategy:** {advice}")

st.markdown("---")

# Scalping Technical Analysis Meter (1-minute timeframe for small moves)
st.markdown("### ⚡ 1-Minute Scalping Signal Meter")
ta_widget = """
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
  {
  "interval": "1m",
  "width": "100%",
  "isTransparent": true,
  "colorTheme": "dark",
  "showSymbolLogo": true,
  "locale": "en",
  "symbol": "BINANCE:BTCUSDT"
}
  </script>
</div>
"""
components.html(ta_widget, height=380)

st.markdown("---")
st.markdown("### 📉 1-Minute Live Scalping & Trap Chart")

# Main Live Interactive TradingView Chart (Set to 1-minute for tiny moves)
tv_widget = """
<div class="tradingview-widget-container">
  <div id="tradingview_chart"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({
  "width": "100%",
  "height": 600,
  "symbol": "BINANCE:BTCUSDT",
  "interval": "1",
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

# Auto Refresh every 5 seconds for real-time scalping
if st.checkbox("🔄 Auto Refresh (Every 5s)", value=True):
    time.sleep(5)
    st.rerun()
    
