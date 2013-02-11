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

	def getSlope(self, x1, y1, x2, y2):
		return (x2 - x1) / (y2 - y1)

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
		solution.extend( self.fill() )
		return solution

	def scan_line(self, a):
		"""
		A simple scan-line intersection algorithm to compute the intersection
	 	of a scan line y = a and an edge – with vertex points (x1, y1) and (x2, y2)
	 	– is outlined in the following steps:

		"""
		solution = []

		for i in range(len(self.point_list)-1):
			x1 = self.point_list[i][0]
			y1 = self.point_list[i][1]
			x2 = self.point_list[i+1][0]
			y2 = self.point_list[i+1][1]
			# 1. If y2 − y1	= 0,
			if y2 - y1 == 0:
				# (a) This is a horizontal line, so there is not an intersection
				continue
			# 2. If y2 − y1	=/= 0
			else:
				# (a) If a is not in the range from y1 to y2
				if not (min(y1,y2) <= a and max(y1,y2) >= a):
					continue 
			 	# i. The scan line is outside of the edge, so there is not an intersection
				
				# (b) Find the y-value of the maximal vertex point
				y_max = max(y1,y2)
				
				# (c) If a = y-maximal
				# i. The scan line intersects a maximal vertex-point, so there is not an intersection
				if a == y_max:
					continue
				# (d) If a =/= y-maximal and is in the range from y1 to y2
				else:
					#i. Find the x-value of the intersect for y = a using Equation 2.4
					x_val = self.getSlope(x1, y1, x2, y2)*a - self.getSlope(x1, y1, x2, y2)*y1 + x1
					#ii. Round the x-value to the nearest integer
					#print(x_val)
					solution.append( (round(x_val), a) )

		return solution

	def fill(self):
		solution = []

		# 1. Find the min y-value (ymin) and the max y-value (ymax)
		min_y = min(y[1] for y in self.point_list)
		max_y = max(y[1] for y in self.point_list)
		# 2. For all the scan lines from ymin to ymax (integers values only)

		# (a) For each edge
		# i. Use the scan-line intersection algorithm to find intersec-tions
		for a in range(min_y, max_y):
			solution.extend( self.scan_line(a) )

		# ii. If there are intersections
		if len(solution) > 0:
			# A. Sort intersections from minimal to maximal value based on
			# the x values of the intersection points
			solution.sort( key=operator.itemgetter(1) )
			# B. Fill in pixels between adjacent pairs of intersection points
			#print(solution)
			#return solution
			pairs = []
			for i in range(len(solution)-1):
				pairs.extend( Line(solution[i][0], solution[i][1], solution[i+1][0], solution[i+1][1]).draw() )
			# 3. Use the polygon algorithm in section 2.4 to fill in the border pixels of
			# the polygon	
			return pairs
		

# Unit Testing
if __name__ == "__main__":
	# Create Blank Image
	img = Image(320, 240)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Polygon
	point_list = [ (60,120), (110,200), (110,150), (200,220), (160,120) ]
	polygon1 = Polygon( point_list, Color(255,0,255) )
	#polygon1.fill()
	# Blit and Create/Write Image
	img.blit( polygon1 )
	makePPM('test.ppm', img)
	# verts = [(10,10), (20,30)]
	# print( polygon1.scan_line(verts, 1) )