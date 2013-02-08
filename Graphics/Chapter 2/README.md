Computer Graphics
=========
Practicing the fundamentals of computer graphics by building a 2D/3D graphic engine. Emphasis is placed on simplicing and code-reuse, rather than preformance. The finished results are outputted as [PPM files](http://netpbm.sourceforge.net/doc/ppm.html). 

***

Primitive Module
---
Contains the bare essentials for the engine to run. These include:

* Color (`class`) - Object to contain RGB color info for pixels. Might use a 3 item tuple instead.
* Image (`class`) - Object that contains all the pixel data for an image.
* makePPM (`function`) - Writes an Image object to a PPM file.

GeoPrimitive Module
---
Contains all the geometric primitives for the 2D part of the engine. All the geometric primitives are based on the abtract class Shape. Included geometric primitives:
 
* Line
* Ellipse
* Circle
* Polygon

### Abtract Class: Shape
Parent class to all geometric primitives. 

#### Vars
* color (`color Class`) - Contains the RGB draw color for the shape.
* points (`tuples List`) - Contains all the draw points for the shape.

#### Methods
* \_\_str\_\_ (returns `String`) - Prints out all draw points for the shape. Primarily for debugging.
* remove_duplicates (return `tuples List`) - Removes all duplicate points for a passed list.
* draw (return `tuples List`) - Calculates all draw points for the shape.