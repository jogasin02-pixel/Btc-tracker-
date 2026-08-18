import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import requests

# Page Configuration
st.set_page_config(page_title="BTC Pro Trap Dashboard", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

# 1. Fetch data directly from Binance Public API (Fast & No Errors)
@st.cache_data(ttl=5)
def get_binance_data():
    try:
        url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=15m&limit=96"
        response = requests.get(url)
        data = response.json()
        
        df = pd.DataFrame(data, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
        ])
        
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = df[col].astype(float)
            
        current_price = df['close'].iloc[-1]
        daily_high = df['high'].max()
        daily_low = df['low'].min()
        
        return df, current_price, daily_high, daily_low
    except Exception as e:
        return None, None, None, None

df, price, high, low = get_binance_data()

if price:
    range_spread = high - low
    pos_in_range = (price - low) / range_spread if range_spread > 0 else 0.5
    
    # Trap Status & Zones
    if pos_in_range > 0.85:
        status = "⚠️ BEARISH TRAP ZONE (Operators selling - Look for Sell/Short)"
        zone_color = "rgba(255, 0, 0, 0.2)"
        trap_zone_high = high
        trap_zone_low = high - (range_spread * 0.15)
    elif pos_in_range < 0.15:
        status = "⚠️ BULLISH TRAP ZONE (Operators buying - Look for Buy/Long)"
        zone_color = "rgba(0, 255, 0, 0.2)"
        trap_zone_high = low + (range_spread * 0.15)
        trap_zone_low = low
    else:
        status = "⚖️ NEUTRAL ZONE (Wait for breakout)"
        zone_color = "rgba(200, 200, 200, 0.2)"
        trap_zone_high = 0
        trap_zone_low = 0

    # Metric Display
    col1, col2, col3 = st.columns(3)
    col1.metric("Live BTC Price", f"${price:,.2f}")
    col2.metric("24h Range", f"H: ${high:,.2f} / L: ${low:,.2f}")
    col3.metric("Operator Status", status)

    # PLOTLY CHART WITH ZONES
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['open'], high=df['high'], low=df['low'], close=df['close'],
        name="BTC/USDT",
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
        title="Advanced BTC Operator Trap Chart with Buy/Sell Zones",
        yaxis_title="BTC Price (USD)",
        xaxis_title="Time",
        height=700,
        template="plotly_dark",
        xaxis_rangeslider_visible=False,
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Connecting to Binance API... Please wait a few seconds and refresh.")

if st.checkbox("🔄 Auto Refresh (Every 10s)", value=True):
    import time
    time.sleep(10)
    st.rerun()
    
