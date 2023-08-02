# File: piles.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel
# pick up all the beepers in the world.

def main():
    move()
    pick_ten_beepers()
    double_move()
    pick_ten_beepers()
    double_move()
    pick_ten_beepers()
    move()

# pick 10 beepers using a for loop 
def pick_ten_beepers() :
   for i in range(10):
       pick_beeper()
   	
 # double move
def double_move():
    for i in range(2):
        move()

if __name__ == '__main__':
    main()
