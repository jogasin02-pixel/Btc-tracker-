import streamlit as st
import streamlit.components.v1 as components
import requests

st.set_page_config(page_title="BTC Operator Trap & Pro Chart", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

# 1. Top Section: Only Live Price
st.markdown("### 🔴 Live Bitcoin Price")
price_widget = """
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
  {
  "symbol": "BINANCE:BTCUSDT",
  "width": "100%",
  "colorTheme": "dark",
  "isTransparent": true,
  "locale": "en"
}
  </script>
</div>
"""
components.html(price_widget, height=90)

st.markdown("---")

# 2. Detailed Analysis: High, Low, Trap Price & Status (Short/Long)
st.subheader("📊 Operator Trap & Market Status Analysis")

@st.cache_data(ttl=5)
def get_trap_details():
    try:
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
        res = requests.get(url, timeout=3).json()
        price = float(res['lastPrice'])
        high = float(res['highPrice'])
        low = float(res['lowPrice'])
        
        spread = high - low
        pos = (price - low) / spread if spread > 0 else 0.5
        
        if pos >= 0.82:
            status = "🚨 BEARISH TRAP (SHORT POSITION ZONE)"
            trap_price = high
            advice = "Operators are trapping buyers near resistance. Look to **SELL / SHORT**."
            box_type = "error"
        elif pos <= 0.18:
            status = "🚀 BULLISH TRAP (LONG POSITION ZONE)"
            trap_price = low
            advice = "Operators are trapping sellers near support. Look to **BUY / LONG**."
            box_type = "success"
        else:
            status = "⚖️ NEUTRAL ZONE (WAIT FOR EXTREMES)"
            trap_price = (high + low) / 2
            advice = "Price is in the middle range. Wait for price to touch 24h High or Low."
            box_type = "warning"
            
        return price, high, low, trap_price, status, advice, box_type
    except:
        return 0.0, 0.0, 0.0, 0.0, "🔄 Loading Market Data...", "Please wait...", "warning"

price, high, low, trap_price, status, advice, box_type = get_trap_details()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("24h High", f"${high:,.2f}" if high > 0 else "Loading...")
with col2:
    st.metric("24h Low", f"${low:,.2f}" if low > 0 else "Loading...")
with col3:
    st.metric("Operator Trap Level", f"${trap_price:,.2f}" if trap_price > 0 else "Loading...")

if box_type == "error":
    st.error(f"### {status}\n* **Strategy:** {advice}")
elif box_type == "success":
    st.success(f"### {status}\n* **Strategy:** {advice}")
else:
    st.warning(f"### {status}\n* **Strategy:** {advice}")

st.markdown("---")
st.subheader("📉 Full Live Interactive TradingView Chart")

# 3. Main Interactive Chart
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

if st.checkbox("🔄 Auto Refresh (Every 10s)", value=True):
    import time
    time.sleep(10)
    st.rerun()
    
