# Header 
magic = "P3"
author = "# Created by Shawn Wilkinson"
size_x, size_y = (320, 240)
inten = 255

# Open/Create File and Add Header
f = open('1.4pe2.ppm', 'w+')
f.write(magic + "\n")
f.write(author + "\n")
f.write(str(size_x) + " " + str(size_y) + "\n")
f.write(str(inten) + "\n")

# Write Image
color = (255, 0, 0)
for y in range(size_y):
	for x in range(size_x):
		f.write( str(color[0]) + " " + str(color[1]) + " " + str(color[2]) + " ")
	f.write("\n")