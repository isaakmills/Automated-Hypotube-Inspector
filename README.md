I![Image](QC_machine_PNG.png)




The Automated Hypotube Inspector is a cutting-edge prototype designed to automate defect detection in catheter manufacturing. Traditionally, quality control in this field requires technicians to visually inspect every single part, a time-consuming and labor-intensive process. This prototype streamlines and automates this task.
First, the host computer executes main.py. The script initializes a serial connection with the Arduino microcontroller running GRBL, an open-source motion control software. The Arduino controls all motion for both the rollers and the camera gantry. The host computer calculates how far to move the camera gantry in each section and begins sending motion commands to the Arduino. Once the motion command has been executed, an image is captured by the Raspberry Pi and sent to a directory on the host computer. The Raspberry Pi is running custom firmware that configures it to be recognized as a USB camera. Once all images have been captured, they are reformatted to a uniform size, and a YOLOv8 detection algorithm is iterated throughout the image directory. Finally, the program opens a popup window containing images of all the detections and outputs the number of detections in the terminal.

1. The host computer runs main.py, which establishes a serial connection with the Arduino running GRBL, an open-source motion control software.
2. The Arduino manages the motion of the rollers and camera gantry, receiving precise movement commands from the host computer.
3. The Raspberry Pi captures images and transfers them to the host computer.
4. The Raspberry Pi, configured as a USB camera, captures images as the gantry moves.
5. These images are resized uniformly and processed using a YOLOv8 detection algorithm.
6. Detected defects are displayed in a popup window, and the total count is shown in the terminal.










Acknowledgments

<a href="https://docs.ultralytics.com">Ultralytics Yolov8</a>    
<a href="https://github.com/computervisioneng/train-yolov8-custom-dataset-step-by-step-guide">train-yolov8-custom-dataset-step-by-step-guide</a>    
<a href="https://www.raspberrypi.com/tutorials/plug-and-play-raspberry-pi-usb-webcam/">plug-and-play-raspberry-pi-usb-webcam</a>  
<a href="https://www.raspberrypi.com/news/how-to-build-your-own-raspberry-pi-webcam">how-to-build-your-own-raspberry-pi-webcam</a>  


<a href="https://github.com/grbl/grbl">GRBL</a> 

<a href="https://github.com/grbl/grbl/wiki/Configuring-Grbl-v0.9">Configuring-Grbl-v0.9</a>


