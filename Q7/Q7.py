# coding=utf-8
from PIL import Image

# res = get("http://www.pythonchallenge.com/pc/def/oxygen.png", stream=True)
image = Image.open('oxygen.png').convert('L')

width, height = image.size
print width, height

for y in range(image.size[0]):
    print image.getpixel((y, 45))

