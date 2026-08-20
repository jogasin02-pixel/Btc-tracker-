import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Pro Scalper Hub", layout="wide")

st.title("⚡ BTC Pro Scalper Hub (10-Min & All Indicators)")
st.markdown("---")

# 1. Advanced Live Chart pre-set to 10-Minute interval with All Indicators
st.markdown("### 📊 Live Chart (Set to 10-Minute for Operator & Whale Moves)")
st.markdown("*(ਇਸ ਚਾਰਟ ਵਿੱਚ ਉੱਪਰ ਟਾਈਮਫ੍ਰੇਮ ਨੂੰ **10m** ਸੈੱਟ ਕਰੋ ਅਤੇ ਸਾਰੇ ਇੰਡੀਕੇਟਰ ਦੇਖ ਕੇ ਸਟੀਕ ਟਰੇਡ ਲਗਾਓ)*")

tv_widget = """
<div class="tradingview-widget-container">
  <div id="tradingview_advanced_chart"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({
  "width": "100%",
  "height": 620,
  "symbol": "BINANCE:BTCUSDT",
  "interval": "10",
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
