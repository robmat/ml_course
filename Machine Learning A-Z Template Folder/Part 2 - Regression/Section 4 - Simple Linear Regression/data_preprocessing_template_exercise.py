# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:03:30 2019
@author: Bator
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values

"""
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0, verbose=5)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
"""

"""
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencode_x = LabelEncoder()
X[:, 0] = labelencode_x.fit_transform(X[:, 0])
oneHotEncoder_x = OneHotEncoder(categorical_features=[0])
X = oneHotEncoder_x.fit_transform(X).toarray()
labelencode_y = LabelEncoder()
Y = labelencode_y.fit_transform(Y)
"""

from sklearn.model_selection import train_test_split 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""