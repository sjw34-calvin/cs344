from keras import layers
from keras import models
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import cv2
from tqdm import tqdm

# import the dataset
original_dataset_dir = '/home/sjw34/Desktop/cs344/flowers'
# list the contents of the dataset
print(os.listdir(original_dataset_dir))

# import all the individual folders of flowers
flower_daisy_dir = '/home/sjw34/Desktop/cs344/flowers/daisy'
flower_sunflower_dir = '/home/sjw34/Desktop/cs344/flowers/sunflower'
flower_tulip_dir = '/home/sjw34/Desktop/cs344/flowers/tulip'
flower_rose_dir = '/home/sjw34/Desktop/cs344/flowers/rose'
flower_dandelion_dir = '/home/sjw34/Desktop/cs344/flowers/dandelion'

# directory where i will be storing the smaller data sets
#base_dir = '/home/sjw34/Desktop/cs344/flowers_small'
# os.mkdir(base_dir)

X = []
Z = []
img_size = 150

# train data function creates a directory with the training images


def make_train_data(flower_type, dir):
    for img in tqdm(os.listdir(dir)):
        label = assign_label(img, flower_type)
        path = os.path.join(dir, img)
        img = cv2.imread(path, cv2.imread_color)
        img = cv2.resize(img, (img_size, img_size))
        X.append(np.array(img))
        Z.append(str(label))


make_train_data('Daisy', flower_daisy_dir)
print(len(X))






