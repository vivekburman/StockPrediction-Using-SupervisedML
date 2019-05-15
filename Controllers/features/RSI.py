import pandas as pd
def rsi(df, days):
    change = pd.to_numeric(df['Close'].diff(1))
    gain = change.mask(change<0, 0)
    loss = change.mask(change>0, 0)
    avg_gain = gain.ewm(com=days-1, min_periods=days).mean()
    avg_loss = loss.ewm(com=days-1, min_periods=days).mean()
    rs = abs(avg_gain/avg_loss)
    df['RSI{0}'.format(days)] = 100-(100/1+rs)
    return df
