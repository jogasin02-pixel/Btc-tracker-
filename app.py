import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Pro Trap Dashboard", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

# Info Box
st.info("💡 **Live Analysis Tip:** Watch the Daily High and Low extremes on the chart below to identify Operator Bearish/Bullish Traps.")

# TradingView Widget with built-in Binance feed
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

components.html(tv_widget, height=650)
