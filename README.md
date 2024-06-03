![Image](QC_machine_PNG.png)

This is the repository for my Automated Cathider inspecting machine. The machine uses Yolov8 detection algorithms to detect black marks on hypotubes.


The Problem - I was  inspired to create this project beacuse of previous experiance working at a company specializing in laser cutting hypotobes. Within the manufacting process there are mulitple steps which go into preparing a final product; One of them being quality control.

Quality control is the processes of inspecting manufacured parts to ensure they are within customer specification aswell as free from manufacturing defects. Currently in laser cut hypotube manufactring quality control workers are required to visually inspect 100% of the parts. This is a very time consuming task and I relised this could be a perfect use case for a AI computer vision processs. 

The Goal - Create a tool that uses computer vision and cnc technology to detect manufacturing defect without the assistance of a human operator. 

Usage - To use the machine the operator needs to have both the raspberry pi and Arduino connected to the computer.insurd the camera functionalty is working properly by opening the camera program on the compute and waiting for feedback. Inside the main.py file there are three things the operator may need to adjust. First is the COM port of the Aduino controller, this can be found by openning the host computers device manage and looking for the arduino device. Adjust the "ser" variables first parameter to specify the COM port. Next the operator needs to adjust the part_length and part_diameter variables to match the dimentions of the part (both part_length and part_diameter are in mm). Save and close the file. Next the operator needs to set the part on the staged. The operator can run the program. As the program runs the  camera gantry will begin taking measured movments acorss the entire part and the rollers with begin rotating. once the program is complete the number of detections with be output on the command line and a folder will popup with annotated images of all detections. The operator can then visually inspect each indivdual detection and detemine whether it is nessesary to visually inspect the detetions.


Why not Key Dimentions? - From the beginning of the project my understanding of AI computer vision models was that they were good at detecting patterns but lacked the ability to measure accuratly. Manufacturing defects were a prefect example of a usecase or AI comupter vision. Key dimention detection did not. My thinking was that even if I tried to develop a machine that could detect key dimentions the AI models would require highly specialised training for each manufacting lot. Because all parts are unique this would require operatiors to spend time tweaking countless indiviual model for specific dimentions. This did not sound like a good idea. I liked the idea of having one model trained on a wide spectrum of manufacturing defects which could be used on a variaty of unique parts. 


software design -
why I chose yolov8, genral data pipline, Ai training process, challenges with OTG and resberry pi


electrical design-
setting refrenve volate on led drivers, remeber to design electrical routes, control structure,



mechanical design- 
original mechanical design with aliminum plate


manufacturing process- 
grinding rollers, 3d printing, fusion 360,  plastidipping, 


v2 - 



License - 












Acknowledgments

<a href="https://docs.ultralytics.com">Ultralytics Yolov8</a>    
<a href="https://github.com/computervisioneng/train-yolov8-custom-dataset-step-by-step-guide">train-yolov8-custom-dataset-step-by-step-guide</a>    
<a href="https://www.raspberrypi.com/tutorials/plug-and-play-raspberry-pi-usb-webcam/">plug-and-play-raspberry-pi-usb-webcam</a>  
<a href="https://www.raspberrypi.com/news/how-to-build-your-own-raspberry-pi-webcam">how-to-build-your-own-raspberry-pi-webcam</a>  


<a href="https://github.com/grbl/grbl">GRBL</a> 

<a href="https://github.com/grbl/grbl/wiki/Configuring-Grbl-v0.9">Configuring-Grbl-v0.9</a>


