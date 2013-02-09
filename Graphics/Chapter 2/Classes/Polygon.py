# Imports
import operator
from Primitives import *
from Line import Line

# Polygon Class
class Polygon(Shape):
	def __init__(self, point_list, color=Color(0,0,0)):
		# Private Vars
		self.point_list = point_list
		# Color and Points
		super(Polygon, self).__init__(color)

	def draw(self):
		# A simple polygon algorithm is outlined in the following steps for n vertex
		# points [(x1, y1), (x2, y2), ..., (xn, yn)], listed in the order to be connected:
		solution = []
		# 1. Use the line algorithm in section 2.1 to draw a line between adjacent points in the order listed
		for i in range(len(self.point_list)-1):
			x1 = self.point_list[i][0]
			y1 = self.point_list[i][1]
			x2 = self.point_list[i+1][0]
			y2 = self.point_list[i+1][1]
			solution.extend( Line(x1, y1, x2, y2).draw() )
		# 2. Use the line algorithm in section 2.1 to draw a line between the last point in the list and the first point
		x1 = self.point_list[0][0]
		y1 = self.point_list[0][1]
		x2 = self.point_list[len(self.point_list)-1][0]
		y2 = self.point_list[len(self.point_list)-1][1]
		solution.extend( Line(x1, y1, x2, y2).draw() )
		solution = self.remove_duplicates(solution)
		return solution

	def scan_line(self):
		"""
		A simple scan-line intersection algorithm to compute the intersection
	 	of a scan line y = a and an edge – with vertex points (x1, y1) and (x2, y2)
	 	– is outlined in the following steps:

	 	"""
	 	# Find the absolute boundaries of the primitive
		min_y = min(y[1] for y in self.point_list)
		max_y = max(y[1] for y in self.point_list)

		for i in range(self.point_list-1):
			y1 = self.point_list[i][1]
			y2 = self.point_list[i+1][1]
			# 1. If y2 − y1	= 0,
			if y2 - y1 == 0:
				# (a) This is a horizontal line, so there is not an intersection
				pass
			else:
				# 2. If y2 − y1	=/= 0
				# (a) If a is not in the range from y1 to y2
			#	 i. The scan line is outside of the edge, so there is not an intersection
				# (b) Find the y-value of the maximal vertex point
				# i. if y1 ≥ y2, y-maximal = y1
				# ii. if y1	< y2, y-maximal = y2
				# (c) If a = y-maximal
				# i. The scan line intersects a maximal vertex-point, so there is not an intersection
				# (d) If a 6 = y-maximal and is in the range from y1 to y2
				#i. Find the x-value of the intersect for y = a using Equation 2.4
				#ii. Round the x-value to the nearest integer

	def fill(self):
		# Find the absolute boundaries of the primitive
		min_y = min(y[1] for y in self.points)
		max_y = max(y[1] for y in self.points)
		# For each row of the primitive, find the boundary pixels
		for row in range( min_y, max_y ):
			bound_min = min((y for y in self.points if y[1]==row), key=operator.itemgetter(0))
			bound_max = max((y for y in self.points if y[1]==row), key=operator.itemgetter(0))
			# For each row, fill in the pixels between boundary pixels
			self.points.extend( Line(bound_min[0], bound_min[1], bound_max[0], bound_max[1]).draw() )

# Unit Testing
if __name__ == "__main__":
	# Create Blank Image
	img = Image(320, 240)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Polygon
	point_list = [ (60,120), (110,200), (110,150), (200,220), (160,120) ]
	polygon1 = Polygon( point_list, Color(255,0,255) )
	polygon1.fill()
	# Blit and Create/Write Image
	img.blit( polygon1 )
	makePPM('test.ppm', img)