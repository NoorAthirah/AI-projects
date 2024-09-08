import cv2 
import numpy as np


img = cv2.imread("C:/Users/User/Desktop/Python AI/Meeting 7/avenger.jpg")

# # Create a mask with the same dimensions as the image
# mask = np.zeros(img.shape[:2], dtype="uint8")

# # Draw a circle on the mask
# cv2.circle(mask, (300,200), 195, 255, -1) 

# # Apply the mask to the image
# img = cv2.bitwise_or(img, img, mask = mask) 

# Display the mask and the masked image
#cv2.imshow("Mask", mask)

height, width, channel = img.shape
# cv2.line(img, (0,0), (width, height), (0,255,0), 6) #starting coordinate 0,0;  width,height bottom left image, 255 BGR green line, 6 is the thickness of line 
# cv2.line(img, (width,0), (0, height), (55,200,255), 3) #width, 0 is top right, 0, height is bottom left corner, 
#cv2.rectangle(img, (0, 300), (width, height), (255,0,0), 6) #0,300 starting coordinate x=0, y=300 
#cv2.rectangle(img, (0, 0), (width, 100), (0,255,0), -1) 
# cv2.circle(img, (100, 100), 40, (0,0,255), -1) #100,100 is the coordinates, 40 is the radius, red,-1 means the circle should be filled
cv2.circle(img, (100, 100), 20, (255,255,255), 9)
# cv2.circle(img, (250, 100), 40, (0,0,255), -1)
# cv2.circle(img, (250, 100), 20, (255,255,255), -1)
# img = cv2.putText(img, "Avenger", (100, 40), 
# cv2.FONT_HERSHEY_COMPLEX, 1 , (0,0,255), 2)
#         #100,40 the coordinates where text will start, 1 is font size, 2 is thickness of font
 img = cv2.putText(img, "OpenCV", (100, 100), 
cv2.FONT_HERSHEY_COMPLEX, 1 , (255,255,255), 2)
# red = ([0, 0, 30], [50, 56, 255]) #lower bound 
# blue = ([30,0, 0], [255, 150, 50])
# green = ([0, 30, 0], [100, 255, 100])
# white = ([255, 255, 255], [255, 255, 255])
# boundaries = [red,blue,green,white]
# for (lower, upper) in boundaries: 
#     lower = np.array(lower, dtype = "uint8")
#     upper = np.array(upper, dtype = "uint8")
#     mask = cv2.inRange(img, lower, upper)
#     output = cv2.bitwise_and(img, img, mask = mask)
#     cv2.imshow("Color Detection", output)
#     cv2.waitKey(0)

#uint8 stands for "unsigned 8-bit integer." It's a type of data that can store whole numbers, specifically from 0 to 255.

cv2.imshow("Image", img)  #title of the windows

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows() 




#Lower Bound: [0, 0, 30] means:

# Blue = 0 (no blue at all)
# Green = 0 (no green at all)
# Red = 30 (a little bit of red, so it's a very dark red)


# Upper Bound: [50, 56, 255] means:

# Blue = 50 (a little bit of blue)
# Green = 56 (a little bit of green)
# Red = 255 (a lot of red, making it very bright red)