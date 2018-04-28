# -*-encoding:utf-8-*-
__author__ = 'jasonchen'
import pytesseract
from PIL import Image
import os
import urllib


def RecognitionofImg():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    imgpath = os.path.join(path, 'Data/cpatcha.jpg')
    #get url
    url1 = 'http://192.168.112.178/Kaptcha.jpg?1'
    urllib.urlretrieve(url1, imgpath, None)
    image = Image.open(imgpath)
    text = pytesseract.image_to_string(image)

    return text

print RecognitionofImg()