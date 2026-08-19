import streamlit as st
import streamlit.components.v1 as components
import time

# Page Configuration
st.set_page_config(page_title="BTC Operator Trap & Scalping Pro", layout="wide")

st.title("⚡ Bitcoin Operator Trap & Scalping Dashboard")
st.markdown("---")

# 1. Live Price Ticker (Zero Delay - Matches Chart Price Instantly)
st.markdown("### 🔴 Live Market Price")
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

# 2. 1-Minute Scalping Signal Meter (Tells when to Buy / Long or Sell / Short)
st.markdown("### 🎯 1-Minute Scalping Signal & Operator Move Meter")
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

# 3. Main Live Interactive TradingView Chart (Set to 1-minute interval for small moves)
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
