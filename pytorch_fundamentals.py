# -*- coding: utf-8 -*-
"""pytorch fundamentals

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ha5eKAwdql5hO0Qv5rn16EZJLhJgcyfP

Learn PyTorch code: https://www.learnpytorch.io/00_pytorch_fundamentals/

If you need help!: https://github.com/mrdbourke/pytorch-deep-learning/discussions
"""

import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(torch. __version__)



!nvidia-smi

"""## Introduction to Tensors

### creating tensors

PyTorch tensors are creating using torch.Tensor() = https://pytorch.org/docs/stable/tensors.html
"""

# scalar
scalar = torch.tensor(7)
scalar

# Get tensor back as a python int
scalar.item()

# Vector
# This could mean many things, one being, (# of cats, # of dogs) in an animal shelter
vector = torch.tensor([8, 8])
vector

## This checks how many dimensions a tensors has
# in this case the "vector" that is made above
vector.ndim

vector.shape

# MATRIX
MATRIX = torch.tensor([[7, 8],[9, 10]])
MATRIX
MATRIX.ndim

MATRIX.shape

### TENSOR
TENSOR = torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 4, 5]]])
TENSOR

TENSOR.ndim

TENSOR.shape

"""Depending on the number of outer brackets: [ ] or [ [ [ ] ] ] the rank of the tensor changes.
[ ] is a rank one, AKA a vector.
[ [ ] ] is a rank two AKA a matrix
"""

bob = torch.tensor ([[[1, 4, 6, 7, 9],[2, 645, 6, 2, 6],[1, 3, 0, 6, 3]]])
bob.ndim

john = torch.tensor([[1, 2, 3],[4, 5, 6],[2, 4, 7]])
john.ndim

"""## Make Random tensors with PyTorch
Random tensors are important since many neural networks learn by starting with random tensors and then adjusting them overtime to better represent the data.

Start with random #s -> look at the data -> update random #s -> look at the data -> update random #s

Torch Random tensors: https://pytorch.org/docs/stable/generated/torch.rand.html
"""

# Create a random tensor of size (3, 4) AKA 3 rows and 4 columns
# the random tensor you create will have #s rangeing from 0-1.
random_tensor = torch.rand(3, 4)
random_tensor

# Now it's my turn to create a random tensor
# If you have three numbers in the torch.rand(), then it is reffering to the rank
# of the tensor
BILLY = torch.rand(1, 2, 8)
BILLY.shape, BILLY.ndim

"""
Zeros and Ones
"""

# Create a tensor of all zeros
zeros = torch.zeros(size=(3, 4))
zeros

# Create a tensor of all ones
ones =  torch.ones(size=(3, 4))
ones

# .dtype the default type for tensors is a float32.
ones.dtype