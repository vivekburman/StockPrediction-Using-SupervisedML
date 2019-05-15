import pandas as pd

def roc(df, days):
    df['ROC{0}'.format(days,)] = df['Close'].diff(days)/df['Close'].shift(days)*100
    return df
