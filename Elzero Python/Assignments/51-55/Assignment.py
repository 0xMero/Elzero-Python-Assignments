# Assignment 1
# my_nums = [15, 81, 5, 17, 20, 21, 13]
# divisible_by_5 = []
# for num in my_nums:
#     if num % 5 == 0:
#         divisible_by_5.append(num)
# divisible_by_5.sort(reverse=True)
# counter = 0
# for i in divisible_by_5:
#     counter += 1
#     print(f"{counter} => {i}")
# print("All numbers are printed")
# Better solution of Assignment 2
# my_nums = [15, 81, 5, 17, 20, 21, 13]
# counter = 1
# for num in sorted(my_nums, reverse=True):
#     if num % 5 ==0:
#         print(f"{counter} => {num}")
#         counter += 1
# print("All numbers are printed")
# Assignment 2
# for num in range(1,21):
#     if num == 6 or num == 8 or num == 12:
#         continue
#     print(f"{str(num).zfill(2)}")
# else:
#     print("All numbers are printed")
# Assignment 3
# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }
# total_points = 0
# for key, value in my_ranks.items():
#     if value == "A":
#         print(f"My Rank in Math Is {value} And This Equal 100 Points")
#         total_points += 100
#     elif value == "B":
#         print(f"My Rank in Math Is {value} And This Equal 80 Points")
#         total_points += 80
#     elif value == "C":
#         print(f"My Rank in Math Is {value} And This Equal 40 Points")
#         total_points += 40
# print(f"Total Points Is {total_points}")
# Assignment 4 (Solution 1)
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
A = 100
B = 80
C = 40
D = 20
total_points = 0
# for student, subjects in students.items():
#     print(f"{"-" * 30}")
#     print(f"-- Student Name => {student}")
#     print(f"{"-" * 30}")
#     for subject, degree in subjects.items():
#         if degree == "A":
#             print(f"{subject} => {A}")
#             total_points += A
#         elif degree == "B":
#             print(f"{subject} => {B}")
#             total_points += B
#         elif degree == "C":
#             print(f"{subject} => {C}")
#             total_points += C
#         elif degree == "D":
#             print(f"{subject} => {D}")
#             total_points += D
#     print(f"Total Points for {student} == {total_points}")
#     total_points = 0
# Asssignment 4 (solution 2)
for student in students:
    print(f"{"-" * 30}")
    print(f"-- Student Name => {student}")
    print(f"{"-" * 30}")
    for subject in students[student]:
        if students[student][subject] == "A":
            print(f"{subject} => {A}")
            total_points += A
        elif students[student][subject] == "B":
            print(f"{subject} => {B}")
            total_points += B
        elif students[student][subject] == "C":
            print(f"{subject} => {C}")
            total_points += C
        elif students[student][subject] == "D":
            print(f"{subject} => {D}")
            total_points += D
    print(f"Total Points for {student} == {total_points}")
    total_points = 0