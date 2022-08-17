# easy-pygame-button-class
easy to implement button class for pygame

TO USE:

Button(surface, message, (x,y)) to center text on coordinates
OR
Button(surface, message, (x,y), align) to choose where text is placed in relation to coordinates

align is set to 'center' by default, which will center the button at the given coordinates
align can be set to 'top' which will fix the top of the text to the y-coordinate, the text will remain centered horizontally
align can be set to 'top' which will fix the bottom of the text to the y-coordinate, the text will remain centered horizontally
align can be set to 'left' which will fix the left of the text to the x-coordinate, the text will remain centered vertically
align can be set to 'right' which will fix the right of the text to the x-coordinate, the text will remain centered vertically
align can be set to 'topleft' which will fix the top-left corner of the text to the given coordinates
align can be set to 'topright' which will fix the top-right corner of the text to the given coordinates
align can be set to 'bottomleft' which will fix the bottom-left corner of the text to the given coordinates
align can be set to 'bottomright' which will fix the bottom-right corner of the text to the given coordinates

call Button.draw() wherever you draw things to the screen in your main loop
call Button.update() in an if statement:

if Button.update(): do something

Button.update() returns True whenever you left click on the button
