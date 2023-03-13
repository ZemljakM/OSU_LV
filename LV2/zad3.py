import numpy as np
import matplotlib.pyplot as plt

img=plt.imread("road.jpg")
img = img[:,:,0].copy()

plt.imshow(img, alpha=0.5, cmap="gray")
plt.show()

print(img.shape)

img_sliced=img[:,int(img.shape[1]/4):int(img.shape[1]/2)]
plt.imshow(img_sliced, cmap="gray")
plt.show()

plt.imshow(np.rot90(img,3), cmap="gray")
plt.show()

plt.imshow(np.fliplr(img), cmap="gray")
plt.show()








