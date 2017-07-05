# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:39:23 2017

@author: adivt
"""

from __future__ import division
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD,RMSprop,adam
from keras.utils import np_utils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os
import theano
from PIL import Image


path = "D:\Aditya\Documents\GitHub\Devanagari-OCR\nhcd"