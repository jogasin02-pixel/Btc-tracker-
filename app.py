import streamlit as st
import yfinance as yf
import time
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Pro Dashboard", layout="wide")

st.title("🚀 Bitcoin Advanced Dashboard & Live Chart")
st.markdown("---")

# 1. Live Price & Trap Logic (Same as before)
@st.cache_data(ttl=5)
def get_fast_btc_data():
    try:
        btc = yf.Ticker("BTC-USD")
        df = btc.history(period="1d", interval="1m")
        if not df.empty:
            price = float(df['Close'].iloc[-1])
            high = float(df['High'].max())
            low = float(df['Low'].min())
            return price, high, low
    except: return None, None, None
    return None, None, None

price, high, low = get_fast_btc_data()

if price:
    range_spread = high - low
    pos = (price - low) / range_spread if range_spread > 0 else 0.01
    status = "⚠️ BEARISH TRAP" if pos > 0.85 else ("⚠️ BULLISH TRAP" if pos < 0.15 else "⚖️ NEUTRAL")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Live Price", f"${price:,.2f}")
    col2.metric("24h High", f"${high:,.2f}")
    col3.metric("Operator Status", status)

# 2. TradingView Advanced Chart Integration
st.subheader("📊 Advanced Technical Chart (Add Indicators Here)")

# TradingView Widget HTML Code
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
  "theme": "light",
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

if st.checkbox("🔄 Auto Refresh Dashboard"):
    time.sleep(3)
    st.rerun()
  
