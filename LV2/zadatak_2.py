import numpy as np
import matplotlib . pyplot as plt

data=np.loadtxt('data.csv', delimiter=',', skiprows=1, dtype=float)

#a
print(data.shape[0])

#b
x=data[:,1]
y=data[:,2]
plt.scatter(x, y, s=1)
plt.show()

#c
x1=data[::50,1]
y1=data[::50,2]
plt.scatter(x1, y1, s=5)
plt.show()

#d
print("max: ", np.max(x))
print("min: ", np.min(x))
print("mean: ", np.mean(x))

#e
hm=[]
wm=[]
ind = (data[:,0] == 1)
for i in range(len(x)):
    if ind[i]==True:
        hm.append(x[i])
    else:
        wm.append(x[i])

print("max -m: ", np.max(hm))
print("min -m: ", np.min(hm))
print("mean -m: ", np.mean(hm))
print("max -w: ", np.max(wm))
print("min -w: ", np.min(wm))
print("mean -w: ", np.mean(wm))