import os
import sys
import numpy as np

from keras.preprocessing import image 
from skimage.io import imread
from skimage.transform import resize
from keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
classifier = load_model('DogOrCat.h5')

lines = sys.stdin.readlines()
imgline = lines[0]

img = imread(imgline)
img = resize(img,(64,64))
img = np.expand_dims(img,axis=0)
 
if(np.max(img)>1):
    img = img/255.0
 
prediction = classifier.predict_classes(img)
 
if(prediction):
    print ("DOG")
else:
    print("CAT")

