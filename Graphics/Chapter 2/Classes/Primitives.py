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
	def __init__(self, x, y, color=Color(0,0,0)):
		self.x = x
		self.y = y
		self.color = color
	def __str__(self):
		return "(%s,%s)" % (self.x,self.y)
	def getIndex(self, size_x, size_y):
		# I = x + xd(yd − y − 1) + 1
		return self.x + size_x * ( size_y - self.y - 1 ) - 1

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
	def blit(self, points):
		for point in points:
			self.img[ point.getIndex(self.x, self.y) ] = point.color

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