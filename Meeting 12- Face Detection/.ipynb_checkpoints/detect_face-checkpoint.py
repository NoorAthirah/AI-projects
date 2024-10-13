# import numpy as np
# import cv2
# #Import library Numpy dan OpenCV 

# min_confidence = 0.5 #Minimum confidence model value when detecting faces. Minimum 50% of the objects are faces
# # net = cv2.dnn.readNetFromCaffe("models/deploy.prototxt.txt", 
# # "models/res10_300x300_ssd_iter_140000.caffemodel")

# net = cv2.dnn.readNetFromCaffe(
#     "models/deploy.prototxt.txt",
#     "models/res10_300x300_ssd_iter_140000.caffemodel"
# )
# image = cv2.imread('images/masked.jpg') #Load the image that will later detect the face

# cv2.dnn.readNetFromCaffe() #built-in function from OpenCV to load Caffe pre-trained model

# cv2.imshow("Output", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
print(cv2.__file__)
print(hasattr(cv2, 'dnn'))





