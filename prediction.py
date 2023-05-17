import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

def pred(img):
    # print(data)
    df = pd.DataFrame.from_dict(data,orient="index")
    df=df.T
    model = tf.keras.models.load_model('my_model')