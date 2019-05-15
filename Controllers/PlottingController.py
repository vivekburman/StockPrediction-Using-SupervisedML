import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
import matplotlib.pyplot as pyplt
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import datetime as dt
import numpy as np

class PlottingController:

    def plot_candlestick_ohlc(self,ohlc):
        ohlc['Date'] = ohlc['Date'].apply(mdates.date2num)
        f1, ax = pyplt.subplots(figsize = (10,5))
        candlestick_ohlc(ax, ohlc.values, width=.6, colorup='green', colordown='red')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        #ax.grid(True)
        plt.xlabel('Dates')
        plt.ylabel('OHLC')
        plt.title('Stock Price Chart')
        plt.show()

    def plot_correlation_matrix(self,df):
        f = df.loc[:, df.columns].corr().applymap(lambda x: round(x,2) if isinstance(x,float) else x)
        mask = np.zeros(f.shape, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True
        sns.heatmap(f, mask=mask, annot=True)
        plt.show()
    def plot_buy_sell(self, df):
        close = df['Close']
        x_up = df[df['UpOrDown'] == 1].index.tolist()
        y_up = df[df['UpOrDown'] == 1]['Close']
        x_down = df[df['UpOrDown'] == -1].index.tolist()
        y_down = df[df['UpOrDown'] == -1]['Close']
        fig = pyplt.figure(figsize=(15,5))
        pyplt.plot(df['Close'],color='g')
        pyplt.scatter(x_up, y_up, color='r', label = 'UP', marker='*', s=30)
        pyplt.scatter(x_down, y_down, color='black', label = 'DOWN', marker='.', s=25)
        pyplt.show()
