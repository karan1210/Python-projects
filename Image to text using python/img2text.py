# import lib

import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Users\Karan\AppData\Local\Tesseract-OCR\tesseract.exe'
import cv2

img = cv2.imread("text.png")
text = tess.image_to_string(img)

# create new file

file = open("output_karan.txt","w")
file.write(text)
file.close() 
