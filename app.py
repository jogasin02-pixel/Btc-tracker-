import streamlit as st
import streamlit.components.v1 as components
import requests

st.set_page_config(page_title="BTC Operator Trap & Pro Chart", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

@st.cache_data(ttl=2)
def get_operator_trap():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
        res = requests.get(url, headers=headers, timeout=3).json()
        price = float(res['lastPrice'])
        high = float(res['highPrice'])
        low = float(res['lowPrice'])
        
        spread = high - low
        pos = (price - low) / spread if spread > 0 else 0.5
        
        if pos >= 0.82:
            status = "🚨 BEARISH TRAP (SHORT POSITION ZONE)"
            advice = "Operators are trapping buyers near resistance. Look to **SELL / SHORT**."
            box_type = "error"
        elif pos <= 0.18:
            status = "🚀 BULLISH TRAP (LONG POSITION ZONE)"
            advice = "Operators are trapping sellers near support. Look to **BUY / LONG**."
            box_type = "success"
        else:
            status = "⚖️ NEUTRAL ZONE (WAIT FOR EXTREMES)"
            advice = "Price is in the middle range. Wait for price to touch 24h High or Low."
            box_type = "warning"
            
        return price, high, low, status, advice, box_type
    except:
        try:
            url2 = "https://blockchain.info/ticker"
            res2 = requests.get(url2, timeout=3).json()
            price = float(res2['USD']['last'])
            return price, price * 1.01, price * 0.99, "⚖️ NEUTRAL ZONE", "Live connected via backup feed.", "warning"
        except:
            return 0.0, 0.0, 0.0, "🔄 Connecting...", "Please wait...", "warning"

price, high, low, status, advice, box_type = get_operator_trap()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Live Price", f"${price:,.2f}" if price > 0 else "Loading...")
with col2:
    st.metric("24h High", f"${high:,.2f}" if high > 0 else "Loading...")
with col3:
    st.metric("24h Low", f"${low:,.2f}" if low > 0 else "Loading...")

st.markdown("### Operator Status")
if box_type == "error":
    st.error(f"### {status}\n* **Strategy:** {advice}")
elif box_type == "success":
    st.success(f"### {status}\n* **Strategy:** {advice}")
else:
    st.warning(f"### {status}\n* **Strategy:** {advice}")

st.markdown("---")
st.subheader("📊 Advanced Technical Chart")

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

if st.checkbox("🔄 Auto Refresh (Every 1s)", value=True):
    import time
    time.sleep(5)
    st.rerun()
    
