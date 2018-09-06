import sys
import numpy as np
import os
import urllib.request

from keras.preprocessing import image 
from skimage.io import imread
from skimage.transform import resize
from keras.models import load_model

path = os.path.dirname(os.path.abspath(__file__))
parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

url = str(sys.argv[1])
urllib.request.urlretrieve(url, path + "/Image.jpg")

modelpath = path + "/DogOrCat.h5"
classifier = load_model(modelpath)
img = imread(path + "/Image.jpg")

img = resize(img,(64,64))
img = np.expand_dims(img,axis=0)
 
if(np.max(img)>1):
    img = img/255.0
 
prediction = classifier.predict_classes(img)

if(prediction):
    print ("DOG")
else:
    print("CAT")

