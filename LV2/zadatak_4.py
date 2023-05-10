import numpy as np
import matplotlib . pyplot as plt

crna=np.zeros((50,50))
bijela=np.ones((50,50))

prvi=np.vstack((crna,bijela))
drugi=np.vstack((bijela, crna))
slika=np.hstack((prvi, drugi))
plt.imshow(slika,cmap="gray")
plt.show()