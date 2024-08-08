from ultralytics import YOLO

# Load a model
model = YOLO("/home/tangkai/fzj/project/yolov8/assets/yolov8n-pose.pt")

# Predict with the model
results = model("/home/tangkai/fzj/project/yolov8/assets/11s.mp4", show=False, save=True, imgsz=384, conf=0.5)