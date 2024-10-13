import numpy as np
import cv2

#Minimum confidence model value when detecting faces. Minimum 50% of the objects are faces
min_confidence = 0.5

# Parameter 1: Prototxt file which is the structure of the neural network graph model that will be used
# Parameter 2: .caffemodel file which is a pre-trained Caffe model file for face detection

net = (cv2.dnn.readNetFromCaffe
       ("models/deploy.prototxt.txt",
        "models/res10_300x300_ssd_iter_140000.caffemodel"))
#cv2.dnn.readNetFromCaffe() #built-in function from OpenCV to load Caffe pre-trained model

image = cv2.imread('images/masked.jpg') #Load the image that will later detect the face

height, width = image.shape[0], image.shape[1]#access the image size, namely height, width and stored in variables height, width
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300,300)) , 1.0, (300,300), (104.0, 117.0, 123.0))
net.setInput(blob) #sets the prepared blob as the input to the neural network using the setInput() method.

detections = net.forward() #Performs forward pass to get face detections

#blob-binary large object
#resize image to 300,300
#1.0 - This is a scaling factor. In this case, it means that the pixel values will remain unchanged (1.0 means no scaling).
# 104.0, 117.0, 123.0.  mean subtraction values for the three color channels (BGR)

#this part of the code checks all the faces the model found, decides if they're real enough to draw boxes around
for i in range(0, detections.shape[2]): #a
    confidence=detections[0,0,i,2] #b
    if confidence > min_confidence: #c if confidence detected iis more than 0.5
        box=detections[0,0,i, 3:7]*np.array([width, height, width, height]) #d
        (startX, startY, endX, endY)=box.astype('int') #e this line converts the box’s coordinates into whole numbers (integers), because we need exact pixels.
        text="{:.2f}%".format(confidence*100) #f This line takes the confidence score (remember, it’s a number between 0 and 1) and turns it into a percentage.
        y=startY-10 if startY -10 > 10 else startY+10 #g
        cv2.rectangle(image, (startX,startY),(endX,endY),(0,0,255),2) #h  This draws a rectangle (bounding box) on the image using OpenCV’s cv2.rectangle function
        cv2.putText(image, text,(startX,y),cv2.FONT_HERSHEY_SIMPLEX,0.445,(0,0,255),2) #i This draws the confidence score (the text string) onto the imag


cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#a
# This line loops over the detected objects.
# The detections array has multiple dimensions, and detections.shape[2] represents the number of detected objects (the third dimension of the detections array).
# So, you're iterating over each detection.



#b
#This line retrieves the confidence score for the i-th detection.
# 0: Look at the first image in the batch.
# 0: Use the first output of the detection model.
# i: Select the i-th detected object (this changes for each iteration of the loop).
# 2: Get the confidence score of that detected object.



#d
#This extracts the bounding box coordinates for the detection and scales them to the image size:
#0: Look at the first image in the batch.
# 0: Use the first output of the detection model.
# i: Select the i-th detected object (this changes for each iteration of the loop).
# 3:7: Get the values starting from index 3 to index 6 for that detected object, which represent the bounding box coordinates.


#g
#y=startY-10 if startY -10 > 10 else startY+10
#This line is figuring out where to put the confidence percentage text. Should it go above the box or below the box?
#If there’s enough room above the box (startY - 10 > 10), the text goes above. Otherwise, the text goes below the box so it doesn’t overlap the object.


#(startX, startY): The top-left corner of the box.
#(endX, endY): The bottom-right corner of the box.

