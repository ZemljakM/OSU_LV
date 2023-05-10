import numpy as np
import matplotlib . pyplot as plt
img = plt . imread ("road.jpg")
img = img [ :,:,0]. copy ()
plt . imshow ( img , cmap ="gray")
plt . show ()


#a
plt . imshow ( img, vmin=0, vmax=100, cmap ="gray")
plt . show ()

#b
cutout=img[:,160:320]
plt . imshow ( cutout, cmap ="gray")
plt . show ()

#c
rotation=np.rot90(img)
plt . imshow ( rotation, cmap ="gray")
plt . show ()

#d
flip=np.fliplr(img)
plt . imshow ( flip, cmap ="gray")
plt . show ()
