# Assignment 1
# def calculate(firstnum, secondnum, operation="add"):
#     operations = ["add", "subtract", "multiply", "a", "s", "m"]
#     if operation.strip().lower() not in operations:
#         return "Invalid Operation. Please choose (add(a), subtract(s), multiply(m))"
#     else:
#         if operation.strip().lower() in ["add", "a"]:
#             return int(firstnum) + int(secondnum)
#         elif operation.strip().lower() in ["subtract", "s"]:
#             return int(firstnum) - int(secondnum)
#         elif operation.strip().lower() in ["multiply", "m"]:
#             return int(firstnum) * int(secondnum)
# print(calculate(1,3,"dsf"))
# Assignment 2
# def addition(*numbers):
#     total_addition = 0
#     for num in numbers:
#         if int(num) == 10:
#             continue
#         elif int(num) == 5:
#             total_addition -= 5
#         else:
#             total_addition += num
#     return total_addition
# print(addition(5,5,5,5,5))
# Assignment 3
# def show_skills(name, *skills):
#     if not skills:
#         return f"Hello {name} You Have No Skills To Show"
#     print(f"Hello {name} Your Skills Is")
#     for skill in skills:
#         print(f"-{skill}")
# print(show_skills("Ahmed"))
# Assignment 4
def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    return f"Hello {name} Your age Is {age} And You Live In {country}"
print(say_hello())