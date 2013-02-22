#!/usr/bin/env python
# Filename: Line3D.py
# Project Github: http://github.com/super3/ClassDev
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports 
from GeoPrimitives import Line

# Line 3D
class Line3D:
	# Constructor
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self
	def eq(self, xya, za, d):
		"""Works for Equation 4.1 and 4.2."""
		return (xya/za) * d
	def project(self):
		
