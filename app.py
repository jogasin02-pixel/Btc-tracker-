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

# Function to fetch live price using CoinGecko Public API
@st.cache_data(ttl=5)
def get_fast_btc_data():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_high_24h=true&include_low_24h=true&include_market_cap=true&include_24hr_change=true"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()['bitcoin']
            price = float(data['usd'])
            high = float(data['usd_high_24h'])
            low = float(data['usd_low_24h'])
            volume = float(data.get('usd_market_cap', 0) / price) # Estimating volume proxy if needed
            price_change = float(data['usd_24h_change'])
            return price, high, low, volume, price_change
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
    elif position_in_range < 0.15:
        trap_status = "⚠️ BULLISH TRAP ZONE (Smart money may pump)"
    else:
        trap_status = "⚖️ NEUTRAL ZONE (Normal market movement)"

    # Display Metrics Instantly
    with metric_placeholder.container():
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Live BTC Price", f"${price:,.2f}", f"{price_change:+.2f}%")
        m2.metric("24h High", f"${high:,.2f}")
        m3.metric("24h Low", f"${low:,.2f}")
        m4.metric("Market Cap / Vol", f"${volume:,.0f}")

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
    
