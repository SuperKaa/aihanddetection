# aihanddetection
Simple hand detection showing three hand gestures. trained using yolov8

model best.pt in /runs/detect/train/weights/best.pt was trained and made by me. dataset was created using roboflow.com then trained locally using ultralytics.

this model has 3 simple detections,
- thumbs up
- palm out
- index finger and thumb out
examples can be seen in /images

to use just:
- run pip install ultralytics
- clone repo
- then run live.py, this will open a live camera window detecting your hand signs live (requires webcam)
