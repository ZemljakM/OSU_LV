import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import sklearn.linear_model as lm
import sklearn.metrics as skm
import math

data=pd.read_csv('data_C02_emission.csv')

ohe = OneHotEncoder()
X_encoded=ohe.fit_transform(data[['Fuel Type']]).toarray()
data['Fuel Type']=X_encoded
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=1)

linearModel = lm.LinearRegression()
linearModel.fit(X_train, y_train)
y_test_p = linearModel.predict ( X_test )