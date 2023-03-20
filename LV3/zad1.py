import pandas as pd
import numpy as np

data = pd.read_csv('data_C02_emission.csv')

#a
print(len(data))
print(data.info())
print(data.isnull().sum())
print(data.duplicated().any())
data.dropna(axis=0).drop_duplicates().reset_index(drop=True)

data['Make']=data['Make'].astype('category')
data['Model']=data['Model'].astype('category')
data['Vehicle Class']=data['Vehicle Class'].astype('category')
data['Transmission']=data['Transmission'].astype('category')
data['Fuel Type']=data['Fuel Type'].astype('category')

#b
print(data.sort_values(by=['Fuel Consumption City (L/100km)'])[['Make','Model','Fuel Consumption City (L/100km)']].head(3))
print(data.sort_values(by=['Fuel Consumption City (L/100km)'])[['Make','Model','Fuel Consumption City (L/100km)']].tail(3))

#c
size_of_motor=data[(data['Engine Size (L)']>2.5) & (data['Engine Size (L)']<3.5)]
print("Velicina motora: ",len(size_of_motor))
print("prosjecna emisija: ", size_of_motor['CO2 Emissions (g/km)'].mean())


#d
audi=data[(data['Make']=='Audi')]
print("Broj Audi auta: ", len(audi))
audi2=audi[(audi['Cylinders']==4)]
print("Audi s 4 cilinda: ", audi2['CO2 Emissions (g/km)'].mean())


#e
cylinders=data[(data['Cylinders']>=4) & (data['Cylinders']%2==0)]
print("Broj vozila s 4,6,8... : ", len(cylinders))
emission_per_cylinder=data.groupby(['Cylinders']).agg({'CO2 Emissions (g/km)':'mean'})
print(emission_per_cylinder)


#f
regular=data[(data['Fuel Type']=='X')]
print("Regular gasoline: ",regular['Fuel Consumption City (L/100km)'].mean(), " median: ", regular['Fuel Consumption City (L/100km)'].median())
diesel=data[(data['Fuel Type']=='D')]
print("Diesel: ",diesel['Fuel Consumption City (L/100km)'].mean(), " median: ",diesel['Fuel Consumption City (L/100km)'].median())

#g
car=data[(data['Cylinders']==4) & (data['Fuel Type']=='D')].sort_values(by='Fuel Consumption City (L/100km)')
print(car.head(1))

#h
print("Broj vozila s rucnim mjenjacem: ", len(data[data['Transmission'].str.contains(pat='M[0-9]',regex=True)]))

#i
print (data.corr(numeric_only = True ))