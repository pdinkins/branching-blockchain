import requests
from io import BytesIO
from PIL import Image


r = requests.get(input("enter url:"))
print(r.status_code)

image = Image.open(BytesIO(r.content))


print(image.size, image.format, image.mode)
path = "./image5." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("image cannot be saved")

