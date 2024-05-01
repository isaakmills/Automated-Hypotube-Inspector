
from ultralytics import YOLO
from ultralytics.models.yolo.detect import DetectionPredictor
from PIL import Image, ImageDraw
import numpy as np
import cv2
import serial
import time
import os
import math
import re
import subprocess
####################################################################################################
#feedback####################################################################################################
####################################################################################################
def status_mes(output=None):
    ser.write(b'?\n')
    time.sleep(0.1)  # Adjust as needed
    prev_line = ''
    last_line = ''
    while True:
        line = ser.readline().decode('utf-8').strip()
        if not line:
            break
        prev_line = last_line
        last_line = line

    if output == 'prev':
        print(prev_line)
    elif output == 'last':
        print(last_line)
    else:
        return prev_line

def status():
    response = status_mes()
    
    if response.startswith('<Idle') or response.startswith('<Home'):
        return True
    elif response.startswith('<Run'):
        time.sleep(.25)
        print(status_mes())
        return status()
    elif response.startswith('<Hold'):
        ser.close()
        print(status_mes())
        print("Machine Malfunction")
    elif response.startswith('<Alarm'):
        print("Machine is in alarm state")
        print(status_mes())
    elif response.startswith(''):
        time.sleep(.25)
        print("Machine Homing")
        print(status_mes())
        return status()
    else:
        print("unknown state")
        print(status_mes())
        ser.close()
    
def report():
    status_mes("prev")
    status_mes("last")
#######################################
###############################################################
######################################

def fileopen_predictcount():
        #folder open 
    max_folder = None
    max_value = float('-inf')

    # Path to the directory containing folders
    filepath = r"runs\detect"

        # Iterate through each folder in the directory
    for folder in os.listdir(filepath):
        # Check if the current item is a directory
        if os.path.isdir(os.path.join(filepath, folder)):
            try:
                # Extract the folder name and the numeric part using regular expression
                folder_name = str(folder)
                match = re.match(r'([a-zA-Z]+)(\d+)', folder_name)

                if match: 
                    word = match.group(1)
                    number = int(match.group(2))

                    # Update max_value and max_folder if the current folder's number is higher
                    if number > max_value:
                        max_value = number
                        max_folder = folder_name

            except Exception as e:
                # Catch any exceptions that might occur during processing
                print(f"Error processing folder {folder}: {e}")
    updatedpath = r"C:\Users\Isaak\Documents\QC machine\runs\detect"
    labels = r"labels"


    # Print the folder with the highest number
    if max_folder is not None:
        

        # Construct the folder path with the highest number
        folder_path = os.path.join(updatedpath, max_folder, labels)
        
        # Define a function to count lines in files
        def count_lines_in_files(folder_path):
            
            # Initialize a dictionary to store filename-line count pairs
            file_line_counts = {}
            total_instance = 0 
            # Iterate through each file in the specified folder
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                
                

                # Check if the current item is a file and ends with '.txt'
                if os.path.isfile(file_path) and filename.endswith('.txt'):
                    try:
                        # Open the file for reading
                        with open(file_path, 'r') as file:
                            # Count the number of lines in the file
                            line_count = sum(1 for line in file)
                            total_instance = total_instance + line_count
                            # Store the filename and its line count in the dictionary
                            
                    except Exception as e:
                        # Catch any exceptions that might occur during file processing
                        print(f"Error processing file {filename}: {e}")

            return print(f"{total_instance} detections")
        
        folderpop_path = os.path.join(updatedpath, max_folder)
        subprocess.Popen(["explorer", folderpop_path], shell = True)
        

        # Call the function to count lines in files
        line_counts = count_lines_in_files(folder_path)

        # Print the line counts for each file

#####################################################
####################################################
#take photo function
img_counter = 0

def delete_existing_images():
    folder = 'rawimgs'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

def image_cap():
     # Delete existing images before capturing a new one

    if status():
        global img_counter 

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error: unable to open camera")
            return
        
        ret, frame = cap.read()

        if not ret:
            print("Error: Couldn't capture frame.")
            return
        cap.release()

        aspect_ratioh = 640 / float(frame.shape[1])
        aspect_ratiow = 640 / float(frame.shape[0])

        height_size = int(frame.shape[0]*aspect_ratiow)
        width_size = int(frame.shape[1]*aspect_ratioh)

        resize = cv2.resize(frame,(width_size,height_size))

        if resize is None:
            print("Error: Unable to resize the img")
            exit()

        img_counter += 1

        file_name = f"rawimgs/img_{img_counter}.jpg"
        cv2.imwrite(file_name, resize)
        print(f"img saved as {file_name}")
    else:
        return print("Image Cap Error")

###############################################################
#define the prediction script
    
def predict():
    model = YOLO("best.pt")
    imgs_dir = "rawimgs"

    # Get a list of image filenames
    img_filenames = [os.path.join(imgs_dir, filename) for filename in os.listdir(imgs_dir) if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

    # Load images and convert them to NumPy arrays
    images = [np.array(Image.open(filename)) for filename in img_filenames]

    # Run inference on the images
    results = model.predict(images, save=True,save_txt=True, imgsz=640, conf=0.5)


###############################################################
#################################
part_length = 5 #part length in mm 
part_diameter =10    # part diameter in mm

print(f"Part length:{part_length}mm, Part Diameter:{part_diameter} mm")

#####################################
#calculate variables
cam_width = 7.5
strcamwidth = str(7.5)
#calculate amount of sections
section_amount = math.ceil(part_length/cam_width)
section_amount_str = str(section_amount)
#calculates intial start pos
halfcamwidth = cam_width/2
start_pos = str(part_diameter/cam_width-halfcamwidth)
#circumference in mm 
circumference = part_diameter*3.14159
rotation_distance = str(circumference/6)


rotation_distance = int(circumference/6)
rotation_distance_rounded = str(math.ceil(rotation_distance))
rotation_distance_rounded_int = int(math.ceil(rotation_distance))

print(f"Part length:{part_length}mm, Part Diameter:{part_diameter} mm")
print(f"Y movements per section:{rotation_distance_rounded}, total x axis movements :{section_amount_str} ")
####################################################################################################
#Functions to send G-code command to GRBL
def home():
    ser.write(b'$H\n')

def G91():
    if status():
        print("G91")
        ser.write(b'G91\n')
        pass
    else: 
        time.sleep(1)
        return G91()
  
def startpos():
    if status():
        report() 
        ser.write((f"G0 X{start_pos} \n").encode('utf-8'))
        print("moving to start pos")
    else:
        time.sleep(1)
        return startpos()
    
def nxtsection():
    if status():
        report() 
        ser.write((f"G0 X{strcamwidth} F200 \n").encode('utf-8'))
        print("next section")
    else:

        return nxtsection()

def rotate():
    if status():
        report()
        ser.write((f"G0 Y-{rotation_distance} F200 \n").encode('utf-8'))
        print("rotating")
    else:

        return rotate()
  

def rotateandpicloop():
    for i in range(rotation_distance_rounded_int):
        rotate()
        image_cap()

    
def sectionloop():
    for i in range(section_amount):
        rotateandpicloop()
        nxtsection()

def run():
    sectionloop()

###########################################################
#run

# Open serial port (replace 'COM3' with the port name of your CNC controller)
ser = serial.Serial('COM11', 115200, timeout=1)
# Wait for GRBL to initialize
time.sleep(2)






delete_existing_images() 
home()
G91()
run()
ser.close()
predict()
fileopen_predictcount()


