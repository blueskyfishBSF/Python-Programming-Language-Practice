# coding=gbk
import cv2
import numpy as np
prototxt_path = r"C:\Users\DELL\Desktop\OpenCV-LAB\deploy.prototxt.txt"
model_path = r"C:\Users\DELL\Desktop\OpenCV-LAB\res10_300x300_ssd_iter_140000_fp16.caffemodel"
model = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
cap = cv2.VideoCapture(0)
while True:
    _, image = cap.read()
    h, w = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))
    model.setInput(blob)
    output = np.squeeze(model.forward())
    font_scale = 1.0
    for i in range(0, output.shape[0]):
        confidence = output[i, 2]
        if confidence > 0.5:
            box = output[i, 3:7] * np.array([w, h, w, h])
            start_x, start_y, end_x, end_y = box.astype(int)
            cv2.rectangle(image, (start_x, start_y), (end_x, end_y), color=(255, 0, 0), thickness=2)
            cv2.putText(image, f"{confidence*100:.2f}%", (start_x, start_y-5), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0), 2)
    cv2.imshow("image", image)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
cap.release()
