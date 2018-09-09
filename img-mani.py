# @author: Xavier Collantes
# @date: 09/8/2018
# @content: Ch. 17 from Al Sweigart's "How to Automate the Boring Stuff with Python"

from PIL import Image
from PIL import ImageColor
import os, arrow


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

	
def cutHalf():
	origin = Image.open('girls.jpg')
	w, h = origin.size
	half = origin.resize((int(w / 2), int(h / 2)))
	half.save('half.png')
	
	
	# Expand will move image dimension with rotation 
def turn(image, degree, bg=True):
	image.rotate(degree, expand=bg).save('rotate' + str(degree) + '.png')
	
	
def flip(img):
	img.transpose(Image.FLIP_LEFT_RIGHT).save('transpose_horizontal.png')
	img.transpose(Image.FLIP_TOP_BOTTOM).save('transpose_vertical.png')
	

def greenScreen(bg, gs):
	# Establish counter for green screen image 
	#countGS = (int(gs.size[0] - 1), int(gs.size[1] - 1))
	WIDTH = gs.size[0]
	HEIGHT = gs.size[1]
	pos = (0, 0)
	
	# Stop when smallest dimension is reached on green screen image 
	while pos[0] <= WIDTH:
	
		while pos[1] <= HEIGHT:
			print("processing pixel: ", pos)

			if gs.getpixel(pos)[1] > 170:  # If pixel on green screen image is somewhat green 
				print("change pixel: ", pos)
				
				frontColor = bg.getpixel(pos)  # Get corresponding pixel color of the same coordinates 
				gs.putpixel(pos, frontColor)
			else:
				pass
			
			pos[1] += 1  # Increment height by 1

		pos[1] = 0
		pos[0] += 1  # Increment width by 1

	
	gs.save(arrow.now('US/Pacific').format('DD-MMM-YY_HH-mm-SS') + '.png')
	
if __name__=='__main__':
	os.chdir('lib/')
	i = Image.open('girls.jpg')
	#pillow()
	#tile()
	#cutHalf()
	#turn(i, 90)
	#turn(i, 180)
	
	#flip(i)
	back = Image.open('transpose_horizontal.png')
	shia = Image.open('shia.jpg')
	greenScreen(back, shia)
	