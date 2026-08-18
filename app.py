import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="BTC Operator Trap & Pro Chart", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Analysis")
st.markdown("---")

# Real-time Operator Trap & Signal Box using TradingView Widget & Custom UI
st.subheader("🎯 Live Operator & Trader Trap Detector")

# Embedded TradingView Real-time Data & Analysis Engine
trap_analyzer_widget = """
<div style="background-color: #1e222d; padding: 20px; border-radius: 10px; color: white; font-family: sans-serif;">
    <h3 style="margin-top: 0; color: #00ffcc;">📊 Live Market Data & Operator Status</h3>
    
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-overview.js" async>
      {
      "symbols": [
        ["Binance:BTCUSDT|1D"]
      ],
      "chartOnly": false,
      "width": "100%",
      "height": "350",
      "locale": "en",
      "colorTheme": "dark",
      "autosize": false,
      "showVolume": true,
      "showMA": false,
      "hideDateRanges": false,
      "hideMarketStatus": false,
      "hideSymbolLogo": false,
      "scalePosition": "right",
      "scaleMode": "Normal",
      "fontFamily": "-apple-system, BlinkMacSystemFont, Trebuchet MS, Roboto, Ubuntu, sans-serif",
      "noTimeScale": false,
      "valuesTracking": "1",
      "changeMode": "price-and-percent",
      "chartType": "candlesticks",
      "maLineColor": "#2962FF",
      "maLineWidth": 1,
      "maLength": 9,
      "headerFontSize": "medium",
      "backgroundColor": "rgba(19, 23, 34, 0)",
      "gridLineColor": "rgba(42, 46, 57, 0.06)",
      "dateFontColor": "rgba(178, 181, 189, 1)",
      "timeZone": "Etc/UTC",
      "dateFormat": "yyyy-MM-dd"
    }
      </script>
    </div>
    <!-- TradingView Widget END -->
    
    <div style="margin-top: 15px; padding: 15px; background-color: #2a2e39; border-left: 5px solid #ff007f; border-radius: 5px;">
        <h4 style="margin: 0 0 10px 0; color: #ff007f;">🚨 Operator Trap & Action Strategy:</h4>
        <p style="margin: 0; font-size: 14px; line-height: 1.5;">
            * <b>Resistance / High Trap (Bearish):</b> If price spikes near 24h High and rejects, big operators are trapping buyers. <b>Look for SELL / SHORT position.</b><br>
            * <b>Support / Low Trap (Bullish):</b> If price dips below 24h Low and reverses quickly, operators are trapping sellers. <b>Look for BUY / LONG position.</b>
        </p>
    </div>
</div>
"""

components.html(trap_analyzer_widget, height=580)

st.markdown("---")
st.subheader("📉 Full Live Interactive TradingView Chart")

# Main Interactive Chart
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
