import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import numpy as np

def pred(img):
    # print(data)
    model = tf.keras.models.load_model('my_model\my_model')
    preds = model.predict(img, verbose=1)
    predicted_class_indices=np.argmax(preds,axis=1)
    return predicted_class_indices[0]
