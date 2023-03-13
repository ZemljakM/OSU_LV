import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,3,1],float)
y=np.array([1,2,2,1,1], float)
plt.plot(x,y,'y', linewidth=3, marker="*", markersize=20)
plt.axis([0.0,4.0,0.0,4.0])
plt.xlabel('x os')
plt.ylabel('y os')
plt.title('Primjer')
plt.show()