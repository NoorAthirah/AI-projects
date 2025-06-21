from tensorflow.keras.models import load_model
from imutils.contours import sort_contours
import numpy as np
import imutils
import cv2

# Load Pre-Trained Model
print("Load the model...")
model = load_model("handwriting_model.h5")

# Load the image
image = cv2.imread("images/11.png")

# Preprocess: grayscale and blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges
edged = cv2.Canny(blurred, 30, 150)

# Find contours
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sort_contours(cnts, method="left-to-right")[0]

# Extract characters
chars = []
for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    if w >= 5 and h >= 15:  # less restrictive filtering
        roi = gray[y:y + h, x:x + w]
        thresh = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        # Resize while keeping aspect ratio
        (tH, tW) = thresh.shape
        if tW > tH:
            thresh = imutils.resize(thresh, width=32)
        else:
            thresh = imutils.resize(thresh, height=32)

        # Add padding to make 32x32
        (tH, tW) = thresh.shape
        dX = int(max(0, 32 - tW) / 2.0)
        dY = int(max(0, 32 - tH) / 2.0)
        padded = cv2.copyMakeBorder(
            thresh, top=dY, bottom=dY, left=dX, right=dX,
            borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0)
        )
        padded = cv2.resize(padded, (32, 32))
        padded = padded.astype("float32") / 255.0
        padded = np.expand_dims(padded, axis=-1)

        chars.append((padded, (x, y, w, h)))

# Prepare for prediction
boxes = [b[1] for b in chars]
chars = np.array([c[0] for c in chars], dtype="float32")

# Predict
preds = model.predict(chars)
labelNames = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Annotate the image
for (pred, (x, y, w, h)) in zip(preds, boxes):
    i = np.argmax(pred)
    prob = pred[i]
    label = labelNames[i]
    print("[INFO] {} - {:.2f}%".format(label, prob * 100))
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, label, (x - 10, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

# Show the final annotated image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
