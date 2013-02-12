# Imports
import math
from Primitives import *

# Line Class
class Line(Shape):
	def __init__(self, x1, y1, x2, y2, color=Color(0,0,0)):
		# Private Vars
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		# Color and Points
		super(Line, self).__init__(color)

	# Equations
	def getSlopeLong(self):
		return (self.y2 - self.y1) / (self.x2 - self.x1)

	def getSlopeTall(self):
		return (self.x2 - self.x1) / (self.y2 - self.y1)

	def getIntercept(self):
		return ( -(self.getSlopeLong()) )*self.x1 + self.y1

	# More Equations
	def eq37(self, x, y, angle):
		return (x * math.cos(angle)) - (y * math.sin(angle))
	def eq38(self, x, y, angle):
		return (y * math.cos(angle)) + (x * math.sin(angle))

	# Draw Functions
	def draw(self):
		return self.draw_border()

	def draw_border(self):
		solution = []

		# Find the x length |x1 − x2| and the y length |y1 − y2|
		x_len = abs(self.x1 - self.x2)
		y_len = abs(self.y1 - self.y2)

		if x_len > y_len:
			x_vals = []
			# Find all the integer values from x1 to x2: [x1...x2]
			for x in range(min(self.x1,self.x2+1), max(self.x1,self.x2+1)):
				x_vals.append(x)
			# Solve for the corresponding y values using Equation 2.1: [y1...y2]
			for x in x_vals:
				y = (self.getSlopeLong() * x) + self.getIntercept()
				solution.append( (x, round(y)) )
		else:
			y_vals = []
			# Find all the integer values from y1 to y2: [y1...y2]
			for y in range(min(self.y1,self.y2+1), max(self.y1,self.y2+1)):
				y_vals.append(y)
			# (b) Solve for the corresponding x values using Equation 2.4: [x1...x2]
			for y in y_vals:
				x = self.getSlopeTall()*y - self.getSlopeTall()*self.y1 + self.x1
				solution.append( (round(x), y) )

		return solution

	def draw_inside(self):
		return []

	# Transformations 
	def translation(self, x, y):
		self.x1 += x
		self.x2 += x
		self.y1 += y
		self.y2 += y
		self.border = self.draw()

	def rotate(self, x, y, angle):
		# 1. For each line
		# (a) Translate the end and start points by xt = −xr and yt = −yr using
		# the translation algorithm in section 3.1
		self.translation(-x,-y)
		x1 = self.x1
		x2 = self.x2
		y1 = self.y1
		y2 = self.y2
		# (b) Rotate the translated x-values β-degrees using Equation 3.7
		# (c) Round rotated x-values
		self.x1 = round(self.eq37(x1, y1, angle))
		self.x2 = round(self.eq37(x2, y2, angle))
		# (d) Rotate the translated y-values β-degrees using Equation 3.8
		# (e) Round rotated y-values
		self.y1 = round(self.eq38(x1, y1, angle))
		self.y2 = round(self.eq38(x2, y2, angle))
		# (f) Translate resulting points by xt = xr and yt = yr using the
		# translation algorithm in section 3.1
		# 2. Find the points for each new line using the line algorithm in section 2.1
		self.x1 += x
		self.x2 += x 
		self.y1 += y
		self.y2 += y 

		self.border = self.draw()

	def scale(self, x, y, factor):
		"""
		A simple scale algorithm to scale a line drawing by Sx and Sy for a fixed
		point (xf, yf) is outlined in the following steps:

		"""
		# 1. For each line
		# (a) Translate the end and start points by xt = −xf and yt = −yf	using
		# the translation algorithm in section 3.1
		self.translation(-x,-y)
		x1 = self.x1
		x2 = self.x2
		y1 = self.y1
		y2 = self.y2
		# (b) Scale the translated x-values by Sx	using Equation 3.9
		self.x1 = round(x1*factor)
		self.x2 = round(x2*factor)
		# (c) Round scaled x-values
		# (d) Scale the translated y-values by Sy	using Equation 3.10
		# (e) Round scaled y-values
		self.y1 = round(y1*factor)
		self.y2 = round(y2*factor)
		# (f) Translate resulting points by xt = xf and yt = yf using the
		# translation algorithm in section 3.1
		self.x1 += x
		self.x2 += x 
		self.y1 += y
		self.y2 += y 
		# 2. Find the points of each new line using the line algorithm in section 2.1
		self.border = self.draw()

# Unit Test
if __name__ == "__main__":
	# Create a Blank Image
	img = Image(320, 240)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Line Objects
	line1 = Line( 60, 120, 160, 120, Color(255, 0, 0) )
	line2 = Line( 160, 120, 160, 220, Color(0, 255, 0) )
	# Rotate
	line1.rotate( 160, 120, 45 )
	line2.rotate( 160, 120, 45 )
	# Scale
	line1.scale( 160, 120, .5 )
	line2.scale( 160, 120, .5 )
	# Translate
	line1.translation( 50, 50 )
	line2.translation( 50, 50 )
	# Blit and Create/Write Image
	img.blit( line1 )
	img.blit( line2 )
	makePPM('test.ppm', img) 