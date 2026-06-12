# Assignment 1
# def reverse_string(my_string):
#     for char in reversed(my_string):
#        yield char
# for c in reverse_string("Elzero"):
#   print(c, end= "")
# Assignment 2
def sugar_add(func):
    def wrapper():
        print("Sugar Added From Decorators")
        func()
        print("#" * 20)
    return wrapper
@sugar_add
def make_tea():
  print("Tea Created")
@sugar_add
def make_coffe():
  print("Coffe Created")
make_tea()
make_coffe()