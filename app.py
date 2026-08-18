import streamlit as st
import streamlit.components.v1 as components
import requests

# Page Configuration
st.set_page_config(page_title="BTC Operator Trap & Pro Chart", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

# Robust Function to Fetch Live Data from Multiple Free APIs (No Connection Error)
@st.cache_data(ttl=5)
def get_live_market_data():
    # 1. Try Binance API first
    try:
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
        res = requests.get(url, timeout=3).json()
        price = float(res['lastPrice'])
        high = float(res['highPrice'])
        low = float(res['lowPrice'])
        return price, high, low
    except:
        pass

    # 2. Try CoinGecko API as backup
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_high=true&include_24hr_low=true"
        res = requests.get(url, timeout=3).json()
        price = float(res['bitcoin']['usd'])
        high = float(res['bitcoin']['usd_24h_high'])
        low = float(res['bitcoin']['usd_24h_low'])
        return price, high, low
    except:
        pass

    # 3. Try Coinbase API as final backup
    try:
        url = "https://api.exchange.coinbase.com/products/BTC-USD/stats"
        res = requests.get(url, timeout=3).json()
        price = float(res['last'])
        high = float(res['high'])
        low = float(res['low'])
        return price, high, low
    except:
        return 0.0, 0.0, 0.0

# Fetch Data
price, high, low = get_live_market_data()

if price > 0 and high > low:
    spread = high - low
    pos = (price - low) / spread if spread > 0 else 0.5

    # Operator Trap Calculation Logic
    if pos >= 0.82:
        status_text = "🚨 BEARISH TRAP (SHORT ZONE)"
        box_color = "error"
    elif pos <= 0.18:
        status_text = "🚀 BULLISH TRAP (LONG ZONE)"
        box_color = "success"
    else:
        status_text = "⚖️ NEUTRAL ZONE (WAIT FOR BREAKOUT)"
        box_color = "warning"

    # Displaying Metrics just like your old screenshot
    st.markdown(f"### Live Price")
    st.markdown(f"## **${price:,.2f}**")
    
    st.markdown(f"### 24h High")
    st.markdown(f"### **${high:,.2f}**")

    st.markdown(f"### Operator Status")
    if box_color == "error":
        st.error(f"### {status_text}")
    elif box_color == "success":
        st.success(f"### {status_text}")
    else:
        st.warning(f"### {status_text}")

else:
    st.error("🔄 Connecting to live feed... Please wait a second.")

st.markdown("---")
st.markdown("### 📊 Advanced Technical Chart (Add Indicators Here)")

# TradingView Live Interactive Chart
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

# Auto-refresh checkbox
if st.checkbox("🔄 Auto Refresh (Every 10s)", value=True):
    import time
    time.sleep(10)
    st.rerun()
    
