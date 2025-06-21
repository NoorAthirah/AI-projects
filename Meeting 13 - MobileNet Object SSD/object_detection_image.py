import numpy as np
import cv2

min_confidence = 0.6
classes = ['background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
colors = np.random.uniform(0, 255, size=(len(classes), 3)) #generates rgb, number of class, 3 is rgb channels. each class will eb diapled unique colour of rectangle


net = (cv2.dnn.readNetFromCaffe
       ("models/MobileNetSSD_deploy.prototxt.txt",
        "models/MobileNetSSD_deploy.caffemodel"))
image = cv2.imread('images/1.jpg')
image = cv2.resize(image, (800, 600))

height, width = image.shape[0], image.shape[1] #Retrieve image height and width dimension data
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5) #resize 300x300, scaling factor to normalize pixel values, 127.5 mean substraction to normalize pixel values
net.setInput(blob) #set image as in put to the network
detected_objects = net.forward() #detect objects and teh result stored in detected_objects in list

# Print the detected_objects contents
print("Detected Objects:")
print(detected_objects)


#Loop through each detected objects

for i in range(detected_objects.shape[2]): #third dimension represents the number of detected objects
    confidence = detected_objects[0, 0, i, 2] #retrieve the confidence score for the ith object
    if confidence > min_confidence: #Only take object detection results with a minimum confidence value of 60%
        class_id = int(detected_objects[0, 0, i, 1]) #Extract class ID for detected objects
        print(classes[class_id])

        prediction_text = f"{classes[class_id]}: {confidence:.2f}"
        box = detected_objects[0, 0, i, 3:7] * np.array([width, height, width, height])  #extract bounding box coordinates
        (start_x, start_y, end_x, end_y) = box.astype('int')  # these are top-left and bottom right coordinates
        cv2.rectangle(image, (start_x, start_y), (end_x, end_y), colors[class_id], 2)  #draws rectangle
        #adjust text placement
        #if top of bounding box is far from top of image (more than 30 pixels), put the text above the box
        if start_y > 30:
            y = start_y - 15  #adjust y-coordinate for the label text 15 pixels above the bounding box
        else:  # if the box is near top, place the label text 15 pixels below bounding box
            y = start_y + 15  #
        cv2.putText(image, prediction_text, (start_x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[class_id], 2)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()