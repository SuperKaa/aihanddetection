from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

results = model("images/001.png", conf=0.5)

results[0].show()