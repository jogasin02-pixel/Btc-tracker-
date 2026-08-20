import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Pro Scalper Hub", layout="wide")

st.title("⚡ BTC Pro Scalper Hub (Multi-Timeframe & Indicators)")
st.markdown("---")

# 1. Live Advanced Multi-Timeframe Chart with All Indicators & Tools
st.markdown("### 📊 Advanced Live Chart (1m, 3m, 5m, 15m & All Indicators)")
st.markdown("*(ਇਸ ਚਾਰਟ ਵਿੱਚ ਤੁਸੀਂ ਕੋਈ ਵੀ ਇੰਡੀਕੇਟਰ ਲਗਾ ਸਕਦੇ ਹੋ ਅਤੇ 1m, 3m, 5m, 15m ਮਿੰਟ ਦੀਆਂ ਕੈਂਡਲਜ਼ ਨੂੰ ਖੁਦ ਰੀਡ ਕਰ ਸਕਦੇ ਹੋ)*")

tv_widget = """
<div class="tradingview-widget-container">
  <div id="tradingview_advanced_chart"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({
  "width": "100%",
  "height": 620,
  "symbol": "BINANCE:BTCUSDT",
  "interval": "3",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "allow_symbol_change": true,
  "studies": [
    "RSI@tv-basicstudies",
    "MACD@tv-basicstudies",
    "Volume@tv-basicstudies"
  ],
  "container_id": "tradingview_advanced_chart"
});
  </script>
</div>
"""
components.html(tv_widget, height=650)
