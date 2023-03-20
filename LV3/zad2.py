import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools

data = pd.read_csv('data_C02_emission.csv')

#a
plt.figure ()
data ['CO2 Emissions (g/km)'].plot( kind ='hist', bins = 20 )


#b
plt.figure()
colors=["r","b","g","k","y"]
gas=['X','Z','D','E','N']

for i in range(0,5):
    data1=data[data['Fuel Type']==gas[i]]
    x=np.array(data1['Fuel Consumption City (L/100km)'])
    y=np.array(data1['CO2 Emissions (g/km)'])
    plt.scatter(x,y, c=colors[i], s=5 )


#c
consumption=data.groupby(['Fuel Type'])
consumption.boxplot(column=['Fuel Consumption Hwy (L/100km)'])

#d
plt.figure()
fuel=data.groupby(['Fuel Type']).size()
fuel.plot(kind='bar')

#e
plt.figure()
emission=data.groupby(['Cylinders']).agg({'CO2 Emissions (g/km)':'mean'})
emission.plot(kind='bar')

plt.show()