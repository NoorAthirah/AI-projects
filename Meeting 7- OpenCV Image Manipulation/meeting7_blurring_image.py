import cv2  # dijelaskan di bagian a

img = cv2.imread("C:/Users/User/Desktop/Python AI/Meeting 7/avenger.jpg")
# print(img.shape)
# img = cv2.resize(img, (300, 400))
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) #fx is width, fy is height
#img = cv2.blur(img, (20,30)) #A kernel size of (20, 30) means a 20-pixel wide and 30-pixel tall rectangle is used to calculate the average of the pixel values within this region
#img = cv2.boxFilter(img, -1, (10, 10))
#img = cv2.GaussianBlur(img, (9,9), 1) #1 is standard deviation more value more blur, 9,9 kernel size

cv2.imshow("Image", img)  #title of the windows
cv2.waitKey(0)
cv2.destroyAllWindows() 


