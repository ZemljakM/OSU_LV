import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from keras.models import load_model


# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: prikazi nekoliko slika iz train skupa
#for i in range(1,5):
 #   plt.figure()
  #  plt.imshow(x_train[i])
  #  print("Oznaka slike: ", y_train[i])
#plt.show()


# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)


# učitati izgrađenu mrežu iz zad 1
model = load_model ('FCN/')

predictions = model.predict(x_test_s)


# transformacija iz 2D u 1D polje s indexima najvećih vrijednosti
y_test_s = np.argmax(y_test_s,axis=1)        
predictions = np.argmax(predictions, axis=1)

# Stvaranje polja sa greškama i polja sa indexima tih grešaka
mistakes=x_test_s[y_test_s!=predictions]            # sprema sliku samo ako je kriva
mistakes_index=np.where(predictions!=y_test_s)      # sprema indexe gdje se slike ne poklapaju

print(len(mistakes))

print("Predviđanja:", predictions[:10])
print("Stvarne vrijednosti:", y_test_s[:10])

# Prikaz svih krivo predviđenih slika
#for i in range(len(mistakes_index[0])):

# Prikaz prvih 3 krivo predviđenih slika
for i in range(3):
    index = mistakes_index[0][i]
    plt.figure()
    plt.imshow(mistakes[i])
    plt.title("Stvarna vrijednost: " + str(y_test_s[index]) + ", Predviđeno: " + str(predictions[index]))
    plt.show()
