import random

# Khansole Academy: randomly generates a simple addition problem for the user

def main():
    print("Khansole Academy")
    num1 = int(random.randint(10, 99))
    num2 = int(random.randint(10, 99))
    total = num1 + num2
    print("What is", num1, "+", num2, "?")
    aws = int(input("Your answer: "))
    if aws == total:
        print("Correct!")
    else :
        print("Incorrect.")
        print("The expected answer is", total)
if __name__ == '__main__':
    main()
