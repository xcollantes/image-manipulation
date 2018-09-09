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
	
	
def tile():
	x = 320
	y = 160
	i = Image.open('girls.jpg')
	cropped = i.crop((x, 0, x + 500, y + 500))
	cropped.save('sample.png')
	
	#cropped.paste(i, (50, 50))
	#cropped.save('sample.png')



if __name__=='__main__':
	os.chdir('lib/')
	#pillow()
	tile()
	