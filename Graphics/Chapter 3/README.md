Computer Graphics
=========
Practicing the fundamentals of computer graphics by building a 2D/3D graphic engine. Emphasis is placed on simplicing and code-reuse, rather than preformance. The finished results are outputted as [PPM files](http://netpbm.sourceforge.net/doc/ppm.html). 

***

Primitive Module
---
Contains the bare essentials for the engine to run. These include:

* Color (`class`) - Object to contain RGB color info for pixels. Might use a 3 item tuple instead.
* Shape (`class`) - Base class for all geometric primitives.
* Image (`class`) - Object that contains all the pixel data for an image.
* makePPM (`function`) - Writes an Image object to a PPM file.

GeoPrimitive Module
---
"Contains" all the geometric primitives for the 2D part of the engine. All the geometric primitives are based on the abtract class Shape. Included geometric primitives:
 
* Line
* Ellipse
* Circle
* Polygon

***

Abtract Class: Shape
---
Base class for all geometric primitives. If you are going to understand how this works you will need to read this first. 

#### Constructor and Magics
* \_\_init\_\_ - Initializes vars, and draws the objects border.
* \_\_str\_\_ (return `String`) - Prints out all draw points for the shape. Primarily for debugging.

#### Vars
* border_color (type `color Class`) - Contains the RGB draw color for the shape's border.
* inside_color (type `color Class`) - Contains the RGB draw color for the shape's inside (or fill).
* border (type `2-tuples List`) - Contains all the draw points for the shape's border.
* inside (type `2-tuples List`) - Contains all the draw points for the shape's inside (or fill).

#### Methods
* draw (return `2-tuples List`) - Calculates all draw points for the shape. Handled by child classes. 
* remove_duplicates (return ` List`) - Removes all duplicate points for a passed list.
* move(return `None`) - Translates a shape. Should be used instead of translate to avoid redrawing.
* translate(return `None`) - Translates a shape. 
* rotate(return `None`) - Rotates a shape. 
* scale(return `None`) - Scales a shape. 