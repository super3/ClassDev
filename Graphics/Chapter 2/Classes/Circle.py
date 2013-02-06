# Imports
import math
from Primitives import *

# Circle Class
class Circle(Shape):
	def __init__(self, x, y, r, color=Color(0,0,0)):
		# Private Vars
		self.x = x 
		self.y = y
		self.r = r
		# Color and Points
		super(Circle, self).__init__(color)

	def sym(self, points):
		"""Uses symmetry to find the other parts of the circle."""
		new_points = []
		for point in points:
			new_points.append( (point[0], point[1])   )
			new_points.append( (-point[0], point[1])  )
			new_points.append( (point[0], -point[1])  )
			new_points.append( (-point[0], -point[1]) )
			new_points.append( (point[1], point[0])   )
			new_points.append( (-point[1], point[0])  )
			new_points.append( (point[1], -point[0])  )
			new_points.append( (-point[1], -point[0]) )
		return new_points

	def center(self, points):
		"""Positions found points around the shape center."""
		new_points = []
		for point in points:
			new_points.append( (point[0]+self.x, point[1]+self.y) )
		return new_points


	def draw(self):
		solution = []
		# A simple circle algorithm is outlined in the following steps for a given center point (xc, yc) and radius r:
		# 1. Initialize starting point to (r, 0): x = r and y = 0
		x = self.r
		y = 0
		solution.append( (x,y) )

		while True:
			# 2. Compute the next y location for the first octant: y + 1
			y += 1
			# 3. Compute the corresponding x value (xa) for y + 1 using Equation 2.6
			x = math.sqrt( (math.pow(self.r, 2) - math.pow(y, 2)) )
			# 4. Round xa to the nearest integer value to find the next x-location
			x = round(x)
			solution.append( (x,y) )
			solution.append( (-x,y) )
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

# Unit Test
if __name__ == "__main__":
	# Create a Blank Image
	img = Image(320, 240)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Circle Object
	circle1 = Circle( 160, 120, 100, Color(0,0,255) )
	# Blit and Create/Write Image
	img.blit( circle1 )
	makePPM('test.ppm', img)