# random number in the range 1 to 100, inclusive.

import random

def main():
    for i in range(10):
        value = random.randint(1, 100)
        print(value)

if __name__ == '__main__':
    main()
