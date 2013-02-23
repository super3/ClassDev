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

	def display(self, d, translate, scale):
		"""
		For a translation location at (xL, yL) and a scale factor of sf, a simple
		display algorithm to display points projected onto a view plane (as describe
		in section 4.2) as 2D lines is as follows:

		"""

		tmp_line = self.project(d)
		# 1. Find the center of the 2D points using Equations 4.3 and 4.4.
		xc, yc = tmp_line.get_center()
		# 2. Translate the start and end points of each line using the translation algorithm in
		# section 3.1, where xt and yt are found from Equations 4.5 and 4.6
		tmp_line.translate(translate[0]-xc, translate[1]-yc)
		# 3. Scale the translated start and end points from Step 2 by Sx = sf and Sy = sf for a fix point of (xL, yL) 
		# using the scale algorithm in section 3.3.
		tmp_line.scale_eq(translate[0], translate[1], scale)
		# 4. Find the points between each start and end point using the line algorithm in section 2.1
		return tmp_line

	def view(self, a, b):
		"""
		A simple 3D view algorithm to define a view for a 3D environment given
		α and β is outlined in the following steps:

		"""

		# 1. Initialize ~u to (1, 0, 0), ~v to (0, 1, 0), and ~n to (0, 0, 1)
		# 2. Rotate ~u by β using Equations 4.19, 4.20, and 4.21
		# 3. Rotate ~v by β using Equations 4.22, 4.23, and 4.24
		# 4. Rotate ~n by β using Equations 4.25, 4.26, and 4.27
		# 5. Rotate the result of step 2 by α using Equations 4.10, 4.11, and 4.12
		# 6. Rotate the result of step 3 by α using Equations 4.13, 4.14, and 4.15
		# 7. Rotate the result of step 4 by α using Equations 4.16, 4.17, and 4.18
		pass

# Unit Tests
if __name__ == "__main__":
	line0 = Line3D( (35,40,70), (20,30,50) ) # d = 20, translate (160, 120), scale = 10
	print( line0.display(20, (160,120), 10) )
	# Output: Displayed Start-Point = (170, 117), Displayed End-Point = (150, 123)

	print("")

	line1 = Line3D( (35,40,70), (20,30,50) ) # d = 20, translate (500, 500), scale = 10
	line2 = Line3D( (55,40,20), (30,50,10) )
	print( line1.display(20, (500,500), 10) )
	print( line2.display(20, (500,500), 10) )
	# Output: Line 1 – Displayed Start-Point = (260, 57), and Displayed End-Point = (240, 63); 
	# 		  Line 2 – Displayed Start-Point = (710, 343), and Displayed End-Point = (760, 943)