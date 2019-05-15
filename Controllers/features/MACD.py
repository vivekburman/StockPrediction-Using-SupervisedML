import pandas as pd

def macd(df, low_days, high_days, period):
    l_ema = df['Close'].ewm(span=low_days).mean()
    h_ema = df['Close'].ewm(span=high_days).mean()
    macd = (h_ema - l_ema)
    macd_signal = macd.ewm(span=period).mean()
    return macd, macd_signal
