from tensorflow.keras.models import load_model
from imutils.contours import sort_contours
import numpy as np
import imutils
import cv2

 #Tensorflow is for training models,tracking models and loader models.
 #Keras is located higher than Tensorflow is used to implement Neural Network
 #To differentiate one alphabet to another, we check the object's edge

#Load Pre Trained Model
print("Load the model...")
#Keras 3 no longer supports the SavedModel format directly in the load_model() function. Instead, Keras 3 supports loading models in the .keras format or the legacy .h5 format.
model = load_model("handwriting_model.h5")

#load the picture to classify the alphabet
image=cv2.imread("images/11.png")

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to gray scale image to reduce intensity, reduce image noise
blurred=cv2.GaussianBlur(gray, (5,5), 0) #GB to focus on patterns rather than tiny details

#Convert picture into edge compilation y sing Canny Edge Detection the find the object outline using findContours()

edged=cv2.Canny(blurred, 30,150) #threshold value
cnts=cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
cnts=sort_contours(cnts, method="left-to-right")[0] #find outlines
# print(cnts)

#Lower Threshold (30): This defines the minimum intensity gradient for an edge to be considered. Any gradient value below this threshold will be ignored and considered non-edge.
#Upper Threshold (150): This defines the maximum intensity gradient. Any gradient above this threshold is considered a strong edge.


#Extract data from each coordinates by sing image thresholding technique.
chars=[]
for c in cnts: #loop to detect all characters
    (x,y,w,h) = cv2.boundingRect(c) #take x,y coordinate and w,h
    if (w>=5 and w<=150) and (h>=15 and h<=120): #bounding box size, min 5px max 150px
        roi=gray[y:y +h, x:x +w] #region of interest
        thresh=cv2.threshold(roi,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1] #change image in roi area to image thresholding using Otsu's Binary Threshold technique
        (tH, tW) =thresh.shape
        if tW>tH: #change size of roi area to 32 pxl
            thresh=imutils.resize(thresh,width=32)
        else:
            thresh=imutils.resize(thresh,height=32)
        (tH,tW)=thresh.shape #padding and border
        dX=int(max(0,32 - tW)/2.0)
        dY=int(max(0,32-tH)/2.0)

        padded=cv2.copyMakeBorder(thresh, top=dY, bottom=dY, left=dX, right=dX, borderType=cv2.BORDER_CONSTANT, value=(0,0,0))
        padded=cv2.resize(padded, (32,32)) #resize to 32x32 pxl
        padded=padded.astype("float32")/255.0 #change scale pixels intensities
        padded=np.expand_dims(padded,axis=-1) #1D to 2D by adding dimension from Numpy array padded picture
        chars.append((padded,(x,y,w,h))) #added to the chars list in form of a tuple

boxes=[b[1] for b in chars] #bounding box coordinate from each characters
chars=np.array([c[0] for c in chars], dtype="float32")

preds=model.predict(chars)
labelNames="0123456789"
labelNames += "ABCDEFGHIJKLMNOPRSTUVWXYZ"
labelNames = [ labelNames for labelNames in labelNames]

for (pred, (x,y,w,h)) in zip(preds,boxes):
    i=np.argmax(pred)
    prob=pred[i]
    label=labelNames[i]
    print ("[INFO] {} - {:.2f}%".format(label,prob*100))
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.putText(image,label, (x-10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)

# cv2.imshow("Ori Image", image)
# cv2.imshow("Gray Image", gray)
# cv2.imshow("Edged Image", edged)
# cv2.imshow("Padded Image", padded)
cv2.imshow("Image", image)



cv2.waitKey(0)




