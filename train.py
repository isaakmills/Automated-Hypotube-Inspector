from ultralytics import YOLO

model = YOLO("yolov8m.pt")

results = model.train (data="blackdotdatav1/data.yaml", epochs =3, imgsz=640 ) #train