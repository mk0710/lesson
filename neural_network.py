# coding:utf-8
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape)
print(type(train_labels))
image = test_images[0]
plt.imshow(image)
plt.show()