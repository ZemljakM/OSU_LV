import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data_C02_emission.csv')

# Pomocu histograma prikažite emisiju C02 plinova. Komentirajte dobiveni prikaz
plt.hist(data['CO2 Emissions (g/km)'])
plt.show()


# Pomocu dijagrama raspršenja prikažite odnos izmedu gradske potrošnje goriva i emisije C02 plinova. 
# Komentirajte dobiveni prikaz. Kako biste bolje razumjeli odnose izmedu velicina, obojite tockice na dijagramu raspršenja s obzirom na tip goriva.

gorivo=np.array(['X', 'Z', 'D', 'E', 'N'])
colors=np.array(['r', 'b', 'g', 'y', 'm'])

for i in range(0,5):
    data1=data[data['Fuel Type']==gorivo[i]]
    x=data1['Fuel Consumption City (L/100km)']
    y=data1['CO2 Emissions (g/km)']
    plt.scatter(x,y,c=colors[i], label=gorivo[i])
plt.legend()
plt.show()


# Pomocu kutijastog dijagrama prikažite razdiobu izvangradske potrošnje s obzirom na tip goriva. 
# Primjecujete li grubu mjernu pogrešku u podacima?

potrosnja=data.groupby(['Fuel Type'])
potrosnja.boxplot(column=['Fuel Consumption Hwy (L/100km)'], by=['Fuel Type'])
plt.show()


# Pomocu stupcastog dijagrama prikažite broj vozila po tipu goriva. Koristite metodu groupby.

broj_vozila=data.groupby(['Fuel Type'])['Fuel Type'].value_counts().reset_index()
broj_vozila.columns=['Fuel Type', 'counts']
plt.bar(broj_vozila['Fuel Type'], broj_vozila['counts'])
plt.show()



# Pomocu stupcastog grafa prikažite na istoj slici prosjecnu C02 emisiju vozila s obzirom na broj cilindara.
cylinders=data.groupby(['Cylinders'])['CO2 Emissions (g/km)'].mean()
cylinders.plot(kind='bar')
plt.show()

