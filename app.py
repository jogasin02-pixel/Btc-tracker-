import streamlit as st
import requests
import time

st.set_page_config(page_title="BTC Live Trap Tracker", layout="centered")
st.title("🚀 Bitcoin Operator Trap & Price Dashboard")

# ਲਾਈਵ ਕੀਮਤ ਲੈਣ ਲਈ ਫੰਕਸ਼ਨ
def get_btc_price():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url)
        return float(response.json()['price'])
    except:
        return None

# ਡੈਸ਼ਬੋਰਡ ਦਾ ਲੇਆਉਟ
price_placeholder = st.empty()
status_placeholder = st.empty()

st.write("---")
st.subheader("Live Market Status")

if st.button("Start Live Tracking"):
    prev_price = get_btc_price()
    while True:
        curr_price = get_btc_price()
        if curr_price and prev_price:
            diff = curr_price - prev_price
            percent = (diff / prev_price) * 100
            
            price_placeholder.metric(label="Bitcoin (BTC/USDT)", value=f"${curr_price:,.2f}", delta=f"{percent:.2f}%")
            
            if abs(percent) >= 0.05:
                status_placeholder.warning(f"🚨 ਵੱਡਾ ਮੂਵ / ਟਰੈਪ ਫੜਿਆ ਗਿਆ! ਬਦਲਾਅ: {percent:.2f}%")
            else:
                status_placeholder.info("🟢 ਮਾਰਕੀਟ ਸਥਿਰ ਹੈ (ਸੈਕਨਿੰਗ ਚੱਲ ਰਹੀ ਹੈ)...")
                
            prev_price = curr_price
        time.sleep(3)
      
