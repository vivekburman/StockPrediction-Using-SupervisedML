import pandas as pd
import numpy as np
from ..features.ATR import atr

def calculate_pos(df):
    if df['moveUp']>0 and df['moveUp']>df['moveDown']:
        return df['moveUp']
    return 0

def calculate_neg(df):
    if df['moveDown']>0 and df['moveDown']>df['moveUp']:
        return df['moveDown']
    return 0
def adx(df, days):
    df = atr(df,days)
    df2 = pd.DataFrame(index = df.index)
    df2['moveUp'] = df['High'] - df['High'].shift(1)
    df2['moveDown'] = df['Low'].shift(1) - df['Low']
    df2['pdm'] = df2.apply(calculate_pos,axis=1)
    df2['ndm'] = df2.apply(calculate_neg, axis=1)
    df2['pdi'] = 100 * (days * df2['pdm'].ewm(span=days,adjust=False).mean() / df['ATR{}'.format(days)])
    df2['ndi'] = 100 * (days * df2['ndm'].ewm(span=days,adjust=False).mean() / df['ATR{}'.format(days)])
    temp = abs(df2['pdi']-df2['ndi']) / (df2['pdi'] + df2['ndi'])
    df['ADX{}'.format(days)] = temp.ewm(span=days, adjust=False).mean()
    return df
