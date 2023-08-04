import csv
import glob
import os 

csv_file = "Train_resnet50/labels_new.csv"
img_dir ="images/train"

# get list of image files and their corresponding box files
img_files = glob.glob(os.path.join(img_dir,"*.jpg"))
box_files = [img_file.replace('.jpg', '.txt') for img_file in img_files]

# open CSV file for writing
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    
    # write column headers to CSV file
    writer.writerow(["filepath","multilabel","xmin","xmax","ymin","ymax"])
    
    # write image and box info to CSV file
    for i, (img_file, box_file) in enumerate(zip(img_files, box_files)):
        try:
            # read bounding box info from box file
            with open(box_file, mode="r") as f:
                multilabel, xmin, xmax, ymin, ymax = f.read().strip().split()
            
            # write image and box info to CSV row
            row = [img_file, multilabel, xmin, xmax, ymin, ymax]
            writer.writerow(row)
            
        except FileNotFoundError:
            print(f"Error: box file not found for {img_file}")
        
        except ValueError:
            print(f"Error: invalid data format in box file {box_file} for image {img_file}")
    
print("done")
