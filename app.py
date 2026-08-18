import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Pro Live Operator Trap & Chart", layout="wide")

st.title("🚀 BTC Live Operator Trap & Pro Chart")
st.markdown("---")

# Layout using Columns for Analysis & Live Chart
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Operator Trend & Signal Meter")
    # TradingView Technical Analysis Widget (Shows Buy/Sell/Trap Signals automatically)
    ta_widget = """
    <!-- TradingView Widget BEGIN -->
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
    <!-- TradingView Widget END -->
    """
    components.html(ta_widget, height=450)

with col2:
    st.subheader("📈 Live Order Flow & Market Summary")
    st.info("""
    **💡 Operator Trap & Trade Guide:**
    * **Bullish Trap (Long):** When price sweeps below daily support and quickly reverses, operators are trapping sellers. Look to **BUY / LONG**.
    * **Bearish Trap (Short):** When price spikes above daily resistance and fails, operators are trapping buyers. Look to **SELL / SHORT**.
    * Use the live chart below and the Technical Meter on the left to confirm your entry points.
    """)

st.markdown("---")
st.subheader("📉 Live Interactive TradingView Chart")

# TradingView Main Interactive Live Chart
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

