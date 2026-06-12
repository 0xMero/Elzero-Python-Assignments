# Assignment 1
# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list, my_tuple):
#   # Write Your Code Here
#   for char in data:
#     my_data.append(char)
#     final_string = "".join(my_data).capitalize()
# print(final_string) # Elzero
# Assignment 2
# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "0", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
  
#   # Write Your Code Here
#   if type(item1) == str:
#     my_data.append(item1)
#   final_string = "".join(my_data).capitalize()
# print(final_string)
# Assignment 3
from PIL import Image
# elzero_image = Image.open("elzero-pillow.png")
# box = (400, 0, 800, 400)
# elzero_image.crop(box).convert("L").save("task1.png")
# box_two = (0, 400, 1200, 800)
# cropped_bottom_image = Image.open("elzero-pillow.png").crop(box_two).convert("L").transpose(Image.Transpose.FLIP_LEFT_RIGHT).transpose(Image.Transpose.FLIP_TOP_BOTTOM).save("task2.png")
# Assignment 4
# def say_hello_to(name):
#     """\"parameter(someone) => Person Name\"
#         \"Function To Say Hello To Anyone\""""
#     return f"Hello {name}"
# print(say_hello_to("Osama"))
# print(say_hello_to.__doc__)