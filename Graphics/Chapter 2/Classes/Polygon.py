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

	def eq24(self, x1, y1, x2, y2, y):
		return self.getSlope(x1, y1, x2, y2)*y - self.getSlope(x1, y1, x2, y2)*y1 + x1

	def draw_border(self):
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

	def scan_line(self, a):
		"""
		A simple scan-line intersection algorithm to compute the intersection
	 	of a scan line y = a and an edge – with vertex points (x1, y1) and (x2, y2)
	 	from the polygon's list of vertex points.

		"""
		solution = []

		for i in range(len(self.point_list)):

			# Two vertex points to local vars
			x1 = self.point_list[i][0]
			y1 = self.point_list[i][1]
			x2 = self.point_list[(i+1)%len(self.point_list)][0]
			y2 = self.point_list[(i+1)%len(self.point_list)][1]
			
			# This is a horizontal line, so there is not an intersection
			if y2 - y1 == 0: continue
			else:
				# The scan line is outside of the edge, so there is not an intersection
				if not (min(y1,y2) <= a and max(y1,y2) >= a): continue 
				
				# Find the y-value of the maximal vertex point
				y_max = max(y1,y2)
				
				# The scan line intersects a maximal vertex-point, so there is not an intersection
				if a == y_max: continue
				else:
					# Find the x-value of the intersect for y = a using Equation 2.4
					x_val = round(self.eq24(x1, y1, x2, y2, a))
					solution.append( (x_val, a) )

		return solution

	def draw_inside(self):
		point_pairs = []
		solution = []

		# Find the min y-value (ymin) and the max y-value (ymax)
		min_y = min(y[1] for y in self.point_list)
		max_y = max(y[1] for y in self.point_list)

		# Use the scan-line intersection algorithm to find intersections
		for a in range(min_y, max_y):
			tmp = self.scan_line(a)
			# sort intersections from minimal to maximal value based on the x values
			tmp.sort( key=operator.itemgetter(0) ) 
			if len(tmp) > 0: point_pairs.extend( tmp ) 

		# If there are intersections
		if len(point_pairs) > 0:
			# Fill in pixels between adjacent pairs of intersection points
			for i in range(0, len(point_pairs)-1, 2):
				solution.extend( Line(point_pairs[i][0], point_pairs[i][1], point_pairs[i+1][0], point_pairs[i+1][1]).draw() )	

		return solution

	def fill(self, color = None):
		self.inside = self.draw_inside()
		if color == None: self.inside_color = self.border_color
		else: self.inside_color = color

# Unit Testing
if __name__ == "__main__":
	# Create Blank Image
	img = Image(150, 350)
	# Fill Image with Color
	img.fill( Color(245, 245, 245) )
	# Create Polygon
	point_list = [ (10, 10), (100, 10), (100, 300), (10, 150), (80, 150), (80, 50), (20, 50), (20, 100), (10, 100) ]
	polygon1 = Polygon( point_list, Color(0,0,0) )
	polygon1.fill( Color(255,0,255) )
	# Blit and Create/Write Image
	img.blit( polygon1 )
	makePPM('test.ppm', img)

	