# First, install Keras Tuner
# !pip install -q -U keras-tuner
import tensorflow as tf
from tensorflow import keras
import kerastuner as kt
from keras_tuner import *

mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Building model with iterative search
def model_builer(hp):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
    # This we using Hyperparameters Tunner
    hp_units = hp.Int('units', min_value=16, max_value=512,step=16)
    model.add(tf.keras.layers.Dense(units=hp_units, activation='relu'))

    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(10))
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
    return model

# Search strategy
tuner = kt.Hyperband(model_builer,
                     objective='val_accuracy',
                     max_epochs=10,
                     factor=3,
)
# Callback conﬁguration
stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                              patience=5)
tuner.search(x_train,
             y_train, 
             epochs=50, 
             validation_split=0.2, 
             callbacks=[stop_early])