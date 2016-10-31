from PIL import Image
import pytesseract

image = Image.open('/Users/rogueandy/Desktop/cucu.jpg')
print('~~~~~~~ ')
stringImage = pytesseract.image_to_string(image)
print(stringImage)