from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

    # draw Indonesia flag
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # get the half of the canvas
    half_canvas = CANVAS_HEIGHT/2
    
    # draw the flag
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, half_canvas, "red")
    

if __name__ == '__main__':
    main()
