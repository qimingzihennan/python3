import tesserocr
from PIL import Image

image = Image.open('/Users/hongwei/Downloads/image.png')
print(tesserocr.image_to_text(image))
