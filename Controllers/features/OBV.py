import pandas as pd

previous_obv = 0
def calculate(df):
    global previous_obv
    if df['change'] > 0:
        previous_obv = previous_obv + df['change']
        return previous_obv
    if df['change'] < 0:
        previous_obv = previous_obv + df['change']
        return previous_obv
    previous_obv = df['change']
    return previous_obv

def obv(df):
    df2 = pd.DataFrame(index = df.index)
    df2['change'] = 0
    df2.loc[(df['Close'] > df['Close'].shift(1).fillna(0)),'change'] = df['Volume']
    df2.loc[(df['Close'] < df['Close'].shift(1).fillna(0)),'change'] = -df['Volume']
    df['OBV']= df2.apply(calculate, axis=1)
    return df
