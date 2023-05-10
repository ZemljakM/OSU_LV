import pandas as pd

data = pd.read_csv('data_C02_emission.csv')

# Koliko mjerenja sadrži DataFrame? Kojeg je tipa svaka velicina? 
# Postoje li izostale ili duplicirane vrijednosti? Obrišite ih ako postoje. 
# Kategoricke velicine konvertirajte u tip category.

print(len(data))
print(data.info())
data.dropna(axis=0)
data.drop_duplicates()
data = data.reset_index ( drop = True )
data[data.select_dtypes(['object']).columns] = data.select_dtypes(['object']).apply(lambda x: x.astype('category'))




# Koja tri automobila ima najvecu odnosno najmanju gradsku potrošnju? 
# Ispišite u terminal: ime proizvodaca, model vozila i kolika je gradska potrošnja.

first_three=data.sort_values(by=['Fuel Consumption City (L/100km)'])[['Make', 'Model', 'Fuel Consumption City (L/100km)']].head(3)     # ascending=False za padajuće sortiranje
last_three=data.sort_values(by=['Fuel Consumption City (L/100km)'])[['Make', 'Model', 'Fuel Consumption City (L/100km)']].tail(3)
print(first_three)
print(last_three)




# Koliko vozila ima velicinu motora izmedu 2.5 i 3.5 L? 
# Kolika je prosjecna C02 emisija plinova za ova vozila?

motor=data[(data['Engine Size (L)']>2.5) & (data['Engine Size (L)']<3.5)]
print(len(motor))
print(motor['CO2 Emissions (g/km)'].mean())




# Koliko mjerenja se odnosi na vozila proizvodaca Audi? 
# Kolika je prosjecna emisija C02 plinova automobila proizvodaca Audi koji imaju 4 cilindara?

audi=data[(data['Make']=='Audi')]
print(len(audi))
audi_4cil=audi[audi['Cylinders']==4]
print(audi_4cil['CO2 Emissions (g/km)'].mean())




# Koliko je vozila s 4,6,8. . . cilindara? 
# Kolika je prosjecna emisija C02 plinova s obzirom na broj cilindara?

cylinders=data[(data['Cylinders']>=4) & (data['Cylinders']%2==0)].groupby(['Cylinders'])['Cylinders'].value_counts()
print(cylinders)
cy_em=data.groupby(['Cylinders']).agg({'CO2 Emissions (g/km)':'mean'})
print(cy_em)



# Kolika je prosjecna gradska potrošnja u slucaju vozila koja koriste dizel, 
# a kolika za vozila koja koriste regularni benzin? 
# Koliko iznose medijalne vrijednosti?

dizel=data[data['Fuel Type']=='D']['Fuel Consumption City (L/100km)']
regbenzin=data[data['Fuel Type']=='X']['Fuel Consumption City (L/100km)']
print("Prosjecna: ", dizel.mean(), ", Medijalna: ", dizel.median())
print("Prosjecna: ", regbenzin.mean(), ", Medijalna: ", regbenzin.median())



# Koje vozilo s 4 cilindra koje koristi dizelski motor ima najvecu gradsku potrošnju goriva?
car=data[(data['Cylinders']==4) & (data['Fuel Type']=='D')].sort_values(by=['Fuel Consumption City (L/100km)']).tail(1)
print("4 cilindra i dizel: ", car[['Make', 'Model', 'Fuel Consumption City (L/100km)']])



# Koliko ima vozila ima rucni tip mjenjaca (bez obzira na broj brzina)?

manual=data[data['Transmission'].str.contains('M[0-9]')]      # ili str.startswith('M')
print(len(manual))



# Izracunajte korelaciju izmedu numerickih velicina. Komentirajte dobiveni rezultat.
print ( data.corr ( numeric_only = True ) )
# sto je blize 1 veca je korelacije, blize 0 nema korelacije, blize -1 negativna korelacija
# na dijagonalama 1 jer svaki sam sa sobom ima najvecu korelaciju
