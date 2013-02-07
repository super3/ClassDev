# Imports
from Primitives import *
from Ellipse import Ellipse

# Circle Class
class Circle(Ellipse):
	def __init__(self, x, y, r, color=Color(0,0,0)):
		super(Circle, self).__init__(x,y,r,r,color)

# Unit Test
if __name__ == "__main__":
	# Create a Blank Image
	img = Image(320, 240)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Circle Object
	circle1 = Circle( 160, 120, 100, Color(0,0,255) )
	circle1.fill()
	# Blit and Create/Write Image
	img.blit( circle1 )
	makePPM('test.ppm', img)