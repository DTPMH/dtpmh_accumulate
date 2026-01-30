"""
=============================================================================
    Eindhoven University of Technology
==============================================================================

    Source Name   : main.py
                    Main file for machine learning training
    Author        : Bart van Erp
    Modified by   : Nishith Chennakeshava
    Date          : 03/10/2019

==============================================================================
"""

# import libraries
import numpy as np
import h5py

# functions = __import__("Your submission file")
functions = __import__("backprop_example")


def SGD(theta, gradients, lr, depth):

    # loop through layers
    for k in range(depth):

        # update weights according to SGD
        theta["w"+str(k+1)] = theta["w"+str(k+1)] - lr*gradients["dJ_dw"+str(k+1)]
        theta["b"+str(k+1)] = theta["b"+str(k+1)] - lr*gradients["dJ_db"+str(k+1)]

    return theta


# parameters for training
nr_epochs = 5000
batch_size = 50
lr = 1e-4

# parameters for model
depth = 2

# load data
X = h5py.File('data.h5', 'r')['X']
y = h5py.File('data.h5', 'r')['y']

# initialize dictionary with all weigths
theta = {'w1': np.array([[-0.65497431, -1.64259778],
                         [0.49698371,  1.53797914]]),
         'w2': np.array([[1.85627443, -0.50453944]]),
         'b1': np.array([[0.20787364],
                         [-0.63470021]]),
         'b2': np.array([[-1.82343559]])}

# start training
print("start training...")
for epoch in range(nr_epochs):

    # loop through batches of data
    for batch in range(X.shape[1]//batch_size):

        # get batch of data
        X_batch = X[:, batch_size*batch:batch_size*(batch+1)]
        y_batch = y[:, batch_size*batch:batch_size*(batch+1)]

        # calculate gradients gradients
        J, yhat, gradients = functions.backprop(X_batch, y_batch, theta, depth)

        # update parameters
        theta = SGD(theta, gradients, lr, depth)

    # print update
    print("epoch %3.0f: loss = %f" % (epoch+1, J))
