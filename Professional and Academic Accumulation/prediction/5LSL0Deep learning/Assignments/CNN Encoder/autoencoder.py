# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:46:22 2019


Load MNIST dataset and implement an autoencoder with only a few layers to do manifold learning

@author: rvulling
"""

import struct as st
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from IPython.display import clear_output
import math

import tensorflow as tf
from sklearn.metrics import accuracy_score
from tensorflow import keras
from tensorflow.keras.layers import Input, Dense, Conv2D, LeakyReLU, AvgPool2D, UpSampling2D, ReLU, MaxPooling2D, \
    Reshape, Softmax, Activation, Flatten, Lambda, Conv2DTranspose
from tensorflow.keras.losses import MSE, categorical_crossentropy, binary_crossentropy
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
import tensorflow.keras.backend as K  # 'generic' backend so code works with either tensorflow or theano

import sklearn
from sklearn.neighbors import NearestNeighbors

from tensorflow.keras.datasets import mnist
from tensorflow.python.framework.ops import disable_eager_execution

disable_eager_execution()

args = {
    'epochs': 10,
    'batch_size': 64
}


def build_batches(x, n):
    m = (x.shape[0] // n) * n
    return x[:m].reshape(-1, n, *x.shape[1:])


def get_mnist32_batches(batch_size, data_format='channels_last'):
    maxNum_data_train = 10000  # reduce data size for computational load
    maxNum_data_test = 1000
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()
    data_x_train = X_train.reshape(-1, 28, 28).astype(np.float32) / 255.
    data_x_test = X_test.reshape(-1, 28, 28).astype(np.float32) / 255.
    # Reduce dimensions of dataset to reduce computations times
    np.random.seed(42)  # seed to ensure reproducible results
    randomIndices_train = np.random.permutation(np.size(data_x_train, 0))
    randomIndices_test = np.random.permutation(np.size(data_x_test, 0))
    indicesTrain = randomIndices_train[0:maxNum_data_train]
    indicesTest = randomIndices_test[0:maxNum_data_test]
    data_x_train = data_x_train[indicesTrain, :, :]  # Reduce dimensions of dataset to reduce computations times
    data_x_train = np.pad(data_x_train, ((0, 0), (2, 2), (2, 2)), mode='constant')
    data_x_train = np.expand_dims(data_x_train, -1)
    data_x_test = data_x_test[indicesTest, :, :]
    data_x_test = np.pad(data_x_test, ((0, 0), (2, 2), (2, 2)), mode='constant')
    data_x_test = np.expand_dims(data_x_test, -1)
    data_y_train = Y_train[indicesTrain]  # Reduce dimensions of dataset to reduce computations times
    data_y_test = Y_test[indicesTest]  # Reduce dimensions of dataset to reduce computations times
    indices = np.arange(len(data_x_train))
    # np.random.shuffle(indices)
    y_batches = build_batches(data_y_train[indices], batch_size)
    x_batches = build_batches(data_x_train[indices], batch_size)

    return x_batches, y_batches, data_x_train, data_y_train, data_x_test, data_y_test


x_batches, y_batches, data_x_train, data_y_train, data_x_test, data_y_test = get_mnist32_batches(args['batch_size'])


def Encoder(input_shape):
    # ENCODER
    input_img = Input(shape=input_shape)
    enc_conv1 = Conv2D(16, (3, 3), activation='relu', padding='same')(input_img)
    enc_pool1 = MaxPooling2D((2, 2), padding='same')(enc_conv1)
    enc_conv2 = Conv2D(16, (3, 3), activation='relu', padding='same')(enc_pool1)
    enc_pool2 = MaxPooling2D((2, 2), padding='same')(enc_conv2)
    enc_conv3 = Conv2D(1, (3, 3), activation='relu', padding='same')(enc_pool2)
    encoded = MaxPooling2D((8, 4), padding='same')(enc_conv3)
    encoder = tf.keras.Model(inputs=input_img, outputs=encoded)
    return encoder


def Decoder(input_shape):
    # DECODER
    output_enc = Input(shape=input_shape)
    dec_conv1 = Conv2DTranspose(16, (3, 3), activation='relu', padding='same')(output_enc)
    dec_upsample1 = UpSampling2D((8, 4))(dec_conv1)
    dec_conv2 = Conv2DTranspose(16, (3, 3), activation='relu', padding='same')(dec_upsample1)
    dec_upsample2 = UpSampling2D((2, 2))(dec_conv2)
    dec_conv3 = Conv2DTranspose(16, (3, 3), activation='relu', padding='same')(dec_upsample2)
    dec_upsample3 = UpSampling2D((2, 2))(dec_conv3)
    decoded = Conv2DTranspose(1, (3, 3), activation='relu', padding='same')(dec_upsample3)
    decoder = tf.keras.Model(inputs=output_enc, outputs=decoded)
    return decoder


"""
Create models    
"""
input_shape = x_batches.shape[2:]
encoder = Encoder(input_shape)
input_shape = encoder.output_shape[1:]
decoder = Decoder(input_shape)

#
input_shape = x_batches.shape[2:]
inputs = Input(input_shape)
encoded = encoder(inputs)
decoded = decoder(encoded)
model = tf.keras.Model(inputs=inputs, outputs=decoded)
model.summary()

# model.compile('adam', loss= MSE)
model.compile('adam', loss=lambda yt, yp: MSE(inputs, decoded))

"""
 Train model or load weights of previously trained model
"""

# model.load_weights("AE_20200519.h5")
loss = []
for epoch in range(args['epochs']):
    print("epoch: ", epoch)
    for batch in x_batches:
        history = model.fit(x=batch, y=batch)
        loss.append(history.history['loss'])

# Plot the loss as a function of the number of epochs
plt.figure()
plt.plot(loss)
plt.xlabel('epochs')
plt.ylabel('loss')

# Predict the first batch's images of x_batches
decoded_images = np.zeros((1, 64, 32, 32, 1))
decoded_imgs = model.predict(x_batches[0, :, :, :])

# Show the fist 10 original images v.s. the predicted images
x_batches = x_batches[0, :, :, :]
n = 10
plt.figure(figsize=(20, 4))
for i in range(1, n + 1):
    # display original
    ax = plt.subplot(2, n, i)
    plt.imshow(x_batches[i - 1])
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    # display reconstruction
    ax = plt.subplot(2, n, i + n)
    plt.imshow(decoded_imgs[i - 1])
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()

# visualize the latent space
x_train_encoded = encoder.predict(data_x_train)
x_test_encoded = encoder.predict(data_x_test)
plt.figure(figsize=(10, 10))
plt.scatter(x_train_encoded[:, 0, 0, 0], x_train_encoded[:, 0, 1, 0], c=data_y_train, cmap='brg')
plt.scatter(x_test_encoded[:, 0, 0, 0], x_test_encoded[:, 0, 0, 0], c=data_y_test, cmap='brg')
plt.colorbar()
plt.show()

# 1-nearest neighbour search for encoded data_x_test
nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree')
nbrs.fit(x_test_encoded.reshape(1000, 1 * 2 * 1))
# accuracy = accuracy_score(data_y_test,x_test_encoded)
# print(accuracy)

