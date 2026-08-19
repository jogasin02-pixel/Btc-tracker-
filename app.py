import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Scalping Pro Dashboard", layout="wide")

st.title("⚡ Bitcoin Scalping Pro Dashboard")
st.markdown("---")

# 1. Single Clean Live Mini Chart / Price Widget
st.markdown("### 🔴 Live Market Price Card")
price_widget = """
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
  {
  "symbol": "BINANCE:BTCUSDT",
  "width": "100%",
  "height": "220",
  "locale": "en",
  "dateRange": "1D",
  "colorTheme": "dark",
  "isTransparent": true,
  "autosize": false,
  "largeChartUrl": ""
}
  </script>
</div>
"""
components.html(price_widget, height=230)

st.markdown("---")

# 2. 1-Minute Scalping Signal & Operator Meter
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

# 3. Live 1-Minute Chart
st.markdown("### 📉 1-Minute Live Chart")
tv_widget = """
<div class="tradingview-widget-container">
  <div id="tradingview_chart"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({
  "width": "100%",
  "height": 550,
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
components.html(tv_widget, height=550)
