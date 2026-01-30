"""
=============================================================================
    Eindhoven University of Technology
==============================================================================

    Source Name   : optimization_test_script.py
                    Main file for machine learning training
    Author        : Bart van Erp
    Modified by   : Nishith Chennakeshava
    Date          : 03/10/2019

==============================================================================
"""

# import libraries
import numpy as np
import h5py

optimizer = __import__("optimisation_example")
backprop = __import__("backprop_example")

# parameters for training
nr_epochs = 5000
batch_size = 100

# parameters for model
depth = 2

# load data
X = h5py.File('data.h5', 'r')['X']
y = h5py.File('data.h5', 'r')['y']

# initialize dictionary with all weigths
theta_init = {**{"w{}".format(i+1): np.random.randn(2, 2) for i in range(depth-1)},
              "w{}".format(depth): np.random.randn(1, 2),
              **{"b{}".format(i+1): np.random.randn(2, 1) for i in range(depth-1)},
              "b{}".format(depth): np.random.randn(1, 1)}

theta = {'w1': np.array([[-0.65497431, -1.64259778],
                         [0.49698371,  1.53797914]]),
         'w2': np.array([[1.85627443, -0.50453944]]),
         'b1': np.array([[0.20787364],
                         [-0.63470021]]),
         'b2': np.array([[-1.82343559]])}

# create optimizer class
opt = optimizer.optimizer(theta_init, depth)

# specify optimizer
opt.specify_optimizer("Adam", parameters={"lr": 0.0001, "delta": 1e-12, "rho1": 0.9, "rho2": 0.999})

# start training
print("start training...")
for epoch in range(nr_epochs):

    # loop through batches of data
    for batch in range(X.shape[1]//batch_size):

        # get batch of data
        X_batch = X[:, batch_size*batch:batch_size*(batch+1)]
        y_batch = y[:, batch_size*batch:batch_size*(batch+1)]

        # calculate gradients
        J, yhat, gradients = backprop.backprop(X_batch, y_batch, opt.theta, depth)
        gradients = optimizer.regularizer(gradients, opt.theta, 'l1', 0.1)

        # update parameters
        opt.optimize_weights(gradients)

    # print update
    print("epoch %3.0f: loss = %f" % (epoch+1, J))
