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
from IPython.display import clear_output
import math

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Input, Dense, Conv2D, LeakyReLU, AvgPool2D, UpSampling2D, ReLU, MaxPooling2D, Reshape, Softmax, Activation, Flatten, Lambda, Conv2DTranspose
from tensorflow.keras.losses import MSE, categorical_crossentropy, binary_crossentropy
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import Adam
import tensorflow.keras.backend as K

import sklearn
from sklearn.neighbors import NearestNeighbors

from tensorflow.keras.datasets import mnist


args = {
    'epochs': 10,    
    'batch_size': 64
}


def build_batches(x, n):
    m = (x.shape[0] // n) * n
    return x[:m].reshape(-1, n, *x.shape[1:])

def get_mnist32_batches(batch_size, data_format='channels_last'):
    maxNum_data_train=10000 #reduce data size for computational load
    maxNum_data_test=1000    
    (X_train, Y_train), (X_test, Y_test) = mnist.load_data()       
    data_x_train = X_train.reshape(-1,28,28).astype(np.float32) / 255.
    data_x_test = X_test.reshape(-1,28,28).astype(np.float32) / 255.    
    
    #Reduce dimensions of dataset to reduce computations times
    np.random.seed(42) #seed to ensure reproducible results
    randomIndices_train=np.random.permutation(np.size(data_x_train,0))
    randomIndices_test=np.random.permutation(np.size(data_x_test,0))
    indicesTrain=randomIndices_train[0:maxNum_data_train]
    indicesTest=randomIndices_test[0:maxNum_data_test]
    data_x_train=  data_x_train[indicesTrain,:,:] #Reduce dimensions of dataset to reduce computations times
    data_x_train = np.pad(data_x_train, ((0,0), (2,2), (2,2)), mode='constant')
    data_x_train = np.expand_dims(data_x_train, -1)
    data_x_test = data_x_test[indicesTest,:,:]
    data_x_test = np.pad(data_x_test, ((0,0), (2,2), (2,2)), mode='constant')
    data_x_test = np.expand_dims(data_x_test, -1)    
    data_y_train=Y_train[indicesTrain] #Reduce dimensions of dataset to reduce computations times
    data_y_test=Y_test[indicesTest] #Reduce dimensions of dataset to reduce computations times
    indices = np.arange(len(data_x_train))
    #np.random.shuffle(indices)
    y_batches = build_batches(data_y_train[indices], batch_size)
    x_batches = build_batches(data_x_train[indices], batch_size)
    return x_batches, y_batches, data_x_train, data_y_train, data_x_test, data_y_test

x_batches, y_batches, data_x_train, data_y_train, data_x_test, data_y_test = get_mnist32_batches(args['batch_size'])

def Encoder(input_shape):
    #ENCODER


    
    
def Decoder(input_shape):
    #DECODER
    
    
    
    
    
    
    
    
"""
Create models    
"""
input_shape = x_batches.shape[2:]
encoder=Encoder(input_shape)
input_shape=encoder.output_shape[1:]
decoder=Decoder(input_shape)

input_shape=x_batches.shape[2:]
inputs=Input(input_shape)
encoded=encoder(inputs)
decoded=decoder(encoded)
model=tf.keras.Model(inputs=inputs,outputs=decoded)

#model.compile('adam', loss= MSE)
model.compile('adam', loss=lambda yt,yp: MSE(inputs, decoded))


"""
Train model or load weights of previously trained model
"""

# model.load_weights("AE_20200519.h5")
for epoch in range(args['epochs']):
    print("epoch: ",epoch)
    for batch in x_batches:
 

