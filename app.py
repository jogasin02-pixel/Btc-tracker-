import streamlit as st
import streamlit.components.v1 as components
import requests

# Page Configuration
st.set_page_config(page_title="BTC Operator Trap & Pro Chart", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

# Fetch Live Price & Calculate Operator Trap Status
@st.cache_data(ttl=5)
def get_operator_trap():
    try:
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
        res = requests.get(url, timeout=3).json()
        price = float(res['lastPrice'])
        high = float(res['highPrice'])
        low = float(res['lowPrice'])
        
        spread = high - low
        pos = (price - low) / spread if spread > 0 else 0.5
        
        if pos >= 0.82:
            return price, high, low, "🚨 BEARISH TRAP (SHORT ZONE - Operators Trapping Buyers)", "error"
        elif pos <= 0.18:
            return price, high, low, "🚀 BULLISH TRAP (LONG ZONE - Operators Trapping Sellers)", "success"
        else:
            return price, high, low, "⚖️ NEUTRAL ZONE (WAIT FOR BREAKOUT)", "warning"
    except:
        return 0.0, 0.0, 0.0, "🔄 Loading Live Status...", "warning"

price, high, low, status_text, box_type = get_operator_trap()

# 1. Live Price & 24h High Section
col1, col2 = st.columns(2)
with col1:
    st.markdown("### Live Price")
    st.markdown(f"## **${price:,.2f}**")
with col2:
    st.markdown("### 24h High")
    st.markdown(f"## **${high:,.2f}**")

# 2. Operator Status Box
st.markdown("### Operator Status")
if box_type == "error":
    st.error(f"### {status_text}")
elif box_type == "success":
    st.success(f"### {status_text}")
else:
    st.warning(f"### {status_text}")

st.markdown("---")
st.markdown("### 📊 Live Interactive TradingView Chart")

# 3. Main Live TradingView Chart
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

# Auto-refresh to keep data live
if st.checkbox("🔄 Auto Refresh (Every 10s)", value=True):
    import time
    time.sleep(10)
    st.rerun()
    
