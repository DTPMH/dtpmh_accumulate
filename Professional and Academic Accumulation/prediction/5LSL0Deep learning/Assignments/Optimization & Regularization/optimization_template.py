import numpy as np
from copy import deepcopy

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
                        Assignment optimization
==============================================================================
1.  Fill in your personal details at the top of the script and adjust the name
    of the script to specified format.

2.  Complete the __init__() and reset_weights() functions.

3.  Complete the specify_optimizer() and optimize_weights() functions.

4.  Complete the functions corresponding to the optimization algorithms:
    "SGD", "SGDmomentum", "AdaGrad", "RMSprop", "Adam"

5.  Complete regularizer function.

Keep the following points in mind:
    - Do not import additional libraries besides numpy.
    - Do not create additional functions in this script.
    - Do not change the names of the functions or their input/output arguments.
    - You are highly encouraged to test your script using a toy example.
"""


# import libraries


"""
==============================================================================
                        Optimization algorithms
==============================================================================
"""


def regularizer(gradients, theta, regtype, reglambda):
    """
    This function updates the gradients as calculated by the backpropagation
    algorithm by adding a regularization term.

    Input:  gradients -     Dictionary containing all current gradients of
                            weights "w" and biases "b" of the network.
                            The naming convention is from "w1" or "b1"
                            up to and including "dJ_dw{depth}" or
                            "dJ_db{depth}", without brackets.
            theta -         Dictionary containing all current estimated
                            weights "w" and biases "b" of the network.
                            The naming convention is from "w1" or "b1"
                            up to and including "w{depth}" or
                            "b{depth}", without brackets.
            regtype -       String containing the type of regularization. This
                            can be one of the following types:
                            "none", "l1", "l2"
            reglambda -     Regularization parameter.

    Output: gradientsreg -  Dictionary containing all regularized gradients of
                            weights "w" and biases "b" of the network.
                            The naming convention is from "w1" or "b1"
                            up to and including "dJ_dw{depth}" or
                            "dJ_db{depth}", without brackets.
    """

    # copy gradients dictionary to a new dictionary gradientsreg, which will
    # be adopted according to the chosen regularization. (keep in mind that
    # copying dictionaries is not the same as copying variables! Use the
    # imported deepcopy function for this purpose)
    gradientsreg = ...

    # check if regularization type is "l1"
    if ...:

        # loop through gradients
        for key in ...:

            # update regularized gradients
            gradientsreg[key] = ...

    # check if regularization type is "l2
    elif ...:

        # loop through gradients
        for key in ...:

            # update regularized gradients
            gradientsreg[key] = ...

    return gradientsreg


class optimizer():
    """
    The optimizer class can be regarded as an object which contains both data
    and functions. The data of this class can be accessed using the dot
    notation (optimizer.variable) and the function similarly as
    (optimizer.function()). Within the functions of the class, internal
    variables and functions can be accessed from the self object.

    This class will save a copy of the initial parameters, the current
    parameters and can deal with updating the parameters using the accompanied
    backpropagation function.
    """

    def __init__(self, theta_init, depth):
        """
        The __init__() function is called when a class is initialized in a
        script. Calling 'opt = optimizer(theta_init, depth)' will create the
        optimizer class called 'opt'. The self variable (refering to the
        class itself) does not need to be supplied, but can be accessed in
        the internal functions.

        This init function requires the initial parameter values of the Dense
        layers and the depth of the network.

        Input:  self -          The class itself. This variable is required in
                                the function definition, but should not be
                                supplied when calling the function.
                theta_init -    Dictionary containing all initial weights "w"
                                and biases "b" of the network. The naming
                                convention is from "w1" or "b1" up to and
                                including "w{depth}" or "b{depth}", without
                                brackets.
                depth -         Integer denoting the depth of the network. An
                                additional depth of 1 results in 1 additional
                                Dense layer consecutively 1 additional ReLU
                                layer. The last Dense layer does not have an
                                activation function.

        Output: self.depth -        Integer denoting the depth of the network.
                                    An additional depth of 1 results in 1
                                    additional Dense layer consecutively 1
                                    additional ReLU layer. The last Dense layer
                                    does not have an activation function.
                self.theta_init -   Dictionary containing all initial weights
                                    "w" and biases "b" of the network. The
                                    naming convention is from "w1" or "b1" up
                                    to and including "w{depth}" or "b{depth}",
                                    without brackets.
                self.theta -        Dictionary containing all current estimated
                                    weights "w" and biases "b" of the network.
                                    The naming convention is from "w1" or "b1"
                                    up to and including "w{depth}" or
                                    "b{depth}", without brackets. This variable
                                    should be initialized with the initial
                                    weights of the network.

        Note:   self.variables should not be returned since they can be
                accessed from the class itself.
        """

        # create the class variable depth by copying the same passed input
        # variable
        self.depth = ...

        # create the class variable theta_init by copying the same passed
        # input argument (keep in mind that copying dictionaries is not the
        # same as copying variables! Use the imported deepcopy
        # function for this purpose)
        self.theta_init = ...

        # create the class variable theta by initializing it with the initial
        # passed values of theta_init (keep in mind that copying dictionaries
        # is not the same as copying variables! Use the imported deepcopy
        # function for this purpose)
        self.theta = ...

    def reset_weights(self):
        """
        Resets the dictionary containing the weights of the model to the
        initial weights as specified during the creation of the class.

        Input:  self -          The class itself. This variable is required in
                                the function definition, but should not be
                                supplied when calling the function.

        Output: self.theta -        Dictionary containing all current estimated
                                    weights "w" and biases "b" of the network.
                                    The naming convention is from "w1" or "b1"
                                    up to and including "w{depth}" or
                                    "b{depth}", without brackets. This variable
                                    should be initialized with the initial
                                    weights of the network.

        Note:   self.variables should not be returned since they can be
                accessed from the object itself.
        """

        # reset the dictionary containing the model weights by resetting them
        # to the initial values. (Hint: recall that self.theta_init contains
        # the initial model weights)
        self.theta = ...

    def specify_optimizer(self, algorithm, parameters):
        """
        Input:  self -          The class itself. This variable is required in
                                the function definition, but should not be
                                supplied when calling the function.
                algorithm -     String specifying one of the optimization
                                algorithms. This supplied string should be
                                specified as one of the following:
                                {"SGD", "SGDmomentum", "AdaGrad", "RMSprop",
                                 "Adam"}
                parameters -    Dictionary with hyperparameters depending on
                                optimization algorithm. The entries consist
                                out of a string specifying the hyperparameter
                                and its corresponding value. The required
                                hyperparameters per optimization algorithm are:
                                SGD -           "lr" -      learning rate
                                SGDmomentum -   "lr" -      learning rate
                                                "rho" -     forgetting factor
                                AdaGrad -       "lr" -      learning rate
                                RMSprop -       "lr" -      learning rate
                                                "rho" -     forgetting factor
                                Adam -          "lr" -      learning rate
                                                "rho1" -    forgetting factor
                                                            first moment
                                                "rho2" -    forgetting factor
                                                            second moment

        Output: self.algorithm -    String specifying one of the optimization
                                    algorithms. This supplied string should be
                                    specified as one of the following:
                                    {"SGD", "SGDmomentum", "AdaGrad",
                                     "RMSprop", "Adam"}
                self.parameters -   Dictionary with hyperparameters depending
                                    on optimization algorithm. The entries
                                    consist out of a string specifying the
                                    hyperparameter and its corresponding value.
                                    The required hyperparameters per
                                    optimization algorithm are:
                                SGD -           "lr" -      learning rate
                                SGDmomentum -   "lr" -      learning rate
                                                "rho" -     forgetting factor
                                AdaGrad -       "lr" -      learning rate
                                                "delta" -   small constant to
                                                            prevent division
                                                            by zero
                                RMSprop -       "lr" -      learning rate
                                                "rho" -     forgetting factor
                                                "delta" -   small constant to
                                                            prevent division
                                                            by zero
                                Adam -          "lr" -      learning rate
                                                "rho1" -    forgetting factor
                                                            first moment
                                                "rho2" -    forgetting factor
                                                            second moment
                                                "delta" -   small constant to
                                                            prevent division
                                                            by zero
        Note:   self.variables should not be returned since they can be
                accessed from the class itself.
        """

        # create the class variable 'algorithm' specifying the algorithm used
        # as a string
        self.algorithm = ...

        # create the class variable 'parameters' containing the dictionary with
        # hyperparameters passed to function (keep in mind that copying
        # dictionaries is not the same as copying variables! Use the imported
        # deepcopy function for this purpose)
        self.parameters = ...

    def optimize_weights(self, gradients):
        """
        Calls the function specified by the algorithm to optimize the weights.

        Input:  self -          The class itself. This variable is required in
                                the function definition, but should not be
                                supplied when calling the function.
                gradients -     Dictionary containing all current gradients of
                                weights "w" and biases "b" of the network.
                                The naming convention is from "w1" or "b1"
                                up to and including "dJ_dw{depth}" or
                                "dJ_db{depth}", without brackets.

        Output: self.theta -        Dictionary containing all current estimated
                                    weights "w" and biases "b" of the network.
                                    The naming convention is from "w1" or "b1"
                                    up to and including "w{depth}" or
                                    "b{depth}", without brackets.

        Note:   self.variables should not be returned since they can be
                accessed from the class itself.
        """

        # create an if-elif-...-else statement where the self.algorithm
        # variable is compared against all of its possible values {"SGD",
        # "SGDmomentum", "AdaGrad", "RMSprop", "Adam"} and calls the
        # corresponding optimizer function as defined below.

        # check if the specified algorithm is "SGD"
        if ...:

            # call the "SGD" optimizer
            ...

        # check if the specified algorithm is "SGDmomentum"
        elif ...:

            # call the "SGDmomentum" optimizer
            ...

        # check if the specified algorithm is "AdaGrad"
        elif ...:

            # call the "Adagrad" optimizer
            ...

        # check if the specified algorithm is "RMSprop"
        elif ...:

            # call the "RMSprop" optimizer
            ...

        # check if the specified algorithm is "Adam"
        elif ...:

            # call the "Adam" optimizer
            ...

    def SGD(self, gradients):
        """
        Calls the steepest gradient descent optimization algorithm.

        Input:  self -          The class itself. This variable is required in
                                the function definition, but should not be
                                supplied when calling the function.
                gradients -     Dictionary containing all current gradients of
                                weights "w" and biases "b" of the network.
                                The naming convention is from "w1" or "b1"
                                up to and including "dJ_dw{depth}" or
                                "dJ_db{depth}", without brackets.

        Output: self.theta -    Dictionary containing all current estimated
                                weights "w" and biases "b" of the network.
                                The naming convention is from "w1" or "b1" up
                                to and including "w{depth}" or "b{depth}",
                                without brackets.

        Note:   self.variables should not be returned since they can be
                accessed from the class itself.
        """

        # loop throught the dictionary of weigths
        for key in ...:

            # update weights (access the hyperparameters, e.g. learning rate,
            # through the specified 'self.parameters')
            self.theta[key] = ...

    def SGDmomentum(self, gradients):
        """
        Calls the steepest gradient descent optimization algorithm with
        momentum.

        Input:  self -          The class itself. This variable is required in
                                the function definition, but should not be
                                supplied when calling the function.
                gradients -     Dictionary containing all current gradients of
                                weights "w" and biases "b" of the network.
                                The naming convention is from "dJ_dw1" or
                                "dJ_b1" up to and including "dJ_dw{depth}" or
                                "dJ_db{depth}", without brackets.

        Output: self.theta -    Dictionary containing all current estimated
                                weights "w" and biases "b" of the network.
                                The naming convention is from "w1" or "b1" up
                                to and including "w{depth}" or "b{depth}",
                                without brackets.
                self.acc1 -     Dictionary containing the accumulated first
                                order moment of weights "w" and biases "b" of
                                the network. The naming convention is
                                similar to the weights dictionary and the
                                keys start from "w1" or "b1" up to and
                                including "w{depth}" or "b{depth}",
                                without brackets.

        Note:   self.variables should not be returned since they can be
                accessed from the class itself.
        """

        # check if the variable 'self.acc1' exists, else create the variable
        # as a dictionary with keys indentical to the weights dictionary, but
        # with all values in the matrices set to 0.
        if ...:

            # create the dict 'self.acc1' with keys identical to the weights
            # dictionary (keep in mind that copying dictionaries is not the
            # same as copying variables! Use the imported deepcopy
            # function for this purpose)
            self.acc1 = ...

            # initialize all values to similarly sized matrices of zeros
            for key in ...:
                self.acc1[key] = ...

        # loop throught the dictionary of weigths
        for key in ...:

            # update accumulated first order moment (access the
            # hyperparameters, e.g. learning rate, through the specified
            # 'self.parameters')
            self.acc1[key] = ...

            # update weights (access the hyperparameters, e.g. learning rate,
            # through the specified 'self.parameters')
            self.theta[key] = ...

    def AdaGrad(self, gradients):
        """
        Calls the Adagrad optimization algorithm

        Input:  self -          The class itself. This variable is required in
                                the function definition, but should not be
                                supplied when calling the function.
                gradients -     Dictionary containing all current gradients of
                                weights "w" and biases "b" of the network.
                                The naming convention is from "dJ_dw1" or
                                "dJ_b1" up to and including "dJ_dw{depth}" or
                                "dJ_db{depth}", without brackets.

        Output: self.theta -    Dictionary containing all current estimated
                                weights "w" and biases "b" of the network.
                                The naming convention is from "w1" or "b1" up
                                to and including "w{depth}" or "b{depth}",
                                without brackets.
                self.accs1 -    Dictionary containing the accumulated squared
                                first order moment of weights "w" and biases
                                "b" of the network. The naming convention is
                                similar to the weights dictionary and the
                                keys start from "w1" or "b1" up to and
                                including "w{depth}" or "b{depth}",
                                without brackets.

        Note:   self.variables should not be returned since they can be
                accessed from the class itself.
        """

        # check if the variable 'self.accs1' exists, else create the variable
        # as a dictionary with keys indentical to the weights dictionary, but
        # with all values in the matrices set to 0.
        if ...:

            # create the dict 'self.accs1' with keys identical to the weights
            # dictionary (keep in mind that copying dictionaries is not the
            # same as copying variables! Use the imported deepcopy
            # function for this purpose)
            self.accs1 = ...

            # initialize all values to similarly sized matrices of zeros
            for key in ...:
                self.accs1[key] = ...

        # loop throught the dictionary of weigths
        for key in ...:

            # update accumulated squared first order moment
            self.accs1[key] = ...

            # update weights (access the hyperparameters, e.g. learning rate,
            # through the specified 'self.parameters')
            self.theta[key] = ...

    def RMSprop(self, gradients):
        """
        Calls the RMSprop optimization algorithm

        Input:  self -          The class itself. This variable is required in
                                the function definition, but should not be
                                supplied when calling the function.
                gradients -     Dictionary containing all current gradients of
                                weights "w" and biases "b" of the network.
                                The naming convention is from "dJ_dw1" or
                                "dJ_b1" up to and including "dJ_dw{depth}" or
                                "dJ_db{depth}", without brackets.

        Output: self.theta -    Dictionary containing all current estimated
                                weights "w" and biases "b" of the network.
                                The naming convention is from "w1" or "b1" up
                                to and including "w{depth}" or "b{depth}",
                                without brackets.
                self.accs1 -    Dictionary containing the accumulated squared
                                first order moment of weights "w" and biases
                                "b" of the network. The naming convention is
                                similar to the weights dictionary and the
                                keys start from "w1" or "b1" up to and
                                including "w{depth}" or "b{depth}",
                                without brackets.

        Note:   self.variables should not be returned since they can be
                accessed from the class itself.
        """

        # check if the variable 'self.accs1' exists, else create the variable
        # as a dictionary with keys indentical to the weights dictionary, but
        # with all values in the matrices set to 0.
        if ...:

            # create the dict 'self.accs1' with keys identical to the weights
            # dictionary (keep in mind that copying dictionaries is not the
            # same as copying variables! Use the imported deepcopy
            # function for this purpose)
            self.accs1 = ...

            # initialize all values to similarly sized matrices of zeros
            for key in ...:
                self.accs1[key] = ...

        # loop throught the dictionary of weigths
        for key in ...:

            # update accumulated squared first order moment
            self.accs1[key] = ...

            # update weights (access the hyperparameters, e.g. learning rate,
            # through the specified 'self.parameters')
            self.theta[key] = ...

    def Adam(self, gradients):
        """
        Calls the Adam optimization algorithm

        Input:  self -          The class itself. This variable is required in
                                the function definition, but should not be
                                supplied when calling the function.
                gradients -     Dictionary containing all current gradients of
                                weights "w" and biases "b" of the network.
                                The naming convention is from "dJ_dw1" or
                                "dJ_b1" up to and including "dJ_dw{depth}" or
                                "dJ_db{depth}", without brackets.

        Output: self.theta -    Dictionary containing all current estimated
                                weights "w" and biases "b" of the network.
                                The naming convention is from "w1" or "b1" up
                                to and including "w{depth}" or "b{depth}",
                                without brackets.
                self.acc1 -     Dictionary containing the accumulated
                                first order moment of weights "w" and biases
                                "b" of the network. The naming convention is
                                similar to the weights dictionary and the
                                keys start from "w1" or "b1" up to and
                                including "w{depth}" or "b{depth}",
                                without brackets.
                self.acc1b -    Dictionary containing the bias corrected
                                accumulated first order moment of weights "w"
                                and biases "b" of the network. The naming
                                convention is similar to the weights
                                dictionary and the keys start from "w1" or
                                "b1" up to and including "w{depth}" or
                                "b{depth}", without brackets.
                self.acc2 -     Dictionary containing the accumulated
                                second order moment of weights "w" and biases
                                "b" of the network. The naming convention is
                                similar to the weights dictionary and the
                                keys start from "w1" or "b1" up to and
                                including "w{depth}" or "b{depth}",
                                without brackets.
                self.acc2b -    Dictionary containing the bias corrected
                                accumulated second order moment of weights "w"
                                and biases "b" of the network. The naming
                                convention is similar to the weights
                                dictionary and the keys start from "w1" or
                                "b1" up to and including "w{depth}" or
                                "b{depth}", without brackets.
                self.count -    Counter (integer) indicating the amount of
                                updates performed.

        Note:   self.variables should not be returned since they can be
                accessed from the class itself.
        """

        # check if the variable 'self.acc1 exists, else create the variable
        # as a dictionary with keys indentical to the weights dictionary, but
        # with all values in the matrices set to 0.
        if ...:

            # create the dict 'self.acc1' with keys identical to the weights
            # dictionary (keep in mind that copying dictionaries is not the
            # same as copying variables! Use the imported deepcopy
            # function for this purpose)
            self.acc1 = ...

            # initialize all values to similarly sized matrices of zeros
            for key in ...:
                self.acc1[key] = ...

        # check if the variable 'self.acc2 exists, else create the variable
        # as a dictionary with keys indentical to the weights dictionary, but
        # with all values in the matrices set to 0.
        if ...:

            # create the dict 'self.acc2' with keys identical to the weights
            # dictionary (keep in mind that copying dictionaries is not the
            # same as copying variables! Use the imported deepcopy
            # function for this purpose)
            self.acc2 = ...

            # initialize all values to similarly sized matrices of zeros
            for key in ...:
                self.acc2[key] = ...

        # check if the variable 'self.acc1b exists, else create the variable
        # as a dictionary with keys indentical to the weights dictionary, but
        # with all values in the matrices set to 0.
        if ...:

            # create the dict 'self.acc1' with keys identical to the weights
            # dictionary (keep in mind that copying dictionaries is not the
            # same as copying variables! Use the imported deepcopy
            # function for this purpose)
            self.acc1b = ...

            # initialize all values to similarly sized matrices of zeros
            for key in ...:
                self.acc1b[key] = ...

        # check if the variable 'self.acc2b exists, else create the variable
        # as a dictionary with keys indentical to the weights dictionary, but
        # with all values in the matrices set to 0.
        if ...:

            # create the dict 'self.acc2b' with keys identical to the weights
            # dictionary (keep in mind that copying dictionaries is not the
            # same as copying variables! Use the imported deepcopy
            # function for this purpose)
            self.acc2b = ...

            # initialize all values to similarly sized matrices of zeros
            for key in ...:
                self.acc2b[key] = ...

        # initialize 'self.count' to 1 if it does not exist, else update the
        # counter by adding 1
        if ...:
            self.count = ...
        else:
            self.count = ...

        # loop throught the dictionary of weigths
        for key in ...:

            # update accumulated first order moment (access the
            # hyperparameters, e.g. learning rate, through the specified
            # 'self.parameters')
            self.acc1[key] = ...

            # update accumulated first order moment (access the
            # hyperparameters, e.g. learning rate, through the specified
            # 'self.parameters')
            self.acc2[key] = ...

            # calcluate bias corrected first order moment (access the
            # hyperparameters, e.g. learning rate, through the specified
            # 'self.parameters')
            self.acc1b[key] = ...

            # calculate bias corrected second order moment (access the
            # hyperparameters, e.g. learning rate, through the specified
            # 'self.parameters')
            self.acc2b[key] = ...

            # update weights (access the hyperparameters, e.g. learning rate,
            # through the specified 'self.parameters')
            self.theta[key] = ...
