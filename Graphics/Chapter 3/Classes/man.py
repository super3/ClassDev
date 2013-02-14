# Imports
from Primitives import *
from Line import Line
from Ellipse import Ellipse
from Circle import Circle
from Polygon import Polygon

# Create a 320 x 240 PPM image of a human-stick figure holding a flag (see example on next page).
# The background color is white [255,255,255], with a maximal intensity of 255. 
img = Image(320, 240)
img.fill( Color(255, 255, 255) )

# The head is made from a circle with center point of (160,120) and
# radius of 20.
img.blit( Circle(160,200,20).fill( Color(255, 255, 51) ) ) # bug here

# The neck is made from a line with start and end points of (160,180)
# and (160,170).
img.blit( Line(160,180,160,170) )

# The body is made from a polygon with vertex points of (130,170),
# (190,170), (190,110), and (130,110).
img.blit( Polygon([(130,170), (190,170), (190,110), (130,110)], Color(255, 0, 0)).fill( Color(0, 0, 255) ) )

# The right arm is a line with start and end points of (130,170) and
# (100,100)
img.blit( Line(130,170,100,100) )

# The left arm is also a line with start and end points of (190,170) and
# (220,100).
img.blit( Line(190,170,220,100) )

# The right hand is a circle with center point of (100,100) and radius
# of 10.
img.blit( Circle(100,100,10, Color(0, 255, 0)).fill( Color(255, 0, 0) ) )

# The left hand is a circle with center point of (220,100) and radius of
# 10.
img.blit( Circle(220,100,10, Color(0, 255, 0)).fill( Color(255, 0, 0) ) )

# The right leg is a line with start and end points of (140,110) and
# (120,50).
img.blit( Line(140,110,120,50) )
# 
# The left leg is a line with start and end points of (180,110) and
# (200,50).
img.blit( Line(180,110,200,50) )

# The right foot is an ellipse with center point of (120,50), major axis
# is 20, and minor axis is 5.
img.blit( Ellipse(120,50,20,5).fill( Color(0, 255, 0) ) )

# The left foot is also an ellipse with center point of (200,50), major
# axis is 20, and minor axis is 5.
img.blit( Ellipse(200,50,20,5).fill( Color(0, 255, 0) ) )

# The flag is constructed as such:
# The pole is a line with start and end points of (100,125) and (100,50).
line1 = Line(100, 125, 100, 50)

# The flag is a polygon with vertex points of (100,125), (100,95), and
# (60,110)
polygon1 = Polygon([(100,125), (100,95), (60,110)]) # bug here #.fill( Color(128, 0, 128) )

# The pole and flag are translated by (0,35), in order to fit in the right
# hand of the stick figure.
line1.translate(0,35)
polygon1.translate(0,35)

# The pole and flag are rotated by 45 degrees for a fix point of (100,100),
# so the flag and pole are tilted in the right hand of the stick figure.
line1.rotate(100,100,45)
polygon1.rotate(100,100,45)

# The pole and flag are scaled by 1.25 in the x and y values for a fix
# point of (100,100), to be larger in the right hand of the stick figure.
line1.scale(100,100,1.25)
polygon1.scale(100,100,1.25)

# Blit Rest
img.blit( line1 )
img.blit( polygon1 )

# Create/Write Image
makePPM('test.ppm', img)