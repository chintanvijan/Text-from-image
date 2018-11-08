#Extracting text from image
from PIL import Image
import pytesseract
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="input_images/image1.jpg")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#cv2.imshow("Original", image)

blurred = cv2.blur(image, (3,3))
#cv2.imshow("Blurred_image", blurred)
img = Image.fromarray(blurred)
text = pytesseract.image_to_string(img, lang='eng')
words = text.split("\n")
print(text)
print(words)
#cv2.waitKey(0)