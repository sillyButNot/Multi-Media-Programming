import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
import numpy as np
from sklearn.metrics import confusion_matrix
import cv2

# tr_file = input('Enter list file for training:')
tr_file = 'list_tr'
# ts_file = input('Enter list file for testing:')
ts_file = 'list_te'
# n_epochs = int(input('Enter number of epochs:'))
n_epochs = int(30)
# b_size = int(input('Enter number of classes:'))
b_size = int(10)

# n_tag = int(input('Enter number of classes : '))
n_tag = int(6)
# l_rate = float(input('Enter learning rate:'))
l_rate = float(0.1)
SX = SY = 64

image = cv2.imread('.\test_ckadhl\te_image_000_000.jpg')
cv2.imshow('image',image)
