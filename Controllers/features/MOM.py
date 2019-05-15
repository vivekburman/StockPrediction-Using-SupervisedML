import pandas as pd

def mom(df, days):
    df['MOM{}'.format(days)] = (df['Close'] - df['Close'].shift(1).fillna(0)) / df['Close'].shift(1)
    return df
