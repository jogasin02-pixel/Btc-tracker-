import streamlit as st
import yfinance as yf
import time

st.set_page_config(
    page_title="BTC Operator Trap Dashboard",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Bitcoin Operator Trap & Super-Fast Price Dashboard")
st.markdown("---")

@st.cache_data(ttl=5)
def get_fast_btc_data():
    try:
        btc = yf.Ticker("BTC-USD")
        df = btc.history(period="1d", interval="1m")
        if not df.empty:
            price = float(df['Close'].iloc[-1])
            high = float(df['High'].max())
            low = float(df['Low'].min())
            volume = float(df['Volume'].sum())
            
            hist_24h = btc.history(period="2d")
            if len(hist_24h) >= 2:
                prev_close = float(hist_24h['Close'].iloc[-2])
                price_change = ((price - prev_close) / prev_close) * 100
            else:
                price_change = 0.0
                
            return price, high, low, volume, price_change
    except Exception:
        return None, None, None, None, None
    return None, None, None, None, None

col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("Control Panel")
    start_tracking = st.button("⚡ Start Fast Tracking")
    auto_refresh = st.checkbox("🔄 Auto Refresh (Every 1s)")

with col2:
    st.subheader("Live Market Status")

price, high, low, volume, price_change = get_fast_btc_data()

if price:
    range_spread = high - low
    position_in_range = (price - low) / range_spread if range_spread > 0 else 0.2
    if position_in_range > 0.85:
        trap_status = "⚠️ BEARISH TRAP ZONE (Smart money may dump)"
    elif position_in_range < 0.15:
        trap_status = "⚠️ BULLISH TRAP ZONE (Smart money may pump)"
    else:
        trap_status = "⚖️ NEUTRAL ZONE"

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Live BTC Price", f"${price:,.2f}", f"{price_change:+.2f}%")
    m2.metric("24h High", f"${high:,.2f}")
    m3.metric("24h Low", f"${low:,.2f}")
    m4.metric("24h Volume", f"{volume:,.0f} BTC")

    st.markdown(f"### **Operator Status: {trap_status}**")
    st.info(f"Price Position in 24h Range: {position_in_range * 100:.1f}%")
else:
    st.error("Error fetching data. Please wait a moment.")

if auto_refresh:
    time.sleep(3)
    st.rerun()
  
