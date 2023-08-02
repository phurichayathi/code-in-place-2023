"""
Program: Liftoff
--------------------
Countdown from 10 to 1 and then print Liftoff!
"""

def main():
    # starts at 10, end at 0. reduces number by 1 each time
    for i in range (10, 0, -1):
        print(i)
    print("Liftoff!")

if __name__ == '__main__':
    main()
