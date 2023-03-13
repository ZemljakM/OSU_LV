import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('data.csv', delimiter=',', skiprows=1, dtype=float)

print('Broj izvršenih mjerenja: ', len(data))


x1=np.array(data[:,1])
y1=np.array(data[:,2])
plt.scatter(x1, y1, alpha=0.8, c='b', s=5)
plt.title('Odnos visine i mase osobe')
plt.show()


x2=np.array(data[::50,1])
y2=np.array(data[::50,2])
plt.scatter(x2, y2, alpha=0.8, c='b', s=5)
plt.title('Odnos visine i mase svake 50. osobe')
plt.show()


print('Min visina: ', x1.min())
print('Max visina: ', x1.max())
print('Srednja visina: ', x1.mean())


m=(data[:,0]==1)
f=(data[:,0]==0)

print('Min muskarci: ', data[m,1].min())
print('Max muskarci: ', data[m,1].max())
print('Srednja muskarci: ', data[m,1].mean())

print('Min zene: ', data[f,1].min())
print('Max zene: ', data[f,1].max())
print('Srednja zene: ', data[f,1].mean())