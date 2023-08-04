import csv
import os

# Mở file csv chứa danh sách đường dẫn tương đối
with open('2_Train_Object_Detection_model/labels.csv', 'r', newline='') as f:
    # Đọc dữ liệu từ file vào một list
    reader = csv.reader(f)
    paths_list = list(reader)

# Duyệt qua các phần tử của list và chuyển đổi đường dẫn tương đối thành đường dẫn tuyệt đối
for i in range(len(paths_list)):
    path_relative = paths_list[i][0]   # Lấy đường dẫn tương đối từ list
    path_absolute = os.path.abspath(path_relative).replace("\\","//")  # Chuyển đổi đường dẫn tương đối thành đường dẫn tuyệt đối
    paths_list[i][0] = path_absolute   # Thay đổi giá trị của phần tử tương ứng trong list
    
# Ghi lại danh sách đường dẫn tuyệt đối vào file csv
with open('2_Train_Object_Detection_model/labels.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(paths_list)

# In ra danh sách đường dẫn tuyệt đối mới
for path in paths_list:
    print(path)
