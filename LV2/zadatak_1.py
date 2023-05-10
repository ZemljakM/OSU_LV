import numpy as np
import matplotlib . pyplot as plt

x=np.array([1,2,3,3,1], np.float32)
y=np.array([1,2,2,1,1], np.float32)
plt.plot(x,y,'r',linewidth=5, marker="*", markersize=10)
plt.axis([0.0,4.0,0.0,4.0])
plt.xlabel("x os")
plt.ylabel("y os")
plt.title("Primjer")
plt.show()