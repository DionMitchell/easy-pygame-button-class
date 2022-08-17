# easy-pygame-button-class
easy to implement button class for pygame

TO USE:

Button(surface, message, (x,y))
OR
Button(surface, message, (x,y), align)

align is set to 'center' by default, which will center the button at the given coordinates
align can be set to 'top' which will fix the top of the text to the y-coordinate, the text will remain centered horizontally
align can be set to 'top' which will fix the bottom of the text to the y-coordinate, the text will remain centered horizontally
align can be set to 'left' which will fix the left of the text to the x-coordinate, the text will remain centered vertically
align can be set to 'right' which will fix the right of the text to the x-coordinate, the text will remain centered vertically

call Button.draw() wherever you draw things to the screen in your main loop
call Button.update() in an if statement:

if Button.update(): do something

Button.update() returns True whenever you left click on the button
