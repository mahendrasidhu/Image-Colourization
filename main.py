from model_loader import load_model
from colorizer import load_image

net = load_model()

image = load_image("BW_image.jpg")

print(type(image))
print(image.shape)
print(image.dtype)
print(image.shape)

print(image[0,0])

print(image[100,100])

print(image[300,400])