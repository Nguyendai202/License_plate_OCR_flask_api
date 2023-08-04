import numpy as np
import  cv2
import os 
from sklearn.model_selection import train_test_split
# Tiền xử lý dữ liệu
img_dir ="images/train"
def preprocess_data(X, y):
    # Resize ảnh về kích thước cố định, ví dụ (224, 224)
    X = np.array([cv2.resize(x, (224, 224)) for x in X])
    # Chuẩn hóa dữ liệu về khoảng giá trị [0, 1]
    X = X.astype('float32') / 255.0
    h,w,d = img.shape
    # Chuyển vector y về dạng one-hot encoding
    multilable ,xmin,xmax,ymin,ymax = y
    nxmin,nxmax = xmin/w,xmax/w
    nymin,nymax = ymin/h,ymax/h
    label_norm = (multilable,nxmin,nxmax,nymin,nymax) 
    y = label_norm
    return X, y

# Tạo ma trận đầu vào và vector đầu ra từ các file ảnh
data = []
output = []
for filename in os.listdir(img_dir):
    if filename.endswith('.jpg'):# true nếu đuôi của filename có dạng này 
        img_path = os.path.join(img_dir, filename)
        img = cv2.imread(img_path)
        box_path = os.path.join(img_dir, filename.replace('.jpg', '.txt'))
        with open(box_path, 'r') as f:
            lines = f.readlines()# đọc hết các dòng 
             # áp dụng int cho từng phần tử trong chuỗi line lấy từ lines , strip : loại bỏ khoảng trắng và kí tự ko cần thiết đầu và cuối , split: chia chuỗi con dựa trên khoảng trắng 
            boxes = np.array([list(map(float,line.strip().split(" "))) for line in lines])
        # Nếu không tìm được box tương ứng hoặc box trống thì bỏ qua ảnh này
        if len(boxes) == 0:
            continue
        data.append(img)
        output.append(boxes)

# Chia dữ liệu thành 2 phần: tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(data, output, test_size=0.2)
# Tiền xử lý dữ liệu cho tập huấn luyện và tập kiểm tra
x_train, y_train = preprocess_data(X_train, y_train)
x_test, y_test = preprocess_data(X_test, y_test)


        
