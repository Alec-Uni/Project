import random as random
import numpy as npy
import pandas as pd
import sklearn as sk
from sklearn import tree
import xgboost as xgb

#Import data as csv and shuffle
data = pd.read_csv("C:/Users/Alec/Desktop/Uni/Project/Point of Interest System Code/Data/NYC_Locations/dataset_TSMC2014_NYC.csv", header=0)   
#data.reindex(npy.random.permutation(data.index))
#rng = 1
print(data)
npy.reshape(-1, 1)

#Data split 
X_train_size = 0.4
X_test_size = 0.6
y_train_size = 0.4
y_test_size = 0.6

X = [[1, 5], [1, 5]]
Y = [1, 207581]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train_size, y_train_size)
#Basic Decision Tree training)


tree.plot_tree(clf)
#Basic Decision Tree testing
clf = tree.DecisionTreeClassifier
clf.fit(X_test_size, y_test_size)

#XGBoost training
xgb
#XGBoost testing
