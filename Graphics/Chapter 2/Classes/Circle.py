# Imports
from Classes.Primitives import *

# Circle Class
class Circle:
	def __init__(self, x, y, r, color=Color(0,0,0)):
		self.x = x 
		self.y = y
		self.r = r
	def getPoints(self):
		pass
		# A simple circle algorithm is outlined in the following steps for a given center point (xc, yc) and radius r:
		# 1. Initialize starting point to (r, 0): x = r and y = 0
		# 2. Compute the next y location for the first octant: y + 1
		# 3. Compute the corresponding x value (xa) for y + 1 using Equation 2.6
		# 4. Round xa to the nearest integer value to find the next x-location
		# 5. If x is greater than y, (Checking to see if points are still in first octant)
		# (a) go back to step 2 
		# 6. If x is less than or equal to y,
		# (a) From the discovered points in the first octant, find the other points
		# on the circle by symmetry as shown in Figure 2.6.
		# 7. Add the center point (xc, yc) to all discovered points