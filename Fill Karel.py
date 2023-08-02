from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    """
    Karel should put the beepers in every squre of each row. 
    Karel's start in the bottom-left corner, facing right. 
    Karel's final position is in the top-right corner facing right.
    """
    while front_is_clear():
        fill_beeper()
        fill_beeper_corner()
        reset_to_next_row()
    
# make karel fill beeper while in front is clear.
def fill_beeper():
    """
    pre codition: karel is at the start facing east. (right)
    post condition: karel is fill the beepers and at the end of a row, facing east.
    """
    while front_is_clear():
        put_beeper()
        move()

# make karel fill the beeper in the corner
def fill_beeper_corner():
    """
    Only work if there are no beepers present in the corner.
    """
    if no_beepers_present():
        put_beeper()

# make karel move to the next row.
def reset_to_next_row():
    """
    pre condition: karel is at the end of the row, facing east.
    post conditon: if front is clear karel is at the start of the next row, facing east else front is blocked karel turn right to facing east and move to the wall, facing east. 
    """
    turn_around()
    move_to_wall()
    turn_right()
    if front_is_clear():
        move()
        turn_right()
    else:
        turn_right()
        move_to_wall()
    
# make karel move to the wall.
def move_to_wall():
    """
    Krl move to the wall.
    Work in any pre-condition state.
    """
    while front_is_clear():
        move()

# make karel turn around. (180 degrees)
def turn_around():
    """
    Make karel turn around 180 degrees.
    Work in any pre-condition state.
    """
    for i in range(2):
        turn_left()

# make karel turn left.
def turn_right():
    """
    Make karel turn in the clock-wise direction.
    Works in any pre-condition state.
    """
    for i in range(3):

if __name__ == '__main__':
    main()
