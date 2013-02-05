# Imports
import math
from Primitives import *

# Circle Class
class Circle:
	def __init__(self, x, y, r, color=Color(0,0,0)):
		self.x = x 
		self.y = y
		self.r = r
		self.color = color
	def sym(self, points):
		new_points = []
		for pon in points:
			new_points.append( Point(pon.x, pon.y, pon.color) )
			new_points.append( Point(-pon.x, pon.y, pon.color) )
			new_points.append( Point(pon.x, -pon.y, pon.color) )
			new_points.append( Point(-pon.x, -pon.y, pon.color) )
			new_points.append( Point(pon.y, pon.x, pon.color) )
			new_points.append( Point(-pon.y, pon.x, pon.color) )
			new_points.append( Point(pon.y, -pon.x, pon.color) )
			new_points.append( Point(-pon.y, -pon.x, pon.color) )
		return new_points
	def center(self, points):
		new_points = []
		for pon in points:
			new_points.append( Point(pon.x+self.x, pon.y+self.y, pon.color) )
		return new_points
	def getPoints(self):
		solution = []
		# A simple circle algorithm is outlined in the following steps for a given center point (xc, yc) and radius r:
		# 1. Initialize starting point to (r, 0): x = r and y = 0
		x = self.r
		y = 0
		solution.append( Point(x,y,self.color) )

		while True:
			# 2. Compute the next y location for the first octant: y + 1
			y += 1
			# 3. Compute the corresponding x value (xa) for y + 1 using Equation 2.6
			x = math.sqrt( (math.pow(self.r, 2) - math.pow(y, 2)) )
			# 4. Round xa to the nearest integer value to find the next x-location
			x = round(x)
			solution.append( Point(x,y,self.color) )
			solution.append( Point(-x,y,self.color) )
			# 5. If x is greater than y, (Checking to see if points are still in first octant)
			# (a) go back to step 2 
			if x > y:
				pass
			# 6. If x is less than or equal to y,
			# (a) From the discovered points in the first octant, find the other points
			# on the circle by symmetry as shown in Figure 2.6.
			else:
				solution = self.sym(solution)
				break
				# 7. Add the center point (xc, yc) to all discovered points
		return self.center(solution)
	def __str__(self):
		string = ""
		for pon in self.getPoints():
			string += str(pon)
		return string

# Unit Test
if __name__ == "__main__":
	# Create a Blank Image
	img = Image(320, 240)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Line Objects
	circle1 = Circle( 160, 120, 100, Color(0,0,255) )
	# Blit and Create/Write Image
	img.blit( circle1.getPoints() )
	makePPM('test.ppm', img)