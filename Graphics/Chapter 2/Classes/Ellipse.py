# Imports
import math
from Primitives import *

# Ellipse Class
class Ellipse:
	def __init__(self, x, y, a, b, color=Color(0,0,0)):
		self.x = x
		self.y = y
		self.a = a # major
		self.b = b # minor
		self.color = color
	def __str__(self):
		string = ""
		for pon in self.getPoints():
			string += str(pon)
		return string
	def sym(self, points):
		new_points = []
		for pon in points:
			new_points.append( Point(pon.x, pon.y, pon.color) )
			new_points.append( Point(-pon.x, pon.y, pon.color) )
			new_points.append( Point(pon.x, -pon.y, pon.color) )
			new_points.append( Point(-pon.x, -pon.y, pon.color) )
		return new_points
	def center(self, points):
		new_points = []
		for pon in points:
			new_points.append( Point(pon.x+self.x, pon.y+self.y, pon.color) )
		return new_points
	def getPoints(self):
		solution = []
		# 1. Initialize starting point to (a, 0): x = a and y = 0
		x = self.a
		y = 0
		solution.append( Point(x,y,self.color) )
		# 2. If a2(y + 1) < b2(x − .5), (In region 2)
		while (math.pow(self.a,2) * (y + 1)) < (math.pow(self.b,2) * (x - 0.5)):
			# (a) Compute the next y location for region 2: y + 1
			y += 1
			# (b) Compute the x value (xa) for y + 1 using Equation 2.8
			x = math.sqrt(math.pow(self.a,2) * (1-(1/math.pow(self.b,2))*math.pow(y,2)))
			# (c) Round xa to the nearest integer
			x = round(x)
			solution.append( Point(x,y,self.color) )
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
			solution.append( Point(x,y,self.color) )
			# 4. From the discovered points in the first quadrant, find the other points on
			# the ellipse by symmetry as shown in Figure 2.8.
			# 5. Add the center point (xc, yc) to all discovered points
		solution = self.sym(solution)
		return self.center(solution)
# Unit Testing
if __name__ == "__main__":
	# Create Blank Image
	img = Image(320, 240)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Line Objects
	ellipse1 = Ellipse( 160, 120, 50, 100, Color(0,0,0) )
	# Blit and Create/Write Image
	img.blit( ellipse1.getPoints() )
	makePPM('test.ppm', img)