# Assignment 1
# NUM = input("Add Your Number ")
# if NUM not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
#     raise Exception("Only Numbers Allowed")
# elif len(NUM) > 1:
#     raise IndexError("Only One Character Allowed")
# elif NUM == "0":
#     raise ValueError("Number Must Be Larger Than 0")
# else:
#     print("#" * 20)
#     print(f"The number is {NUM}")
#     print("#" * 20)
# Assignment 2
import string
class LengthError(Exception):
    pass
class OutOfRangeChar(Exception):
    pass
try:
    LETTER = input("Add Letter From A to Z: ")
    if len(LETTER) > 1:
        raise LengthError("must be more than one")
    elif LETTER not in string.ascii_uppercase:
        raise OutOfRangeChar
    # print(f"You Typed {LETTER}")
except LengthError:
    print("You Must Write One Character Only")
except OutOfRangeChar:
    print("The Letter Not In A - Z")
else:
    # I used else cuz elzero assignments requires to use else statement in try , otherwise i would print the message after if and elif
      print(f"You Typed {LETTER}")
# # Assignment 3
# def calculate(num1, num2) -> int:
#   return num1 + num2

# print(calculate(20, 30))