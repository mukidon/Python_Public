from PIL import Image
import os
import PIL
import glob

image = Image.open('../images/small-39941552906266.jpg')
print(image.size)

resized_image = image.resize((219,219))
resized_image.save('resizedImage.jpg')
print(resized_image.size)