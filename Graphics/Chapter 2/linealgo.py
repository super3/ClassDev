# Pixel Class
class Pixel:
	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b
	def __str__(self):
		return "%s %s %s " % (str(self.r), str(self.g), str(self.b))

# Point Class
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __str__(self):
		return "(%s,%s)" % (self.x,self.y)
	def getIndex(self, size_x, size_y):
		# I = x + xd(yd − y − 1) + 1
		return self.x + size_x * ( size_y - self.y - 1 ) - 1

class Line:
	def __init__(self, x1, y1, x2, y2):
		# Points
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

		# Equation Vars
		self.m = self.getSlope()
		self.b = self.getIntercept()

		print(self.m)
		print(self.b)

	def getSlope(self):
		return (self.y2 - self.y1) / (self.x2 - self.x1)

	def getIntercept(self):
		return ( -(self.getSlope()) )*self.x1 + self.y1

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
			for x in x_vals:
				pass
			# (c) Round the y values to the nearest integer value

		return solution

# PPM Creation Functions
def header(x, y, inten):
	"""Returns the header string for a PPM file."""
	head = "P3\n"
	head += "# Created by Shawn Wilkinson\n"
	head += str(x) + " " + str(y) + "\n"
	head += str(inten) + "\n"
	return head

def makePPM(filename, x, y, inten, img):
	"""Write to a PPM file."""
	f = open(filename, 'w+')
	f.write(header(x, y, inten))
	# write pixel image here
	# close file here

# Unit Testing
if __name__ == "__main__":
	makePPM('test.ppm', 50, 50, 255, None)
	# pix = Pixel(10,10,10)
	# print(pix)
	# pon = Point(10,10)
	# print(pon)
	lin = Line(2, 2, 6, 2)