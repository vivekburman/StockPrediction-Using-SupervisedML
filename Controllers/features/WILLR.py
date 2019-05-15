import pandas as pd

def willr(df,days):
    ax = df['High'].rolling(window=days).max()
    df['WILLR{0}'.format(days,)] = (ax-df['Close'])/(ax-df['Low'].rolling(window=days).min())*100
    return df
