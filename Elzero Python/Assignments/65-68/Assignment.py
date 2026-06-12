# Assignment 1
import os
# for i in range(1,51):
#     if i == 25:
#         open("Python/special-text", "w")
#     else:
#         open(f"Python/file{i}.txt", "w").write(f"Elzero Web School => {i}")
# print(os.getcwd())
# print(os.path.dirname(__file__))
# print(__file__)
# print(os.system("ls Python/ > count.txt"))
# countFile = open("count.txt")
# counter = 0
# for line in countFile:
#     counter += 1
# print(counter)
# print(len(os.listdir("Python")))
# Assignment 2
# for i in range(2,51):
#     open(f"Python/file{i}.txt", "a").write("\nAppended => Elzero Web School" * 50)
# Assignment 3
# line_counter = 0
# word_counter = 0
# char_counter = 0
# l_counter = 0
# myFile = open("Python/file1.txt")
# for line in myFile:
#     line_counter += 1
#     word_counter += len(line.split(" "))
#     for char in line:
#         if char == "l":
#             l_counter += 1
#             char_counter += 1
#         elif char == " " or char =="\n":
#             continue
#         else:
#             char_counter += 1
# print(f"Number Of Lines Is => {line_counter}")
# print(f"Number Of Chars Is => {word_counter}")
# print(f"Number Of Chars Is => {char_counter}")
# print(f"Number Of \"l\" Char Is => {l_counter}")
# Assignment 4
# for num in range(50,39, -1):
#     os.remove(f"Python/file{num}.txt")