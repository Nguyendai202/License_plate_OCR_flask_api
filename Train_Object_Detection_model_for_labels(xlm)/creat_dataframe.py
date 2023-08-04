import os
import cv2
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET

path_data = "labels.csv"
print(os.getcwd())

def load_data(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

df = load_data(path_data)

def get_image_path(xml_file):
    try:
        directory = os.path.dirname(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        filename = root.find('filename').text
        image_path = os.path.join(directory, filename)
        return image_path
    except Exception as e:
        print(f"Error getting image path: {e}")
        return None

image_path_list = list(df['filepath'].apply(lambda x: get_image_path(x))) # 1 list chứa đường dẫn ảnh từ 1 filecsv  chứa đường dẫn xml và toạ độ tương ứng 
# def verify_output(path):
#     img = cv2.imread(path)
#     print(img.shape) 
#     cv2.namedWindow('example', cv2.WINDOW_NORMAL)
#     cv2.imshow('example', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# for image_path in image_path_list:
#     verify_output(image_path)
if __name__ == "__main__":
     image_path_list  = image_path_list 
