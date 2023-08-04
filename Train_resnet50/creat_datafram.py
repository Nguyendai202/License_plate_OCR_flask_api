import os
import cv2
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET

path_data = "Train_resnet50\labels_new.csv"
print(os.getcwd())

def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

df = load_data(path_data)

image_path_list = list(df['filepath']) # 1 list chứa đường dẫn ảnh từ 1 filecsv  chứa đường dẫn xml và toạ độ tương ứng 
# def verify_output(path):
#     img = cv2.imread(path)
#     print(img.shape) 
#     cv2.namedWindow('example', cv2.WINDOW_NORMAL)
#     cv2.imshow('example', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()


if __name__ == "__main__":
     image_path_list  = image_path_list 
    #  for image_path in image_path_list:
    #     verify_output(image_path)
