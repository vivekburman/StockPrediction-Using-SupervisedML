import pandas as pd

def trix(df, days):
    df['TRIX'] = df['Close'].ewm(ignore_na=False, com=days, adjust=True).mean()
    df['TRIX'] = df['TRIX'].ewm(ignore_na=False, com=days, adjust=True).mean()
    df['TRIX'] = df['TRIX'].ewm(ignore_na=False, com=days, adjust=True).mean()
    df['TRIX'] = df['TRIX'] / df['TRIX'].shift(1)
    return df
