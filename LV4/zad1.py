import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error
import sklearn.metrics as skm
import math

data=pd.read_csv('data_C02_emission.csv')

input_variables=['Fuel Consumption City (L/100km)',
                    'Fuel Consumption Hwy (L/100km)',
                    'Fuel Consumption Comb (L/100km)',
                    'Fuel Consumption Comb (mpg)',
                    'Engine Size (L)',
                    'Cylinders']

output_variable=['CO2 Emissions (g/km)']

X=data[input_variables].to_numpy()
y=data[output_variable].to_numpy()


#a
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=1)


#b
X_train_tr=np.transpose(X_train)
X_test_tr=np.transpose(X_test)
plt.scatter(x=X_train_tr[0],y=y_train,c='r',s=5)
plt.scatter(x=X_test_tr[0],y=y_test,c='b',s=5)
plt.show()


#c
ss=StandardScaler()
X_train_ss=ss.fit_transform(X_train)
X_test_ss=ss.transform(X_test)
plt.figure()
plt.hist(X_train_tr[0])
plt.figure()
plt.hist(np.transpose(X_train_ss)[0])
plt.show()


#d
linearModel = lm.LinearRegression()
linearModel.fit(X_train_ss, y_train)
print(linearModel.coef_)

#e
y_test_p=linearModel.predict(X_test_ss)
plt.scatter(x=X_test_tr[0],y=y_test,c='b',s=5)
plt.scatter(x=X_test_tr[0],y=y_test_p,c='r',s=5)
plt.show()


#f
MSE=skm.mean_squared_error(y_test,y_test_p)
print("MAE: ", mean_absolute_error(y_test, y_test_p))
print("MSE: ", MSE)
print("RMSE: ", math.sqrt(MSE))
print("MAPE: ", skm.mean_absolute_percentage_error(y_test,y_test_p))
print("Koef det: ", skm.r2_score(y_test,y_test_p))


#g
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.3,random_state=1)

X_train_tr=np.transpose(X_train)
X_test_tr=np.transpose(X_test)

ss=StandardScaler()
X_train_ss=ss.fit_transform(X_train)
X_test_ss=ss.transform(X_test)

linearModel = lm.LinearRegression()
linearModel.fit(X_train_ss, y_train)

y_test_p=linearModel.predict(X_test_ss)

MSE=skm.mean_squared_error(y_test,y_test_p)
print("MAE: ", mean_absolute_error(y_test, y_test_p))
print("MSE: ", MSE)
print("RMSE: ", math.sqrt(MSE))
print("MAPE: ", skm.mean_absolute_percentage_error(y_test,y_test_p))
print("Koef det: ", skm.r2_score(y_test,y_test_p))

