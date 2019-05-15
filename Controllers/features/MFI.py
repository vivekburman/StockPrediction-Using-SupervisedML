import pandas as pd

def mfi(df, days):
    df2 = pd.DataFrame(index = df.index)
    df2['up_or_down'] = 0
    df2.loc[(df['Close'] > df['Close'].shift(1)),'up_or_down'] = 1
    df2.loc[(df['Close'] < df['Close'].shift(1)),'up_or_down'] = -1
    price = (df['High']+df['Low']+df['Close'])/3
    raw_money_flow = price*df['Volume']
    df2['1pmf'] = 0
    df2.loc[(df2['up_or_down'] == 1),'1pmf'] = raw_money_flow
    n_days_pmf = df2['1pmf'].rolling(days).sum()
    df2['1nmf'] = 0
    df2.loc[(df2['up_or_down'] == -1),'1nmf'] = raw_money_flow
    n_days_nmf = df2['1nmf'].rolling(days).sum()
    mf = n_days_pmf / n_days_nmf
    df['MFI{}'.format(days)] = 100 - 100 / (1+mf)

    return df
