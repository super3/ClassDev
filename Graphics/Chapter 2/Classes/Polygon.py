# Imports
from Primitives import *
from Line import Line

# Polygon Class
class Polygon(Shape):
	def __init__(self, point_list, color=Color(0,0,0)):
		# Private Vars
		self.point_list = point_list
		# Color and Points
		super(Polygon, self).__init__(color)

	def draw(self):
		# A simple polygon algorithm is outlined in the following steps for n vertex
		# points [(x1, y1), (x2, y2), ..., (xn, yn)], listed in the order to be connected:
		solution = []
		# 1. Use the line algorithm in section 2.1 to draw a line between adjacent points in the order listed
		for i in range(len(self.point_list)-1):
			x1 = self.point_list[i][0]
			y1 = self.point_list[i][1]
			x2 = self.point_list[i+1][0]
			y2 = self.point_list[i+1][1]
			print( (x1, y1, x2, y2) )
			print( Line(x1, y1, x2, y2).draw() )
			solution.extend( Line(x1, y1, x2, y2).draw() )
		# 2. Use the line algorithm in section 2.1 to draw a line between the last point in the list and the first point
		x1 = self.point_list[0][0]
		y1 = self.point_list[0][1]
		x2 = self.point_list[len(self.point_list)-1][0]
		y2 = self.point_list[len(self.point_list)-1][1]
		solution.extend( Line(x1, y1, x2, y2).draw() )
		return solution

# Unit Testing
if __name__ == "__main__":
	# Create Blank Image
	img = Image(320, 240)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Polygon
	point_list = [ (60,120), (110,200), (110,150), (200,220), (160,120) ]
	polygon1 = Polygon( point_list, Color(255,0,255) )
	# Blit and Create/Write Image
	img.blit( polygon1 )
	makePPM('test.ppm', img)