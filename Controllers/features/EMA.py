import pandas as pd

def ema(df, period):
    df['EMA{}'.format(period)] = df['Close'].ewm(span=period).mean()
    return df
