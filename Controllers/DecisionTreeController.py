import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import graphviz
import pydotplus
import collections
from sklearn.metrics import classification_report
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from Controllers.FeaturesController import calculate_features
from sklearn import preprocessing
from Controllers.PlottingController import PlottingController 
from Controllers.InitializeController import InitializeController


class DecisionTreeController:

    def solve_decision_tree(self, company, period):
        print ('Im inside solve_decision_tree')

        initial = InitializeController()
        df, X_train, y_train, X_test, y_test, column_names, scaler, ohlc, close, X, y = initial.init(company, period)

        predictors_list = column_names
        clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_leaf= 6)
        clf = clf.fit(X_train, y_train)
        dot_data = tree.export_graphviz(clf, out_file=None,filled=True,feature_names=predictors_list)
        graphviz.Source(dot_data)

        dot_data = tree.export_graphviz(clf,
                                feature_names=predictors_list,
                                out_file=None,
                                filled=True,
                                rounded=True)
        graph = pydotplus.graph_from_dot_data(dot_data)

        colors = ('turquoise', 'orange')
        edges = collections.defaultdict(list)

        for edge in graph.get_edge_list():
            edges[edge.get_source()].append(int(edge.get_destination()))

        for edge in edges:
            edges[edge].sort()
            for i in range(2):
                dest = graph.get_node(str(edges[edge][i]))[0]
                dest.set_fillcolor(colors[i])

        graph.write_png('tree_clf.png')
        y_pred = clf.predict(X_test)
        report = classification_report(y_test, y_pred)
        print ('Classification Report:- ')
        print(report)
        try:
            img=mpimg.imread('tree_clf.png')
            imgplot = plt.imshow(img)
            plt.show()
        except IOError:
            pass
        
        #save and return
        plot = PlottingController()

        #might require thread per plot
        plot.plot_candlestick_ohlc(ohlc)
        plot.plot_buy_sell(close)
        print ('Exiting Decision Tree!')
        return None