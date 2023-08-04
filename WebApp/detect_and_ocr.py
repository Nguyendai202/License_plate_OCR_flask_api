import numpy as np
import cv2
# import matplotlib.pyplot as plt
import tensorflow as tf
from keras.preprocessing import image
import pytesseract 
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
Example_tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract'

model = tf.keras.models.load_model("WebApp/static/models/object_detection.h5")

def object_detection(path,filename):
    # read image
    image = tf.keras.preprocessing.image.load_img(path) # PIL object
    image = np.array(image,dtype=np.uint8) # 8 bit array (0,255)> để xử lí ảnh 
    image1 = tf.keras.preprocessing.image.load_img(path,target_size=(224,224))# return type=obj
    # data preprocessing
    image_arr_224 =  tf.keras.preprocessing.image.img_to_array(image1)/255.0  # convert into array and get the normalized output
    h,w,d = image.shape
    test_arr = image_arr_224.reshape(1,224,224,3)
    # make predictions
    coords = model.predict(test_arr)
    # denormalize the values
    denorm = np.array([w,w,h,h])
    coords = coords * denorm
    coords = coords.astype(np.int32)
    # draw bounding on top the image
    xmin, xmax,ymin,ymax = coords[0]
    pt1 =(xmin,ymin)
    pt2 =(xmax,ymax)
    print(pt1, pt2)
    cv2.rectangle(image,pt1,pt2,(0,255,0),3)
    # convert into bgr
    image_bgr = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    cv2.imwrite('./3_WebApp/static/predict/{}'.format(filename),image_bgr)
    return coords

def OCR(path,filename):
    img = np.array(tf.keras.preprocessing.image.load_img(path))
    cods = object_detection(path,filename)
    xmin ,xmax,ymin,ymax = cods[0]
    roi = img[ymin:ymax,xmin:xmax]
    roi_bgr = cv2.cvtColor(roi,cv2.COLOR_RGB2BGR)
    cv2.imwrite('./WebApp/static/roi/{}'.format(filename),roi_bgr)
    text = pytesseract.image_to_string(roi,config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 13 --oem 1--tessdata-dir"C:/Program Files/Tesseract-OCR/tessdata/mymodel_process_0404.traineddata"')
    print(text)
    return text