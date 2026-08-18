import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Pro Dashboard", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

# Top Control / Info Section
col1, col2 = st.columns(2)
with col1:
    st.info("💡 **Tip:** Use the TradingView toolbar below to add RSI, MACD, Moving Averages and all technical indicators.")
with col2:
    st.warning("⚠️ **Operator Zone Guide:** Watch the upper and lower extremes of the daily range to identify smart money traps.")

# TradingView Advanced Chart Integration
st.subheader("📊 Live Advanced Technical Chart")

tv_widget = """
<div class="tradingview-widget-container">
  <div id="tradingview_chart"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({
  "width": "100%",
  "height": 650,
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

components.html(tv_widget, height=650)
