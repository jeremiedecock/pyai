#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2013,2014,2015 Jérémie DECOCK (http://www.jdhp.org)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import numpy as np
import math


# MAIN ########################################################################

def main():

    # SETUP OBJECTIVE FUNCTION ############################

    objective_func = "sphere"

    if objective_func == "sphere":
        # Sphere ##########################
        from function.sphere import Function
        #f = Function(1)
        f = Function(2)

    elif objective_func == "noised_sphere":
        # Noised sphere ###################
        from function.noised_sphere import Function
        #f = Function(1)
        f = Function(2)

    elif objective_func == "sin1":
        # Sinusoid functions ##############
        from function.sin1 import Function
        f = Function()

    elif objective_func == "sin2":
        # Sinusoid functions ##############
        from function.sin2 import Function
        f = Function()

    elif objective_func == "sin3":
        # Sinusoid functions ##############
        from function.sin3 import Function
        f = Function()

    elif objective_func == "yahoo":
        # Yahoo function ##################
        from function.yahoo import Function
        f = Function()

    elif objective_func == "deg_2_poly":
        # Degree 2 polynomial function ####
        from function.degree_2_polynomial import Function
        f = Function(np.array([6.,2.]), np.array([1.,2.]), 1., 2)

    else:
        raise Exception("Wrong objective_func value.")

    # Plot ########
    #f.plot()


    # OPTIMIZER ###########################################

    optimizer_choice = "cutting_plane"

    if optimizer_choice == "naive":
        # Naive Minimizer #################
        from optimizer.naive import Optimizer
        optimizer = Optimizer()
        best_x = optimizer.optimize(f, num_samples=300)

    elif optimizer_choice == "gradient":
        # Gradient descent ################
        from optimizer.gradient import Optimizer
        optimizer = Optimizer()
        f.delta = 0.01
        best_x = optimizer.optimize(f, num_iterations=30)

    elif optimizer_choice == "saes":
        # SAES ############################
        from optimizer.saes_hgb import Optimizer
        optimizer = Optimizer(x_init=np.ones(f.ndim), num_evals_func=lambda gen_index: math.floor(10. * pow(gen_index, 0.5)))
        optimizer = Optimizer(x_init=np.ones(f.ndim))
        best_x = optimizer.optimize(f, num_gen=50)

    elif optimizer_choice == "cutting_plane":
        # Gradient descent ################
        from optimizer.cutting_plane import Optimizer
        optimizer = Optimizer()
        best_x = optimizer.optimize(f, num_iterations=15)

    elif optimizer_choice == "eda":
        # EDA #############################
        #from optimizer.eda import Optimizer
        pass

    else:
        raise Exception("Wrong optimizer_choice value.")

    print("Best sample: f(", best_x, ") = ", f(best_x))

if __name__ == '__main__':
    main()

