import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Karan\AppData\Local\Tesseract-OCR\tesseract.exe'
import cv2

img = cv2.imread('img.png')
text = tess.image_to_string(img)

  
# path of the current script 
path = 'P:\\Image to Text'

# Creates a new file 
file = open("output.txt","w")

#write text in file
file.write(text) 
file.close() 
