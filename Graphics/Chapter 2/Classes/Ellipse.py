# Imports
import math
from Primitives import *

# Ellipse Class
class Ellipse:
	def __init__(self, x, y, major, minor):
		self.x = x
		self.y = y
		self.major = major
		self.minor = minor
	def getPoints():
		pass
		# 1. Initialize starting point to (a, 0): x = a and y = 0
		# 2. If a2(y + 1) < b2(x − .5), (In region 2)
		# (a) Compute the next y location for region 2: y + 1
		# (b) Compute the x value (xa) for y + 1 using Equation 2.8
		# (c) Round xa to the nearest integer
		# (d) If a2	(y + 1) < b2(x − .5) (Still in region 2)
		# i. go back to step 2(a)
		# (e) If a2(y + 1) ≥ b2(x − .5), goto step 3
		# 3. Now in region 1
		# (a) Compute the next x location for region 1: x − 1
		# (b) Compute the y location (ya) for x − 1 using Equation 2.9
		# (c) Round ya to the nearest integer
		# (d) If x > 0, goto step 3(a) (Still in region 1)
		# 4. From the discovered points in the first quadrant, find the other points on
		# the ellipse by symmetry as shown in Figure 2.8.
		# 5. Add the center point (xc, yc) to all discovered points

# Unit Testing
if __name__ == "__main__":
	# Create Blank Image
	img = Image(320, 240)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Line Objects
	ellipse1 = Ellipse( 0, 0, 4, 2, Color(0,0,0) )
	# Blit and Create/Write Image
	img.blit( ellipse1.getPoints() )
	makePPM('test.ppm', img)