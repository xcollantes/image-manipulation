# @author: Xavier Collantes
# @date: 09/8/2018
# @content: Ch. 17 from Al Sweigart's "How to Automate the Boring Stuff with Python"

from PIL import Image
import os, sys

def pillow():
	img = Image.open('girls.jpg')
	print (img.size)
	print (img.filename)
	print (img.format)
	print (img.format_description)
	




if __name__=='__main__':
	os.chdir('lib/')
	pillow()