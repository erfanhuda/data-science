import pyTesseract
from PIL import Image
import numpy as np

filename = "test.PNG"
img = np.array(Image.open(filename))
text = pyTesseract.image_to_string(img)
print(text)

def convert_pdf_to_excel():
    pass

def convert_pdf_to_csv():
    pass

def convert_pdf_to_string():
    pass