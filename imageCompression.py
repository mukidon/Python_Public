from PIL import Image
import os
import PIL
import glob

ListOfFiles=os.listdir('../images')
for x in ListOfFiles:
    image = Image.open("../images/"+x)
    print(x)
    resized_image = image.resize((219,219))
    resized_image = resized_image.convert("RGB")
    resized_image.save('doctors_testing/'+x)
        
# image = Image.open('../images/small-39941552906266.jpg')
# print(image.size)

# resized_image = image.resize((219,219))
# resized_image.save('resizedImage.jpg')
# print(resized_image.size)