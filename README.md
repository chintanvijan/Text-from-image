# Text-from-image
Contains python code for extracting data from images (OCR).

Dependencies :
	- Python version 3.0 or above
	- Tesseract-ocr (Download link: https://excellmedia.dl.sourceforge.net/project/tesseract-ocr-alt/tesseract-ocr-setup-3.02.02.exe)
		Note:The above link is for windows users, tesseract for linux ,macOS and others are also available on web. 
				From the above link tesseract would be automatically installed at 'C:/program files(86)/' .
	- Open libraries used which are mentioned below.

Libraries used:
	- PILLOW (PIL) 		# For image manupulation
	- pytesseract  		# For extracting text from image
	- argparse	   		# For argument parsing
	- OpenCV (cv2)		# For image processing

Steps to execute:
	- Extract files from "Text from Image.rar"
	- Open cmd -> reach to path of 'extract.py' file in "Text from Image" directory
	- write code in the form of:
			python extract.py -i "Path of image from which text is to be extracted"

			for.eg. 
				python extract.py -i input_images/image1.jpg

Form of Output:
	- Output is available in form of a String as well as in the form of list containing words(line-wise).

