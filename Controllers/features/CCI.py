import pandas as pd

def cci(df, days):
    tp = (df['High']+df['Low']+df['Close'])/3
    df['CCI{0}'.format(days)] = tp-tp.rolling(window=days).mean()/(0.015*tp.rolling(window=days).std())
    return df
