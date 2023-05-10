from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler
import sklearn.linear_model as lm
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score
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


# Odaberite željene numericke velicine specificiranjem liste s nazivima stupaca. 
# Podijelite podatke na skup za ucenje i skup za testiranje u omjeru 80%-20%.

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.2, random_state=1)


# Pomocu matplotlib biblioteke i dijagrama raspršenja prikažite ovisnost emisije C02 plinova o jednoj numerickoj velicini. 
# Pri tome podatke koji pripadaju skupu za ucenje oznacite plavom bojom, a podatke koji pripadaju skupu za testiranje oznacite crvenom bojom.

plt.scatter(x=X_train[:,0], y=y_train, c='r', label='train')
plt.scatter(x=X_test[:,0], y=y_test, c='b', label='test')
plt.legend()
plt.show()


# Izvršite standardizaciju ulaznih velicina skupa za ucenje. Prikažite histogram vrijednosti jedne ulazne velicine prije i nakon skaliranja. 
# Na temelju dobivenih parametara skaliranja transformirajte ulazne velicine skupa podataka za testiranje.

ss=StandardScaler()
X_train_ss=ss.fit_transform(X_train)
X_test_ss=ss.transform(X_test)

plt.figure()
plt.hist(X_train[:,0], bins=15)
plt.figure()
plt.hist(X_train_ss[:,0], bins=15)
plt.show()


# Izgradite linearni regresijski modeli. Ispišite u terminal dobivene parametre modela i povežite ih s izrazom 4.6.

linearModel=lm.LinearRegression()
linearModel.fit(X_train_ss, y_train)

print(linearModel.intercept_)
print(linearModel.coef_)


# Izvršite procjenu izlazne velicine na temelju ulaznih velicina skupa za testiranje. 
# Prikažite pomocu dijagrama raspršenja odnos izmedu stvarnih vrijednosti izlazne velicine i procjene dobivene modelom.

y_test_p=linearModel.predict(X_test_ss)
plt.scatter(y_test, y_test_p)
plt.show()


# Izvršite vrednovanje modela na nacin da izracunate vrijednosti regresijskih metrika na skupu podataka za testiranje.
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



# Što se dogada s vrijednostima evaluacijskih metrika na testnom skupu kada mijenjate broj ulaznih velicina?
input_variables=['Fuel Consumption City (L/100km)',
                    'Engine Size (L)',
                    'Cylinders']
X=data[input_variables].to_numpy()
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.2, random_state=1)

X_train_ss=ss.fit_transform(X_train)
X_test_ss=ss.transform(X_test)

linearModel=lm.LinearRegression()
linearModel.fit(X_train_ss, y_train)

y_test_p=linearModel.predict(X_test_ss)

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
#smanjuje se tocnost
