import cv2 
import numpy as np


img = cv2.imread("C:/Users/User/Desktop/Python AI/Meeting 7/avenger.jpg")

# Create a mask with the same dimensions as the image
mask = np.zeros(img.shape[:2], dtype="uint8")

# Draw a circle on the mask
cv2.circle(mask, (160,200), 165, 255, -1) 

# Apply the mask to the image
img = cv2.bitwise_or(img, img, mask = mask) 

# Display the mask and the masked image
cv2.imshow("Mask", mask)
cv2.imshow("Image", img)  #title of the windows

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows() 

