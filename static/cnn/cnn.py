#Importing all the important packages and modules
import sys
import numpy as np
import os
import urllib.request

from keras.preprocessing import image 
from skimage.io import imread
from skimage.transform import resize
from keras.models import load_model

#Load the current working path
path = os.path.dirname(os.path.abspath(__file__))

#Get the url of the image from the argument
url = str(sys.argv[1])

#Save that into a local file
urllib.request.urlretrieve(url, path + "/Image.jpg")

#Get the path of the model
modelpath = path + "/DogOrCat.h5"

#Load the Convolutional Neural Networks model file
classifier = load_model(modelpath)

#Read in the image
img = imread(path + "/Image.jpg")

#Resize the image to 64 x 64
img = resize(img, (64, 64))

#Adding another axis to the image
img = np.expand_dims(img, axis=0)
 
 #Equalize the image value
if(np.max(img)>1):
    img = img/255.0
 
#Get the prediction
prediction = classifier.predict_classes(img)

if(prediction):
    print ("DOG")
else:
    print("CAT")

