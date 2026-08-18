import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# Page Configuration
st.set_page_config(page_title="BTC Pro Trap Dashboard", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

# 1. Data Fetching (Real-time)
@st.cache_data(ttl=10)
def get_btc_data_for_chart():
    try:
        btc = yf.Ticker("BTC-USD")
        df = btc.history(period="7d", interval="15m")
        if not df.empty:
            current_price = float(df['Close'].iloc[-1])
            daily_high = float(df['High'].last('1d').max())
            daily_low = float(df['Low'].last('1d').min())
            return df, current_price, daily_high, daily_low
    except:
        return None, None, None, None
    return None, None, None, None

# 2. Trap Logic (Enhanced)
df, price, high, low = get_btc_data_for_chart()

if price:
    range_spread = high - low
    pos_in_range = (price - low) / range_spread if range_spread > 0 else 0.5
    
    # Trap Status
    if pos_in_range > 0.85:
        status = "⚠️ BEARISH TRAP ZONE (Operators selling)"
        zone_color = "rgba(255, 0, 0, 0.2)"
        trap_zone_high = high
        trap_zone_low = high - (range_spread * 0.15)
    elif pos_in_range < 0.15:
        status = "⚠️ BULLISH TRAP ZONE (Operators buying)"
        zone_color = "rgba(0, 255, 0, 0.2)"
        trap_zone_high = low + (range_spread * 0.15)
        trap_zone_low = low
    else:
        status = "⚖️ NEUTRAL ZONE"
        zone_color = "rgba(200, 200, 200, 0.2)"
        trap_zone_high = 0
        trap_zone_low = 0

    # 3. Metric Display (Fixed Syntax)
    col1, col2, col3 = st.columns(3)
    col1.metric("Live BTC Price", f"${price:,.2f}")
    col2.metric("24h Range", f"H: ${high:,.2f} / L: ${low:,.2f}")
    col3.metric("Operator Status", status)

    # 4. CUSTOM PLOTLY CHART
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'],
        name="BTC/USD",
        increasing_line_color='cyan',
        decreasing_line_color='magenta'
    ))

    if trap_zone_high > 0:
        fig.add_shape(
            type="rect",
            xref="paper", yref="y",
            x0=0, x1=1,
            y0=trap_zone_low, y1=trap_zone_high,
            fillcolor=zone_color,
            opacity=0.5,
            layer="below",
            line_width=0,
        )
        fig.add_annotation(
            xref="paper", yref="y",
            x=0.98, y=(trap_zone_high + trap_zone_low) / 2,
            text=status,
            showarrow=False,
            font=dict(color="black", size=10),
            bgcolor="white",
            bordercolor="black",
            borderwidth=1
        )

    fig.add_trace(go.Scatter(
        x=[df.index[0], df.index[-1]],
        y=[high, high],
        mode="lines", name="24h High",
        line=dict(color="red", width=1, dash="dash")
    ))
    fig.add_trace(go.Scatter(
        x=[df.index[0], df.index[-1]],
        y=[low, low],
        mode="lines", name="24h Low",
        line=dict(color="green", width=1, dash="dash")
    ))
    fig.add_trace(go.Scatter(
        x=[df.index[0], df.index[-1]],
        y=[price, price],
        mode="lines", name="Live Price",
        line=dict(color="white", width=2)
    ))

    fig.update_layout(
        title="Advanced BTC Operator Trap Chart",
        yaxis_title="BTC Price (USD)",
        xaxis_title="Time",
        height=700,
        template="plotly_dark",
        xaxis_rangeslider_visible=False,
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Error fetching data. Please wait a moment.")

if st.checkbox("🔄 Auto Refresh (Every 10s)", value=True):
    import time
    time.sleep(10)
    st.rerun()
    
