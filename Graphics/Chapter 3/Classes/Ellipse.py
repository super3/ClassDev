# Imports
import math
import operator
from Primitives import *
from Line import Line

# Ellipse Class
class Ellipse(Shape):
	# Constructor
	def __init__(self, x, y, a, b, color=Color(0,0,0)):
		# Private Vars
		self.x = x
		self.y = y
		self.a = a # major
		self.b = b # minor
		# Color and Points
		super(Ellipse, self).__init__(color)

	# Ellipse Functions
	def sym(self, points):
		"""Uses symmetry to find the other parts of the ellipse."""
		new_points = []
		for point in points:
			new_points.append( ( point[0], point[1])  )
			new_points.append( (-point[0], point[1])  )
			new_points.append( ( point[0], -point[1]) )
			new_points.append( (-point[0], -point[1]) )
		return new_points

	def center(self, points):
		"""Positions found points around the ellipse center."""
		new_points = []
		for point in points:
			new_points.append( (point[0]+self.x, point[1]+self.y) )
		return new_points

	# Draw Functions
	def draw_border(self):
		solution = []

		# Initialize starting point to (a, 0): x = a and y = 0
		x = self.a
		y = 0
		solution.append( (x,y) )

		# If a2(y + 1) < b2(x − .5), (In region 2)
		while (math.pow(self.a,2) * (y + 1)) < (math.pow(self.b,2) * (x - 0.5)):
			# Compute the next y location for region 2: y + 1
			y += 1
			# Compute the x value (xa) for y + 1 using Equation 2.8
			x = round(math.sqrt(math.pow(self.a,2) * (1-(1/math.pow(self.b,2))*math.pow(y,2))))
			solution.append( (x,y) )
		# Now in region 1
		while(x > 0):
			# Compute the next x location for region 1: x − 1
			x -= 1
			# Compute the y location (ya) for x − 1 using Equation 2.9
			y = round(math.sqrt(math.pow(self.b,2) * (1-(1/math.pow(self.a,2))*math.pow(x,2))))
			solution.append( (x, y) )
			
		# From the discovered points in the first quadrant, find the other points by symmetry
		solution = self.sym(solution)
		# Add the center point (xc, yc) to all discovered points
		solution = self.center(solution)
		# Remove duplicates to be safe
		solution = self.remove_duplicates(solution)
		
		return solution

	def draw_inside(self):
		solution = []

		# Find the absolute boundaries of the primitive
		self.border = self.draw_border()
		min_y = min(y[1] for y in self.border)
		max_y = max(y[1] for y in self.border)
		# For each row of the primitive, find the boundary pixels
		for row in range( min_y, max_y ):
			bound_min = min((y for y in self.border if y[1]==row), key=operator.itemgetter(0))
			bound_max = max((y for y in self.border if y[1]==row), key=operator.itemgetter(0))
			# For each row, fill in the pixels between boundary pixels
			solution.extend( Line(bound_min[0], bound_min[1], bound_max[0], bound_max[1]).draw() )

		return solution

	# Transformations
	def translate(self, x, y):
		self.x += x
		self.y += y

	def rotate(self, x, y, angle):
		# One possible way this could work is forming a line from the center of the ellipse
		# to one of the border points. Then you apply your standard line rotation with the
		# center point being the rotation point. Unfortunately, you literally have to do this
		# for every single border point. 
		raise NotImplementedError

	def scale(self, x, y, factor):
		# This only scales on the center point.
		self.a *= factor
		self.b *= factor

# Unit Testing
if __name__ == "__main__":
	# Create Blank Image
	img = Image(320, 240)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Ellipse Object
	ellipse1 = Ellipse( 160, 120, 50, 100, Color(0,0,0)).fill( Color(0,255,0) )
	# Blit and Create/Write Image
	img.blit( ellipse1 )
	makePPM('test.ppm', img)