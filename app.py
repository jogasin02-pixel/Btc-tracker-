import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import requests

# Page Configuration
st.set_page_config(page_title="BTC Operator Trap & Pro Chart", layout="wide")

st.title("🚀 Bitcoin Operator Trap & Pro Chart")
st.markdown("---")

# Fetch Real-time Data from Binance Public API
@st.cache_data(ttl=5)
def get_operator_trap_data():
    try:
        url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=15m&limit=96"
        response = requests.get(url)
        data = response.json()
        
        df = pd.DataFrame(data, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'qav', 'trades', 'tbav', 'tqav', 'ignore'
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

df, price, high, low = get_operator_trap_data()

if price:
    spread = high - low
    pos_in_range = (price - low) / spread if spread > 0 else 0.5
    
    # --- OPERATOR TRAP LOGIC ---
    if pos_in_range >= 0.80:
        trap_status = "🚨 BEARISH OPERATOR TRAP (SELL / SHORT ZONE)"
        action_msg = "Operators/Whales are trapping retail buyers at the top resistance. High chance of a sharp downside fall. Look for **SHORT** entry."
        box_type = "error"
        zone_color = "rgba(255, 0, 0, 0.2)"
        zone_top = high
        zone_bottom = high - (spread * 0.20)
    elif pos_in_range <= 0.20:
        trap_status = "🚀 BULLISH OPERATOR TRAP (BUY / LONG ZONE)"
        action_msg = "Operators/Whales are trapping retail sellers at the bottom support. High chance of a sharp upward bounce. Look for **LONG** entry."
        box_type = "success"
        zone_color = "rgba(0, 255, 0, 0.2)"
        zone_top = low + (spread * 0.20)
        zone_bottom = low
    else:
        trap_status = "⚖️ NEUTRAL ZONE (NO TRAP - WAIT)"
        action_msg = "Price is in the middle of the range. Operators are accumulating. Wait for price to reach 24h High or Low extremes to find traps."
        box_type = "warning"
        zone_top = 0
        zone_bottom = 0

    # Display Operator Result at the Top
    if box_type == "error":
        st.error(f"### {trap_status}\n* **Live Price:** ${price:,.2f} | **24h Range:** ${low:,.2f} - ${high:,.2f}\n* **Operator Action:** {action_msg}")
    elif box_type == "success":
        st.success(f"### {trap_status}\n* **Live Price:** ${price:,.2f} | **24h Range:** ${low:,.2f} - ${high:,.2f}\n* **Operator Action:** {action_msg}")
    else:
        st.warning(f"### {trap_status}\n* **Live Price:** ${price:,.2f} | **24h Range:** ${low:,.2f} - ${high:,.2f}\n* **Operator Action:** {action_msg}")

    # Plotly Chart with Highlighted Operator Trap Zone
    fig = go.Figure()

    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['open'], high=df['high'], low=df['low'], close=df['close'],
        name="BTC/USDT",
        increasing_line_color='#00ffcc',
        decreasing_line_color='#ff007f'
    ))

    # Highlight Trap Zone Box if active
    if zone_top > 0:
        fig.add_shape(
            type="rect",
            xref="paper", yref="y",
            x0=0, x1=1,
            y0=zone_bottom, y1=zone_top,
            fillcolor=zone_color,
            opacity=0.7,
            layer="below",
            line_width=1,
            line_dash="dot",
            line_color="white"
        )

    # 24h High and Low Lines
    fig.add_trace(go.Scatter(
        x=[df.index[0], df.index[-1]], y=[high, high],
        mode="lines", name="24h High (Resistance)",
        line=dict(color="red", width=2, dash="dash")
    ))
    fig.add_trace(go.Scatter(
        x=[df.index[0], df.index[-1]], y=[low, low],
        mode="lines", name="24h Low (Support)",
        line=dict(color="green", width=2, dash="dash")
    ))

    fig.update_layout(
        title="Live Operator Trap Zones & Price Action",
        yaxis_title="Price (USD)",
        xaxis_title="Time",
        height=650,
        template="plotly_dark",
        xaxis_rangeslider_visible=False,
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Connecting to live feed... Please wait a moment.")

if st.checkbox("🔄 Auto Refresh (Every 10s)", value=True):
    import time
    time.sleep(10)
    st.rerun()
      
