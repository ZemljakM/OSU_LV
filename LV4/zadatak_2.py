# Na temelju rješenja prethodnog zadatka izradite model koji koristi i kategoricku varijable „Fuel Type“ kao ulaznu velicinu. 
# Pri tome koristite 1-od-K kodiranje kategorickih velicina. 
# Radi jednostavnosti nemojte skalirati ulazne velicine. Komentirajte dobivene rezultate. 
# Kolika je maksimalna pogreška u procjeni emisije C02 plinova u g/km? O kojem se modelu vozila radi?

from sklearn.preprocessing import OneHotEncoder
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt 
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score, max_error
import math
import numpy as np

data = pd.read_csv('data_C02_emission.csv')
ohe = OneHotEncoder ()
X_encoded = ohe.fit_transform ( data[['Fuel Type']]).toarray()
data['Fuel Type']=X_encoded

input_variables=['Fuel Consumption City (L/100km)',
                    'Fuel Consumption Hwy (L/100km)',
                    'Fuel Consumption Comb (L/100km)',
                    'Fuel Consumption Comb (mpg)',
                    'Engine Size (L)',
                    'Cylinders',
                    'Fuel Type']

output_variable=['CO2 Emissions (g/km)']

X=data[input_variables].to_numpy()
y=data[output_variable].to_numpy()

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.2, random_state=1)

linearModel=lm.LinearRegression()
linearModel.fit(X_train, y_train)

y_test_p=linearModel.predict(X_test)

MSE=mean_squared_error(y_test, y_test_p)
MAE=mean_absolute_error(y_test, y_test_p)
RMSE=math.sqrt(MSE)
MAPE=mean_absolute_percentage_error(y_test, y_test_p)
R2=r2_score(y_test, y_test_p)
print("MSE: ", round(MSE,2))
print("MAE: ", round(MAE, 2))
print("RMSE: ", round(RMSE,2))
print("MAPE: ", round(MAPE,2))
print("R2: ", round(R2,2))

max_err=abs(y_test_p-y_test)
index=np.argmax(max_err)
print(data['Make'][index], data['Model'][index])