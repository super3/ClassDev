# Pixel Class
class Color:
	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b
	def __str__(self):
		return "%s %s %s " % (str(self.r), str(self.g), str(self.b))

# Shape Class
class Shape(object):
	def __init__(self, color=Color(0,0,0)):
		"""Base class for Geometric Primitives."""
		self.color = color # color obj
		self.points = self.draw()
	def __str__(self):
		"""Returns a string containing all the points in the shape."""
		output = ""
		for a_point in self.points:
			output += str(a_point) + ", "
		return output
	def remove_duplicates(self, points):
		return list(set(points))
	def draw(self):
		"""Calculates a shape's points, and stores it."""
		raise NotImplementedError

# Image Class
class Image:
	def __init__(self, size_x, size_y, inten = 255):
		self.x = size_x
		self.y = size_y
		self.inten = inten
		self.img = []
	def fill(self, color):
		for y in range(self.y):
			for x in range(self.x):
				self.img.append( color )
	def getIndex(self, x, y):
		# I = x + xd(yd − y − 1) + 1
		return x + self.x * ( self.y - y - 1 ) - 1
	def blit(self, shapeObj):
		for point in shapeObj.points:
			self.img[ self.getIndex(point[0], point[1]) ] = shapeObj.color

# PPM Function
def makePPM(filename, img):
	"""Write to a PPM file."""
	head = "P3\n"
	head += "# Created by Shawn Wilkinson\n"
	head += str(img.x) + " " + str(img.y) + "\n"
	head += str(img.inten) + "\n"
	f = open(filename, 'w+')
	f.write(head)
	for pix in img.img:
		f.write(str(pix))
	f.close()