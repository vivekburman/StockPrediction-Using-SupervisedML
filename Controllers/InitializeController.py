import pandas as pd
from Controllers.FeaturesController import calculate_features
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class InitializeController:
    def init(self, company, period):
        #read files
        df = pd.read_csv('./data_files/'+company+'.csv', index_col= None)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.set_index('Date')

        #calculate_features
        df = calculate_features(df)
        df.dropna(inplace=True)

        #ohlc
        ohlc = pd.DataFrame(df[['Open','High','Low','Close']], index = df.index).reset_index()

        #divide data into X and y
        df['UpOrDown'] = 0
        if period == 1:
            df.loc[(df['Close'] > df['Close'].shift(1)),'UpOrDown'] = 1
            df.loc[(df['Close'] < df['Close'].shift(1)),'UpOrDown'] = -1
        else:
            df['SMA'] = df['Close'].rolling(window = 3).mean()
            df.dropna(inplace=True)
            df.loc[df['SMA'] > df['SMA'].shift(3), 'UpOrDown'] = 1
            df.loc[df['SMA'] < df['SMA'].shift(3), 'UpOrDown'] = -1
            df.drop(columns='SMA', inplace=True, axis=0)
        y = df['UpOrDown']
        close = pd.DataFrame(df[['Close','UpOrDown']], index=df.index)
        df.drop(['Open','High','Low','Close','UpOrDown'],axis=1 ,inplace=True)
        X = df

        #split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        #Scale data
        column_names = df.columns
        scaler = preprocessing.StandardScaler()
        X_train = scaler.fit_transform(X_train)
        #X_train = pd.DataFrame(X_train, columns = column_names,index=df.index)
        X_test = scaler.transform(X_test)

        return df, X_train, y_train, X_test, y_test, column_names, scaler, ohlc, close, X, y
