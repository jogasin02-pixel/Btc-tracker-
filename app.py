import streamlit as st
import pandas as pd
import numpy as np
import requests
import time

# Page Configuration
st.set_page_config(
    page_title="BTC Operator Trap & Price Dashboard",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Bitcoin Operator Trap & Super-Fast Price Dashboard")
st.markdown("---")

# Function to fetch ultra-fast live price using Binance Public API with 10s timeout
@st.cache_data(ttl=2)
def get_fast_btc_data():
    try:
        url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return float(data['lastPrice']), float(data['highPrice']), float(data['lowPrice']), float(data['volume']), float(data['priceChangePercent'])
    except Exception:
        return None, None, None, None, None
    return None, None, None, None, None

# Layout for controls
col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("Control Panel")
    start_tracking = st.button("⚡ Start Fast Tracking")
    auto_refresh = st.checkbox("🔄 Auto Refresh (Every 3s)")

with col2:
    st.subheader("Live Market Status & Operator Trap Analysis")

# Placeholder for real-time updating
status_placeholder = st.empty()
metric_placeholder = st.empty()
trap_placeholder = st.empty()

with st.spinner("Fetching high-speed data..."):
    price, high, low, volume, price_change = get_fast_btc_data()

if price:
    # Instant Operator Trap Logic based on price action
    range_spread = high - low
    if range_spread > 0:
        position_in_range = (price - low) / range_spread
    else:
        position_in_range = 0.5

    if position_in_range > 0.85:
        trap_status = "⚠️ BEARISH TRAP ZONE (Smart money may dump)"
        trap_color = "red"
    elif position_in_range < 0.15:
        trap_status = "⚠️ BULLISH TRAP ZONE (Smart money may pump)"
        trap_color = "green"
    else:
        trap_status = "⚖️ NEUTRAL ZONE (Normal market movement)"
        trap_color = "orange"

    # Display Metrics Instantly
    with metric_placeholder.container():
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Live BTC Price", f"${price:,.2f}", f"{price_change:+.2f}%")
        m2.metric("24h High", f"${high:,.2f}")
        m3.metric("24h Low", f"${low:,.2f}")
        m4.metric("24h Volume", f"{volume:,.2f} BTC")

    with trap_placeholder.container():
        st.markdown(f"### **Operator Status: {trap_status}**")
        st.info(f"Price Position in 24h Range: {position_in_range * 100:.1f}%")
else:
    with metric_placeholder.container():
        st.error("Connection timeout. Retrying high-speed fetch...")

if auto_refresh:
    time.sleep(3)
    st.rerun()
else:
    st.info("Click **'Start Fast Tracking'** or check **'Auto Refresh'** to begin live updates.")
  
