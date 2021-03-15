# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:38:06 2021

@author: ramesh
"""
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

df = pd.read_excel("Critical Care Records.xlsx")
l = [i for i in range(0, 385)]

h = []
for j in l:
    h.append(df.loc[df['PATIENT_ID'] == j])

for i in range(385):
    column_means = h[i].mean()
    h[i] = h[i].fillna(column_means)

result = pd.concat(h)
resul1 = result.loc[result['WINDOW']=='0-2']

resul1=resul1.dropna() 
X = resul1.iloc[:, 1:230]
y = resul1.iloc[:, 230:231]

len(X_test.columns)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4, random_state=42)

X_train=X_train.drop(columns=['AGE_PERCENTILE', 'WINDOW'])
X_test=X_test.drop(columns=['AGE_PERCENTILE', 'WINDOW'])


y_train=np.ravel(y_train)

log_reg = LogisticRegression(random_state=0, max_iter = 2000)

log_reg.fit(X_train, y_train)

pickle.dump(log_reg, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict(X_test))

