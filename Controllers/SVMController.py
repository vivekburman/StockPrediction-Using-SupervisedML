import pandas as pd
from Controllers.FeaturesController import calculate_features
from sklearn import svm, preprocessing
from Controllers.PlottingController import PlottingController
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from Controllers.InitializeController import InitializeController

class SVMController:

    def solve_svm(self, company, period):

        print ('Im inside solve_svm')

        initial = InitializeController()
        df, X_train, y_train, X_test, y_test, column_names, scaler, ohlc, close, X, y = initial.init(company, period)
        
        #train data
        clf = svm.SVC(kernel = 'rbf', gamma=0.2, C=1)

        clf_train = clf.fit(X_train, y_train)
        y_predict = clf.predict(X_test)

        report = classification_report(y_test, y_predict)
        print ('Classification Report:- ')
        print(report)

        #save and return
        plot = PlottingController()

        #might require thread per plot
        plot.plot_candlestick_ohlc(ohlc)
        plot.plot_correlation_matrix(X)
        plot.plot_buy_sell(close)
        print ('Exiting SVM!')
        return None
