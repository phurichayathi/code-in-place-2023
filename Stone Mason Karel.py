from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""
def main():
    turn_left()
    build_column()
    turn_right()
    move_quadruple()
    turn_right()
    build_column()
    turn_left()
    move_quadruple()
    turn_left()
    build_column()
    turn_right()
    move_quadruple()
    turn_right()
    build_column()
    turn_left()
    
    # make karel build column
def build_column():
        while front_is_clear():
            put_beeper()
            move()
        put_beeper()  

    # make karel move quadruple 
def move_quadruple():
        for i in range(4):
            move()
    
    # make karel turn right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
