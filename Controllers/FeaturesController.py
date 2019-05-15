import pandas as pd
from Controllers.features.OBV import obv
from Controllers.features.RSI import rsi
from Controllers.features.ATR import atr
from Controllers.features.MFI import mfi
from Controllers.features.ADX import adx
from Controllers.features.MOM import mom
from Controllers.features.CCI import cci
from Controllers.features.ROC import roc
from Controllers.features.WILLR import willr
from Controllers.features.TRIX import trix

def calculate_features(df):
    #obv
    df = obv(df)

    #RSI6, RSI12
    df = rsi(df, 6)
    df = rsi(df, 12)

    #ATR14
    df = atr(df, 14)

    #MFI14
    df = mfi(df, 14)

    #ADX14, ADX20
    df = adx(df, 14)
    df = adx(df, 20)

    #MOM1, MOM3
    df = mom(df, 1)
    df = mom(df, 3)

    #CCI12, CCI20
    df = cci(df, 12)
    df = cci(df, 20)

    #ROC3, ROC12
    df = roc(df, 3)
    df = roc(df, 12)

    #WILLR10
    df = willr(df,10)

    #TRIX10
    df = trix(df, 10)

    return df
