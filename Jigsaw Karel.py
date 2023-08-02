from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

def main():
    move_double()
    pick_beeper()
    move()
    turn_left()
    move_double()
    put_beeper()
    turn_around()
    move_double()
    turn_right()
    move_to_wall()
    turn_around()
    
# Make karel move 2 steps.
def move_double():
    for i in range(2):
        move()
        
# Make karel move to the wall.
def move_to_wall():
    while front_is_clear():
        move()
        
# Make karel turn around 180 degrees.
def turn_around():
    for i in range(2):
        turn_left()
      
 # Make karel turn right.       
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()
