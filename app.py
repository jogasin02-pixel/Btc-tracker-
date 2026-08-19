import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Auto Scalp Robot", layout="centered")

st.title("⚡ BTC Auto Scalp Signal & Operator Bot")
st.markdown("---")

st.markdown("### 🎯 Live Automated Scalping Decision & Signal")
st.markdown("*(यह बोट अपने आप मार्केट को पढ़कर नीचे बता रहा है कि इस समय क्या करना है)*")

# TradingView Automated Technical Analysis Widget (Instant Buy/Sell Signal)
ta_widget = """
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
  {
  "interval": "1m",
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

components.html(ta_widget, height=480)
