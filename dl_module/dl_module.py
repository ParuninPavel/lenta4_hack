import keras
import numpy as np
import pandas as pd
from tqdm import tqdm_notebook
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import median_absolute_error
import pickle
from utils.dataset_func import encode
import cv2
import urllib.request


class NN_Predictor(object):
    DIR = 'saved_models/'
    MODEL_IMAGE_NAME = 'image_model_v1.h5' 
    MODEL_TEXT_NAME = 'text_model_v1.h5'
    def __init__(self):
        self.model_text = keras.models.load_model(self.DIR+self.MODEL_TEXT_NAME)
        self.model_image = keras.models.load_model(self.DIR+self.MODEL_IMAGE_NAME)
    def predict(self,txt=None,img=None):
        
        
        if txt == None:
            urllib.request.urlretrieve(img, 'Dataset/images/cache.jpg')
            pic = cv2.imread('Dataset/images/cache.jpg')
            pic = cv2.resize(pic,(224,224))
            pic = pic/255
            
            y_pred = self.model_image.predict(np.array([pic]))
        elif img == None:
            print('TXT=',txt)
            txt2 = encode([txt])
            print(txt2.shape)
            y_pred = self.model_text.predict(np.array(txt2))
        else:
            txt2 = encode([txt])
            urllib.request.urlretrieve(img, 'Dataset/images/cache.jpg')
            pic = cv2.imread('Dataset/images/cache.jpg')
            print(pic.shape)
            pic = cv2.resize(pic,(224,224))
            pic = pic/255
            y_pred_text = self.model_text.predict(np.array(txt2))  
            y_pred_image = self.model_image.predict(np.array([pic]))
            y_pred = (y_pred_text+y_pred_image)/2
        print(y_pred)
        return str(y_pred[0]*100)