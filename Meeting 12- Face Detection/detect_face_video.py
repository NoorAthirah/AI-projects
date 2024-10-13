import numpy as np
import cv2

#Minimum confidence model value when detecting faces. Minimum 50% of the objects are faces
min_confidence = 0.5

# Parameter 1: Prototxt file which is the structure of the neural network graph model that will be used later
# Parameter 2: .caffemodel file which is a pre-trained Caffe model file for face detection

net = (cv2.dnn.readNetFromCaffe
       ("models/deploy.prototxt.txt",
        "models/res10_300x300_ssd_iter_140000.caffemodel"))
#cv2.dnn.readNetFromCaffe() #built-in function from OpenCV to load Caffe pre-trained model

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    height, width = frame.shape[0], frame.shape[
        1]  # access the image size, namely height, width and stored in variables height, width
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > min_confidence:
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (startX, startY, endX, endY) = box.astype('int')
            text = "{:.2f}%".format(confidence * 100)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(frame, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.445, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)
    key=cv2.waitKey(1) & 0xFF #hexadecimal numbers #wait 1 seconds before close
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()







