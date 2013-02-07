# Imports
import math
import operator
from Primitives import *
from Line import Line

# Ellipse Class
class Ellipse(Shape):
	def __init__(self, x, y, a, b, color=Color(0,0,0)):
		# Private Vars
		self.x = x
		self.y = y
		self.a = a # major
		self.b = b # minor
		# Color and Points
		super(Ellipse, self).__init__(color)

	def sym(self, points):
		"""Uses symmetry to find the other parts of the ellipse."""
		new_points = []
		for point in points:
			new_points.append( (point[0], point[1])   )
			new_points.append( (-point[0], point[1])  )
			new_points.append( (point[0], -point[1])  )
			new_points.append( (-point[0], -point[1]) )
		return new_points

	def center(self, points):
		"""Positions found points around the shape center."""
		new_points = []
		for point in points:
			new_points.append( (point[0]+self.x, point[1]+self.y) )
		return new_points

	def draw(self):
		solution = []
		# 1. Initialize starting point to (a, 0): x = a and y = 0
		x = self.a
		y = 0
		solution.append( (x,y) )
		# 2. If a2(y + 1) < b2(x − .5), (In region 2)
		while (math.pow(self.a,2) * (y + 1)) < (math.pow(self.b,2) * (x - 0.5)):
			# (a) Compute the next y location for region 2: y + 1
			y += 1
			# (b) Compute the x value (xa) for y + 1 using Equation 2.8
			x = math.sqrt(math.pow(self.a,2) * (1-(1/math.pow(self.b,2))*math.pow(y,2)))
			# (c) Round xa to the nearest integer
			x = round(x)
			solution.append( (x,y) )
			# (d) If a2	(y + 1) < b2(x − .5) (Still in region 2)
			# i. go back to step 2(a)
			# (e) If a2(y + 1) ≥ b2(x − .5), goto step 3
		# 3. Now in region 1
		while(x > 0):
			# (a) Compute the next x location for region 1: x − 1
			x -= 1
			# (b) Compute the y location (ya) for x − 1 using Equation 2.9
			y = math.sqrt(math.pow(self.b,2) * (1-(1/math.pow(self.a,2))*math.pow(x,2)))
			# (c) Round ya to the nearest integer
			y = round(y)
			# (d) If x > 0, goto step 3(a) (Still in region 1)
			solution.append( (x,y) )
			# 4. From the discovered points in the first quadrant, find the other points on
			# the ellipse by symmetry as shown in Figure 2.8.
			# 5. Add the center point (xc, yc) to all discovered points
		solution = self.sym(solution)
		solution = self.center(solution)
		solution = self.remove_duplicates(solution)
		return solution

	def fill(self):
		# Find the absolute boundaries of the primitive
		min_y = min(y[1] for y in self.points)
		max_y = max(y[1] for y in self.points)
		# For each row of the primitive, find the boundary pixels
		for row in range( min_y, max_y ):
			bound_min = min((y for y in self.points if y[1]==row), key=operator.itemgetter(0))
			bound_max = max((y for y in self.points if y[1]==row), key=operator.itemgetter(0))
			# For each row, fill in the pixels between boundary pixels
			self.points.extend( Line(bound_min[0], bound_min[1], bound_max[0], bound_max[1]).draw() )

# Unit Testing
if __name__ == "__main__":
	# Create Blank Image
	img = Image(320, 240)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Ellipse Object
	ellipse1 = Ellipse( 160, 120, 50, 100, Color(0,0,0) )
	ellipse1.fill()
	# Blit and Create/Write Image
	img.blit( ellipse1 )
	makePPM('test.ppm', img)