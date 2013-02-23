#!/usr/bin/env python
# Filename: Line3D.py
# Project Github: http://github.com/super3/ClassDev
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports 
from GeoPrimitives import Image
from GeoPrimitives import Line

# Line 3D
class Line3D:
	# Constructor
	def __init__(self, start_pt, end_pt):
		# Private Vars
		self.start_pt = start_pt
		self.end_pt = end_pt

	# Equations
	def eq(self, xya, za, d):
		"""Works for Equation 4.1 and 4.2."""
		return (xya/za) * d
	def eq43(self):
		pass

	def project(self, d):
		"""
		A simple projection algorithm to project the vertex points of a 3D line
		segment onto a view plane located at z = d, for a center of projection at the
		origin (0,0,0), is outlined in the following steps:

		"""

		# 1. Project the x-values of the start and end points to the view plane using
		# Equation 4.2
		x1 = self.eq(self.start_pt[0], self.start_pt[2], d)
		y1 = self.eq(self.start_pt[1], self.start_pt[2], d)
		# 2. Project the y-values of the start and end points to the view plane using
		# Equation 4.1
		x2 = self.eq(self.end_pt[0], self.end_pt[2], d)
		y2 = self.eq(self.end_pt[1], self.end_pt[2], d)
		
		return Line(x1, y1, x2, y2)

	def display(self, translate, scale):
		"""
		For a translation location at (xL, yL) and a scale factor of sf , a simple
		display algorithm to display points projected onto a view plane (as describe
		in section 4.2) as 2D lines is as follows:

		"""

		pass
		# 1. Find the center of the 2D points using Equations 4.3 and 4.4.
		# 2. Translate the start and end points of each line using the
		# translation algorithm in section 3.1, where xt and yt are found from Equations 4.5 and 4.6
		# 3. Scale the translated start and end points from Step 2 by Sx = sf and Sy = sf for a fix point of (xL, yL) 
		# using the scale algorithm in section 3.3.
		# 4. Find the points between each start and end point using the line algorithm in section 2.1

	# Draw Functions
	def draw(self, d):
		pass


# Unit Tests
if __name__ == "__main__":
	line1 = Line3D( (35,40,70), (20,30,50) ) # d = 20
	print( line1.project(20) )
	# Output: Projected Start-Point = (10, 11.43), Projected End-Point = (8, 12)

	line2 = Line3D( (35,40,70), (20,30,50) ) # d = -20
	print( line1.project(-20) )
	# Output: Projected Start-Point = (−10, −11.43), Projected End-Point = (−8, −12)