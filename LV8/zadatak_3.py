import numpy as np
import tensorflow as tf
from tensorflow import keras
from matplotlib import pyplot as plt

model = keras.models.load_model('FCN/')

image = tf.keras.utils.load_img('test1.png', color_mode="grayscale", target_size=(28, 28))

image_arr = np.array(image)
image_arr = image_arr.astype("float32")/255
image_arr = np.expand_dims(image_arr, -1)
image_arr = np.reshape(image_arr, (1, 28, 28, 1))  # batch_size, height and width, number of channels

prediction = model.predict(image_arr)

print('Vrijednosti mogućnosti izlaza:',prediction)
prediction_class = np.argmax(prediction)
print("Predviđena vrijednost:", prediction_class)
print("Stvarna vrijednost: 0")