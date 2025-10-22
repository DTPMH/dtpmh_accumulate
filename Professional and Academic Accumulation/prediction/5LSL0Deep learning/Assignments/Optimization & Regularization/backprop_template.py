import numpy as np

"""
=============================================================================
    Eindhoven University of Technology
==============================================================================

    Source Name   : {First name}-{Last name}-{student ID}.py
                    Use underscores '_' when your first/last name consists out
                    of multiple parts.
                    e.g.
                        Tim-de_Jong-0123456.py
                        Pieter-Jansen-2589631.py
    Author        : ...
    Date          : ...

==============================================================================
"""


"""
==============================================================================
                        Assignment backpropagation
==============================================================================
1.  Fill in your personal details at the top of the script and adjust the name
    of the script to specified format.

2.  Complete the functions at the bottom of the script for the Dense layer
    and the ReLU and Sigmoid activation layers.

3.  Complete the functions at the bottom of the script that calculate the
    derivatives of the ReLU and Sigmoid activation layers.

4.  Complete the functions that calculate the BCE and its
    derivative.

5.  Implement the forward pass of the backpropagation algorithm.

6.  Implement the backwards pass of the backpropagation algorithm.


Keep the following points in mind:
    - Do not import additional libraries besides numpy.
    - Do not create additional functions in this script.
    - Do not change the names of the functions or their input/output arguments.
    - You are highly encouraged to test your script using a toy example.
    - The outline of the algorithm is based on algorithm 6.3 and 6.4 at
      http://www.deeplearningbook.org/contents/mlp.html.
"""


# import libraries


"""
==============================================================================
                        Backpropagation algorithm
==============================================================================
"""


def backprop(X, y, theta, depth):

    # perform a forward pass
    J, p, h, a = forward_pass(X, y, theta, depth)

    # perform a backwards pass
    gradients = backwards_pass(y, theta, h, a)

    return J, p, gradients


def forward_pass(X, y, theta, depth):
    """
    This function performs the forward pass of the backpropagation algorithm.

    Input:  X -     Input of the network
            y -     Ground-truth output of the network
            theta - Dictionary containing all estimated weights "w" and biases
                    "b" of the network. The naming convention is from "w1" or
                    "b1" up to and including "w{depth}" or "b{depth}", without
                    brackets
            depth - Integer denoting the depth of the network. An additional
                    depth of 1 results in 1 additional Dense layer
                    consecutively 1 additional ReLU layer. The last Dense layer
                    does not have an activation function
    Output: J -     Value of the cost function as a float.
            p -     Estimated output of the network as an numpy array with
                    the same dimensionality as input 'y'.
            h -     Dictionary of the intermediate outputs as numpy arrays at
                    the inputs of Dense layers and of the final output. The
                    naming convention is from "h0" up to and including
                    "h{depth}", without brackets
            a -     Dictionary of the intermediate outputs as numpy arrays at
                    the inputs of activation layers and of the final output.
                    The naming convention is from "a1" up to and including
                    "a{depth}", without brackets
    """

    # create the initial dictionary 'h' with as key "h0", corresponding to X
    ...

    # create the initial dictionary 'a' without any entries
    ...

    # loop through layers
    for k in ...:

        # calculate the next output after another Dense layer and append this
        # to the dictionary 'a' using the key "a{index}" without brackets and
        # by choosing the appropriate index according to algorithm 6.3 at
        # http://www.deeplearningbook.org/contents/mlp.html
        # important:    use the previously defined Dense function in the
        #               calculation!
        ...

        # calculate the next output after another activation layer and append
        # this to the dictionary 'h' using the key "h{index}" without brackets
        # and by choosing the appropriate index according to algorithm 6.3 at
        # http://www.deeplearningbook.org/contents/mlp.html
        # important:    use the previously defined ReLU/Sigmoid function in the
        #               calculation!
        ...

    # determine the value of 'p', which is the estimated output
    ...

    # calculate the cost function 'J' (= BCE between the
    # ground-truth 'y' and the estimated output 'p')
    # important:    use the previously defined BCE function in the
    #               calculation!
    ...

    # return the cost function 'J', the estimated output 'p', and the
    # intermediate outputs 'h' and 'a'
    return J, p, h, a


def backwards_pass(y, theta, h, a):
    """
    This function performs the backwards pass of the backpropagation algorithm.

    Input:  y -     Ground-truth output of the network as an numpy array.
            theta - Dictionary containing all estimated weights "w" and biases
                    "b" of the network. The naming convention is from "w1" or
                    "b1" up to and including "w{depth}" or "b{depth}", without
                    brackets
            h -     Dictionary of the intermediate outputs at the inputs of
                    Dense layers and of the final output. The naming convention
                    is from "h0" up to and including "h{depth}", without
                    brackets
            a -     Dictionary of the intermediate outputs at the inputs of
                    activation layers and of the final output. The naming
                    convention is from "a1" up to and including "a{depth}",
                    without brackets
    Output: gradients - Dictionary containing the gradients of the cost
                        function with respect to the weights. The dictionary
                        should have the following keys: "dJ_dw{k}" and
                        "dJ_db{k}" for k = 1:depth without brackets. Tip:
                        make sure that the shapes of the calculated gradients
                        are numpy arrays that correspond with the shapes of
                        the weights.
    """

    # initialize an empty dictionary for the gradients called 'gradients'
    ...

    # compute the gradient 'g' on the output layer, i.e. the gradient of the
    # cost function with respect to the estimated output
    # important:    use the previously defined dBCE_dphat function in the
    #               calculation!
    ...

    # loop through all layers in a backwards manner
    for k in ...:

        # convert the gradient on the layer's output into a gradient on the
        # previous activation function. Keep in mind that the last layer does
        # not have an ReLU activation layer and therefore this step can be
        # omitted. You can just update the value of 'g'
        # important:    use the previously defined dReLU_da function in the
        #               calculation!
        ...

        # compute the gradients on the weights and biases of the previous Dense
        # layer and save them in the dictionary 'gradients' with the syntax as
        # specified above. Keep in mind that the derivative of dJ_db can be
        # calculated as dJ_da * da_db, where the second term is neglected in
        # the algorithm 6.4. However, for a correct operation, this term should
        # be determined in order to obtain a gradient with an adequate shape.
        ...

        # propagate the gradient 'g' with respect to the next lower-level
        # activations functions and update 'g'
        ...

    # return gradients
    return gradients


"""
==============================================================================
                        Cost function and derivative
==============================================================================
"""


def BCE(y, p):
    """
    This function returns the Binary Cross Entropy of the ground-truth 'y' and
    the estimated value 'p'.

    Input:  y -     Ground-truth output of the network, which is an arbitrarily
                    shaped Numpy array containing only real values
            p -     Estimated output of the network, which is an arbitrarily
                    shaped Numpy array containing only real values
    Output: bce -   Binary Cross Entropy of the ground-truth 'y' and the
                    estimated value 'p' as a single float
    """
    # calculate binary cross entropy

    # return BCE
    return bce


def dBCE_dphat(y, p):
    """
    This function returns the derivative of the Binary Cross Entropy of the
    ground-truth 'y' and the estimated value 'p' with respect to the
    estimated value 'p'.

    Input:  y -             Ground-truth output of the network, which is an
                            arbitrarily shaped Numpy array containing only real
                            values
            p -             Estimated output of the network, which is an
                            arbitrarily shaped Numpy array containing only real
                            values
    Output: dbce_dphat -    Derivative of the binary cross entropy of the
                            ground-truth 'y' and the estimated value 'phat'
                            with respect to the estimated value 'phat' as an
                            Numpy array containing only real values with the
                            same shape as the estimated value 'phat'
    """
    # calculate derivative of BCE

    # return derivative of BCE
    return dbce_dphat


"""
==============================================================================
                Derivatives of layers and activation functions
==============================================================================
"""


def dReLU_da(a):
    """
    This function returns the derivative of the output 'h' of a Rectified
    Linear Unit with respect to the input 'a'.

    Input:  a -     Input of the Rectified Linear Unit, which is an arbitrarily
                    shaped Numpy array containing only real values
    Output: dh_da - Derivative of the output 'h' of a Rectified Linear Unit
                    with respect to the input 'a' formatted as a Numpy array
                    containing only real values with the same shape as input
                    'a'
    """
    # calculate dh_da
    ...

    # return dh_da
    return dh_da


def dSigmoid_da(a):
    """
    This function returns the derivative of the output 'h' of a Sigmoidal
    activation layer with respect to the input 'a'.

    Input:  a -     Input of the Sigmoidal activation layer, which is an
                    arbitrarily shaped Numpy array containing only real values
    Output: dh_da - Derivative of the output 'h' of a Sigmoidal activation
                    layer with respect to the input 'a' formatted as a Numpy
                    array containing only real values with the same shape as
                    input 'a'
    """
    # calculate dh_da
    ...

    # return dh_da
    return dh_da


"""
==============================================================================
                        Layers and activation functions
==============================================================================
"""


def Dense(h, w, b):
    """
    This function returns the output of a Dense layer with bias.

    Input:  h - Input of the Dense layer formatted as a Numpy array containing
                only real values with shape (M x N)
            w - Linear weights of the Dense layer formatted as a Numpy array
                containing only real values with shape (K x M)
            b - Bias weights of the Dense layer formatted as a Numpy array
                containing only real values with shape (...)
    Output: a - Output of the Dense layer formatted as a Numpy array containing
                only real values with 2D shape (...)
    """
    # calculate a
    ...

    # return a
    return a


def ReLU(a):
    """
    This function returns the output of a Rectified Linear Unit.

    Input:  a - Input of the Rectified Linear Unit, which is an arbitrarily
                shaped Numpy array containing only real values
    Output: h - Output of the Rectified Linear Unit, which is a Numpy array
                with the same shape as input 'a'
    """
    # calculate h
    ...

    # return h
    return h


def Sigmoid(a):
    """
    This function returns the output of a Sigmoidal activation layer.

    Input:  a - Input of the Sigmoidal activation layer, which is an
                arbitrarily shaped Numpy array containing only real values
    Output: h - Output of the Sigmoidal activation layer, which is a Numpy
                array with the same shape as input 'a'
    """
    # calculate h
    ...

    # return h
    return h
