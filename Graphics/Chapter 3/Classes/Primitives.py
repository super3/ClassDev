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
	# Magic Functions
	def __init__(self, color=Color(0,0,0)):
		"""Base class for Geometric Primitives."""
		self.border_color = color
		self.inside_color = color
		self.border = []
		self.inside = []
		self.do_fill = False
	def __str__(self):
		"""Returns a string containing all the points in the shape."""
		output = ""
		for a_point in self.points:
			output += str(a_point) + ", "
		return output

	# Drawing Functions
	def draw(self):
		"""Calculates a shape's points, and stores it."""
		self.border = self.draw_border()
		if self.do_fill: self.inside = self.draw_inside()
	def draw_border(self):
		"""Calculates a shape's border points."""
		raise NotImplementedError
	def draw_inside(self):
		"""Calculates a shapes's inside points (or fill)."""
		raise NotImplementedError
	def fill(self, color = None):
		self.do_fill = True
		if color == None: self.inside_color = self.border_color
		else: self.inside_color = color
		return self

	# Cleanup Function
	def remove_duplicates(self, points):
		"""Removes duplicates from a list by converting it to a set then back to a list."""
		return list(set(points))
	
	# Transformations
	def move(self, x, y):
		"""Translate any shape."""

		# Temp Vars
		tmp_border = []
		tmp_inside = []

		# Translate
		for point in self.border:
			tmp_border.append( (point[0]+x, point[1]+y) )
		for point in self.inside:
			tmp_border.append( (point[0]+x, point[1]+y) )	

		# Save Translated Data
		self.border = tmp_border
		self.inside = tmp_inside

	def translate(self, x, y):
		raise NotImplementedError
	def rotate(self, x, y, angle):
		raise NotImplementedError
	def scale(self, x, y, factor):
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
		# Calculate Object's Points
		shapeObj.draw()
		# Draw Object on Image
		for point in shapeObj.inside:
			self.img[ self.getIndex(point[0], point[1]) ] = shapeObj.inside_color
		for point in shapeObj.border:
			self.img[ self.getIndex(point[0], point[1]) ] = shapeObj.border_color

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