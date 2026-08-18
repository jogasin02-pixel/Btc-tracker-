import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Operator Trap & Pro Chart", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

# Layout for Top Metrics using TradingView Live Widgets (Zero Connection Errors)
col1, col2 = st.columns(2)

with col1:
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

with col2:
    st.markdown("### 📊 Operator Trend & Signal Meter")

# Technical Analysis Meter (Shows Buy/Sell/Trap Signals Live)
ta_widget = """
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
  {
  "interval": "15m",
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
components.html(ta_widget, height=400)

st.markdown("---")
st.markdown("### 📉 Live Interactive TradingView Chart")

# Main Live TradingView Chart
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
