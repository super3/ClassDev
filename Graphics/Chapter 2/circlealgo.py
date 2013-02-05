# Imports
from Classes.Primitives import *
from Classes.Circle import Circle

# Pr a Blank Image
img = Image(320, 240)
# Fill Image with Color
img.fill( Color(245, 245, 245) )
# Create Line Objects
circle1 = Circle( 50, 50, 10, )
# Blit and Create/Write Image
img.blit( circle1.getPoints() )
makePPM('test.ppm', img)