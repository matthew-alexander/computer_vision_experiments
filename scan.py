from transform import four_point_transform
import imutils
from skimage.filters import threshold_adaptive
import numpy as np
import argparse
import cv2

ap = argparse.ArguementParser()
ap.add_arguement("-i", "--image", required = True, help = "Path to the image to be scanned")
args = vars(ap.parse_args())

### edge detection

#load image, compute old height to new height, clone it, resize it
image = cv2.imread(args["image"])
ratio = image.shape[0]/500.0
orig = image.copy()
image = imutils.resize(image, height = 500)

# convert the image to grayscale, blur it, and find edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)
edged = cv2.Canny(gray, 75, 200)

# show the original image and the edge detected image
print "STEP 1: Edge Detection"
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()


