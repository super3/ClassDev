# Pixel Class
class Color:
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

# Line Class
class Line:
	def __init__(self, x1, y1, x2, y2):
		# Points
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2

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
				solution.append( (x, round(y)) )

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
				solution.append( (round(x), y) )

		return solution
	def draw(self):
		print(self.getPoints())

# Image Class
class Image:
	def __init__(self, size_x, size_y, inten):
		self.x = size_x
		self.y = size_y
		self.inten = inten
		self.img = []
	def fill(self, color):
		for y in range(self.y):
			for x in range(self.x):
				self.img.append( color )
	def blit(self, points):
		for point in points:
			self.img[ point.getIndex(self.x, self.y) ] = Color(0, 0 ,0)

# PPM Creation Functions
def header(x, y, inten):
	"""Returns the header string for a PPM file."""
	head = "P3\n"
	head += "# Created by Shawn Wilkinson\n"
	head += str(x) + " " + str(y) + "\n"
	head += str(inten) + "\n"
	return head

def makePPM(filename, img):
	"""Write to a PPM file."""
	f = open(filename, 'w+')
	f.write(header(img.x, img.y, img.inten))
	for pix in img.img:
		f.write(str(pix))
	f.close()

# Unit Testing
if __name__ == "__main__":
	img = Image(320, 240, 255)
	img.fill( Color(245, 245, 245) )
	img.blit( [Point(50, 50)] )
	makePPM('test.ppm', img)