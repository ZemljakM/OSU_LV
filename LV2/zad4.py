import numpy as np
import matplotlib.pyplot as plt

crno=np.ones((50,50))
bijelo=np.zeros((50,50))
stack=np.hstack((bijelo,crno))
stack2=np.hstack((crno,bijelo))
img=np.vstack((stack,stack2))
plt.imshow(img, cmap="gray")
plt.show()