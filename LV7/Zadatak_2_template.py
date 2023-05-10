import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs\\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()


# Otvorite skriptu zadatak_2.py. Ova skripta ucitava originalnu RGB sliku test_1.jpg te ju transformira 
# u podatkovni skup koji dimenzijama odgovara izrazu (7.2) pri cemu je n broj elemenata slike, a m je jednak 3. 
# Koliko je razlicitih boja prisutno u ovoj slici?

print(len(np.unique(img_array,axis=0)))



# Primijenite algoritam K srednjih vrijednosti koji ce pronaci grupe u RGB vrijednostima elemenata originalne slike.

km = KMeans (n_clusters = 5, init ='k-means++', n_init = 5 , random_state = 0)
km.fit( img_array_aprox )
labels = km.predict( img_array_aprox )


# Vrijednost svakog elementa slike originalne slike zamijeni s njemu pripadajucim centrom.
centers=km.cluster_centers_
for i in range(len(img_array_aprox)):
    img_array_aprox[i]=centers[labels[i]]   # centers je matrica 5x3 (5 grupa i rgb), a u labels je pohranjeno kojem centru pripada


# Usporedite dobivenu sliku s originalnom. Mijenjate broj grupa K. Komentirajte dobivene rezultate.

plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()


img_array_aprox = np.reshape(img_array_aprox, (w,h, d))
# img_array_aprox=(img_array_aprox * 255).astype(np.uint8)             sa i bez ovog slike izgledaju identično 

plt.figure()
plt.title("Kvantizirana slika")
plt.imshow(img_array_aprox)
plt.tight_layout()
plt.show()

# Primijenite postupak i na ostale dostupne slike
for i in range(2,7):
    img = Image.imread(f"imgs\\test_{i}.jpg")
    img = img.astype(np.float64) / 255
    w,h,d = img.shape
    img_array = np.reshape(img, (w*h, d))
    img_array_aprox = img_array.copy()

    km = KMeans (n_clusters = 5, init ='k-means++', n_init = 5 , random_state = 0)
    km.fit( img_array_aprox )
    labels = km.predict( img_array_aprox )

    centers=km.cluster_centers_
    for i in range(len(img_array_aprox)):
        img_array_aprox[i]=centers[labels[i]]
    
    plt.figure()
    plt.title("Originalna slika")
    plt.imshow(img)
    plt.tight_layout()

    img_array_aprox = np.reshape(img_array_aprox, (w,h, d))

    plt.figure()
    plt.title("Kvantizirana slika")
    plt.imshow(img_array_aprox)
    plt.tight_layout()
    plt.show()


# Graficki prikažite ovisnost J o broju grupa K. 
# Koristite atribut inertia objekta klase KMeans. 
# Možete li uociti lakat koji upucuje na optimalni broj grupa?

inertia = []
K_range = range(2, 10)
for K in K_range:
    kmeans = KMeans(n_clusters=K)
    kmeans.fit(img_array)
    inertia.append(kmeans.inertia_)

# prikazi rezultate na grafu
plt.plot(K_range, inertia, marker='x')
plt.xlabel('Broj grupa K')
plt.ylabel('Inercija')
plt.title('Elbow metoda za određivanje optimalnog broja grupa')
plt.show()



# Elemente slike koji pripadaju jednoj grupi prikažite kao zasebnu binarnu sliku. 
# Što primjecujete?

km = KMeans(n_clusters = 5, init = 'k-means++')
km.fit(img_array)
labels = km.predict(img_array)

for i in range(1, 6):
    img_array_k = np.full((w*h, d), 255)
    for j in range(len(labels)):
        if labels[j] == i-1:
            img_array_k[j] = km.cluster_centers_[i-1]*255
    img_array_k = np.reshape(img_array_k.astype(np.uint8), (w, h, d))
    plt.figure()
    plt.imshow(img_array_k)
plt.show()


