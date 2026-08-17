import streamlit as st
import yfinance as yf
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Pro Dashboard", layout="wide")

st.title("🚀 Bitcoin Advanced Dashboard")
st.markdown("---")

# 1. Fetching Data using same source logic
@st.cache_data(ttl=2)
def get_btc_data():
    try:
        ticker = yf.Ticker("BTC-USD")
        data = ticker.history(period="1d", interval="1m")
        if not data.empty:
            price = float(data['Close'].iloc[-1])
            high = float(data['High'].max())
            low = float(data['Low'].min())
            return price, high, low
    except: return None, None, None
    return None, None, None

price, high, low = get_btc_data()

if price:
    col1, col2, col3 = st.columns(3)
    col1.metric("Live Price (Exchange Feed)", f"${price:,.2f}")
    col2.metric("24h High", f"${high:,.2f}")
    
    # Status
    range_spread = high - low
    pos = (price - low) / range_spread if range_spread > 0 else 0.5
    status = "⚠️ BEARISH TRAP" if pos > 0.85 else ("⚠️ BULLISH TRAP" if pos < 0.15 else "⚖️ NEUTRAL")
    col3.metric("Operator Status", status)

# 2. TradingView Chart
st.subheader("📊 Live Technical Chart")
tv_widget = """
<div class="tradingview-widget-container">
  <div id="tradingview_chart"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({
  "width": "100%",
  "height": 500,
  "symbol": "BTCUSD",
  "interval": "15",
  "timezone": "Etc/UTC",
  "theme": "light",
  "style": "1",
  "locale": "en",
  "container_id": "tradingview_chart"
});
  </script>
</div>
"""
components.html(tv_widget, height=500)
