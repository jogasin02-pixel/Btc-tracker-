import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Live Operator Trap & Chart", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

# 1. TradingView Live Ticker Tape (Exact Same Real-time Price as Chart - Zero Delay)
st.markdown("### Live Market Price (Real-Time)")
ticker_widget = """
<!-- TradingView Widget BEGIN -->
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
<!-- TradingView Widget END -->
"""
components.html(ticker_widget, height=90)

st.markdown("---")
st.markdown("### 📊 Live Interactive TradingView Chart")

# 2. Main Live TradingView Chart
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
