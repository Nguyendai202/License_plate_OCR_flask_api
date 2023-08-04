from creat_datafram import df,image_path_list,load_data
from sklearn.model_selection import train_test_split
import cv2
import tensorflow as tf 
import numpy as np
labels = df.iloc[:,1:].values
data = []# matrix ảnh 
output = [] # các toạ độ (label)
for ind in range(len(image_path_list)):
    image = image_path_list[ind]
    img_arr = cv2.imread(image)
    h,w,d = img_arr.shape
    # procesing 
    load_image = tf.keras.preprocessing.image.load_img(image,target_size=(160,160))
    load_image_arr =  tf.keras.preprocessing.image.img_to_array(load_image)
    # normalization 
    norm_load_image_arr = load_image_arr/255.0
    # normalize to labels
    multilable,xmin,xmax,ymin,ymax = labels[ind]
    nxmin,nxmax = xmin/w,xmax/w
    nymin,nymax = ymin/h,ymax/h
    label_norm = (multilable,nxmin,nxmax,nymin,nymax) 
    data.append(norm_load_image_arr)
    output.append(label_norm)
def train_test_splitt(X,y):
    x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
    return x_train,x_test,y_train,y_test

    # # convert output array to a numpy array
    # output_arr = np.array(output)
    # data_array = np.array(data)

    # # save data and output to CSV files
    # np.savetxt("maxtrix_images.csv", data_array.reshape(len(data), -1), delimiter=",")
    # np.savetxt("boxes_images.csv", output_arr, delimiter=",", fmt="%f,%f,%f,%f,%f")

X =np.array(data,dtype=np.float32)
y = np.array(output,dtype=np.float32)
X_train1 ,X_test1,y_train1,y_test1=train_test_splitt(X,y)














