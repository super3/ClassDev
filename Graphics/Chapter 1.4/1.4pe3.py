# Header 
magic = "P3"
author = "# Created by Shawn Wilkinson"
size_x, size_y = (100, 100)
inten = 255

# Open/Create File and Add Header
f = open('1.4pe3.ppm', 'w+')
f.write(magic + "\n")
f.write(author + "\n")
f.write(str(size_x) + " " + str(size_y) + "\n")
f.write(str(inten) + "\n")

# Define Colors
red  = (255, 0, 0)
blue = (0, 0, 255)

# Write Images
for q in range(10):
	for w in range(10):
		for j in range(50):
			for x in range(10):
				f.write( str(red[0]) + " " + str(red[1]) + " " + str(red[2]) + " ")
			for x in range(10):
				f.write( str(blue[0]) + " " + str(blue[1]) + " " + str(blue[2]) + " ")
			f.write("\n")
		for j in range(50):
			for x in range(10):
				f.write( str(blue[0]) + " " + str(blue[1]) + " " + str(blue[2]) + " ")
			for x in range(10):
				f.write( str(red[0]) + " " + str(red[1]) + " " + str(red[2]) + " ")
			f.write("\n")