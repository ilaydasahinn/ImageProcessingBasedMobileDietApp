# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eCGt4v-lfE_3Id9AimvkhoQNAE1AIk8e
"""

import cv2
import glob
import os
from google.colab import drive

drive.mount('/content/drive')

import tensorflow as tf
from tensorflow import keras

# Helper libraries
import matplotlib.pyplot as plt
import numpy as np
from os import listdir
from os.path import join
import cv2
import pandas
import os
import random

data = "/content/drive/My Drive/DietApp/PlateDataSet/train"

folders = os.listdir(data)

folders

image_names2 = []
train_labels2 = []
train_images2 = []

size = 256, 256

for folder in folders:
  for file in os.listdir(os.path.join(data, folder)):
    print(file)
    image_names2.append(os.path.join(data, folder, file))
    train_labels2.append(folder)
    img = cv2.imread(os.path.join(data, folder, file))
    train_images2.append(img)

train = np.array(train_images2)

train.shape

train = train.astype('float32') / 255.0

label_dummies = pandas.get_dummies(train_labels2)

labels = label_dummies.values.argmax(1)

pandas.unique(train_labels2)

pandas.unique(labels)

union_list = list(zip(train, labels))
random.shuffle(union_list)
train,labels = zip(*union_list)

train = np.array(train)
labels = np.array(labels)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(256,256,3)),
    keras.layers.Dense(128, activation=tf.nn.tanh),
    keras.layers.Dense(5, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.optimizers.Adam(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train,labels, epochs=5)

