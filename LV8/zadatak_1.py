import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


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

# Koliko primjera sadrži skup za ucenje, a koliko skup za testiranje? 
print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)




# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu

model=keras.Sequential()
model.add( layers.Flatten(input_shape=input_shape))
model.add( layers.Dense(100, activation ="relu"))
model.add( layers.Dense(50, activation ="relu"))
model.add( layers.Dense(10, activation ="softmax"))
model.summary()

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile ( loss = "categorical_crossentropy" , optimizer = "adam", metrics = ["accuracy"])


# TODO: provedi ucenje mreze
batch_size = 32
epochs = 5
history = model.fit ( x_train_s, y_train_s, batch_size = batch_size, epochs = epochs, validation_split = 0.1)    # pazi na skalirane vrijednosti



# TODO: Prikazi test accuracy i matricu zabune
predictions = model.predict(x_test_s)
score = model.evaluate( x_test_s , y_test_s , verbose = 0 )
print(score[1])


# transformacija iz 2D u 1D polje s indexima najvećih vrijednosti
y_test_s = np.argmax(y_test_s,axis=1)          # u numpy je axis=1 za red
predictions = np.argmax(predictions, axis=1)    

# predictions=np.around(predictions).astype(np.int32) 


disp = ConfusionMatrixDisplay ( confusion_matrix ( y_test_s, predictions ))
disp.plot()
plt.show()


# TODO: spremi model

model.save ("FCN/")

