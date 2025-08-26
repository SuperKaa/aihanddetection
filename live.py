import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

picture = cv2.VideoCapture(0)

while True:
    ret, frame = picture.read()
    if not ret:
        break

    results = model.predict(frame, conf=0.7)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 Custom Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

picture.release()
cv2.destroyAllWindows()
