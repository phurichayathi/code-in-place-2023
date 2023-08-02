from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    move_double()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move_double()
    turn_around()
 
    # make karel move double
def move_double():
    move()
    move()
    
    # make karel turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    # make karel turn around
def turn_around():
    turn_left()
    turn_left()
    
if __name__ == '__main__':
    main()
