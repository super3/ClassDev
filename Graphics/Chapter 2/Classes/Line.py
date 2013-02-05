# Imports
from Classes.Primitives import *

# Line Class
class Line:
	def __init__(self, x1, y1, x2, y2, color=Color(0,0,0)):
		# Points
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.color = color

	def getSlopeLong(self):
		return (self.y2 - self.y1) / (self.x2 - self.x1)

	def getSlopeTall(self):
		return (self.x2 - self.x1) / (self.y2 - self.y1)

	def getIntercept(self):
		return ( -(self.getSlopeLong()) )*self.x1 + self.y1

	def getPoints(self):
		"""Return list of points based on the line algorithm."""
		# Solution List
		solution = []

		# 1. Find the x length |x1 − x2| and the y length |y1 − y2|
		x_len = abs(self.x1 - self.x2)
		y_len = abs(self.y1 - self.y2)

		# 2. If the x length is longer
		if x_len > y_len:
			# (a) Find all the integer values from x1 to x2: [x1...x2]
			x_vals = []
			for x in range(self.x1, self.x2+1):
				x_vals.append(x)
			# (b) Solve for the corresponding y values using Equation 2.1: [y1...y2]
			# (c) Round the y values to the nearest integer value
			for x in x_vals:
				y = (self.getSlopeLong() * x) + self.getIntercept()
				solution.append( Point(x, round(y), self.color) )

		#3. If the y length is longer 
		else:
			# (a) Find all the integer values from y1 to y2: [y1...y2]
			y_vals = []
			for y in range(self.y1, self.y2+1):
				y_vals.append(y)
			# (b) Solve for the corresponding x values using Equation 2.4: [x1...x2]
			# (c) Round the x values to the nearest integer value
			for y in y_vals:
				x = self.getSlopeTall()*y - self.getSlopeTall()*self.y1 + self.x1
				solution.append( Point(round(x), y, self.color) )

		return solution
	def draw(self):
		print(self.getPoints())