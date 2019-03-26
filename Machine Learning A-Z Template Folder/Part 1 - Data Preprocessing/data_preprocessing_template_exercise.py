# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:03:30 2019

@author: Bator
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values

Y = dataset.iloc[:, 3].values

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values=np.nan, strategy='mean', axis=0, verbose=5)

