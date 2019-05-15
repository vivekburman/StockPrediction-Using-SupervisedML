import pandas as pd
import numpy as np
def atr(df, days):
    df2 = pd.DataFrame(index= df.index)
    df2['x']= abs(df['High']-df['Low'])
    df2['y'] = abs(df['High']-df['Close'].shift(1))
    df2['z'] = abs(df['Low']-df['Close'].shift(1))
    atr = df2.apply(np.max, axis=1)
    df['ATR{0}'.format(days)] = (atr.rolling(window=days-1).sum()+atr)/days
    return df
