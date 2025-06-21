import cv2
import numpy as np
import imutils
import easyocr




img=cv2.imread('images/10.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#decrease the noise in image by using Bilateral Filtering Blurring Techniques
bfilter=cv2.bilateralFilter(gray,11,17,17)
edged=cv2.Canny(bfilter,30,200)

#finding contour location
#imutlis library to do Image Processing to take the alphabet coordinate by using grab_contours() method and sorted()
keypoints=cv2.findContours(edged.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours=imutils.grab_contours(keypoints)
contours=sorted(contours, key=cv2.contourArea, reverse=True)[:10]


location=None
for contour in contours:
    approx=cv2.approxPolyDP(contour,10,True)
    if len(approx)==4:
        location=approx
        break




#Masking Technique
mask=np.zeros(gray.shape,np.uint8)
new_image=cv2.drawContours(mask,[location], 0, 255, -1)
new_image=cv2.bitwise_and(img,img,mask=mask)
#delete black colour inside masked image
(x,y) = np.where(mask==255)
(x1,y1)= (np.min(x), np.min(y))
(x2,y2)=(np.max(x), np.max(y))
cropped_image=gray[x1:x2+1, y1:y2+1]


#read text inside picture
reader=easyocr.Reader(['en']) #English
result=reader.readtext(cropped_image)
print(result) #print list of information of plate number

#find complete information of location data and text of number plate
text=result[0][-2]
res=cv2.putText(img, text, (approx[0][0][0], approx[1][0][1]+60),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0), 2)
res=cv2.rectangle(img,tuple(approx[0][0]), tuple(approx[2][0]), (255,255,0),3)

# cv2.imshow("Canny Edge Detector", edged)
# cv2.imshow("Image", gray)
# cv2.imshow("Mask Image", new_image)
# cv2.imshow("Masked Image Remove Black", cropped_image)
cv2.namedWindow("Final Image", cv2.WINDOW_NORMAL)  # Make the window resizable
cv2.resizeWindow("Final Image", 600, 400)  # Set the window size


cv2.imshow("Final Image", cv2.cvtColor(res, cv2.COLOR_BGR2RGB))

cv2.waitKey(0)
cv2.destroyAllWindows()