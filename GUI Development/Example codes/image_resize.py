'''
Example code to resize the image
'''

from tkinter import *
from PIL import Image


# enter the image path
myimage = Image.open('/home/pi/Downloads/twitter.png')

# in resize write height and width
myimage = myimage.resize((200,200), Image.ANTIALIAS)

# save image in current directory in png format
final = myimage.save('image1', 'png')

# save image in current directory in png format
final = myimage.save('image2', 'ppm')
