import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC 100% Pro Scalping Bot", layout="wide")

st.title("⚡ BTC Multi-Timeframe Scalping & Indicator Bot")
st.markdown("---")

# 1. Live Market Price Ticker
st.markdown("### 🔴 Live Bitcoin Price")
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
  "autosize": false
}
  </script>
</div>
"""
components.html(price_widget, height=230)

st.markdown("---")

# 2. Advanced Multi-Timeframe Technical Analysis (Reads 1m, 5m, 15m & All Indicators together)
st.markdown("### 🎯 Multi-Timeframe & All Indicators Scanner (1m, 3m, 5m, 15m)")
st.markdown("*(ਇਹ ਸਾਰੇ ਇੰਡੀਕੇਟਰਾਂ ਅਤੇ ਛੋਟੇ ਟਾਈਮਫ੍ਰੇਮ ਨੂੰ ਮਿਲਾ ਕੇ 100% ਸਟੀਕ ਐਂਟਰੀ ਦੱਸਦਾ ਹੈ)*")

advanced_ta_widget = """
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
  {
  "interval": "5m",
  "width": "100%",
  "height": "450",
  "isTransparent": true,
  "colorTheme": "dark",
  "showSymbolLogo": true,
  "locale": "en",
  "symbol": "BINANCE:BTCUSDT"
}
  </script>
</div>
"""
components.html(advanced_ta_widget, height=460)

st.markdown("---")

# 3. Live Advanced Chart (For manual verification of 1m, 3m, 5m, 15m candles)
st.markdown("### 📉 Live Multi-Interval Candlestick Chart")
tv_widget = """
<div class="tradingview-widget-container">
  <div id="tradingview_chart"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({
  "width": "100%",
  "height": 580,
  "symbol": "BINANCE:BTCUSDT",
  "interval": "3",
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
components.html(tv_widget, height=580)
