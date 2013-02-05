# Imports
from Classes.Primitives import *
from Classes.Line import Line

# Pr a Blank Image
img = Image(320, 240)
# Fill Image with Color
img.fill( Color(245, 245, 245) )
# Create Line Objects
line1 = Line( 60, 120, 160, 120, Color(255, 0,0 ) )
line2 = Line( 160, 120, 160, 220, Color(0, 255, 0) )
# Blit and Create/Write Image
img.blit( line1.getPoints() )
img.blit( line2.getPoints() )
makePPM('test.ppm', img)