# Assignment 1 
# Method 1
# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
# def remove_chars(word):
#     return word[1:-1]
# cleaned_list = map(remove_chars, friends_map)
# for name in cleaned_list:
#     print(name)
# Method 2
# for word in map(lambda name: name[1: -1], friends_map):
#     print(word)
# Assignment 2
# Method 1
# friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
# def get_names(name):
#     return name[-1].lower() == "m"
# names = filter(get_names, friends_filter)
# for name in names:
#     print(name)
# Method 2
# for name in filter(lambda name : name[-1].lower() == "m", friends_filter):
#     print(name)
# Assignment 3
# from functools import reduce
# nums = [2, 4, 6, 2]
# print(reduce(lambda num1, num2: num1 * num2, nums))
# Assignment 4
# Method 1
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
# for order, skill in enumerate(reversed(skills), 50):
#     if type(skill) != int:
#         print(f"{order} - {skill}")
# Method 2
def filter_nums(pair):
    for skill in pair:

        return type(pair[-1]) != int
# for order, skill1 in 
#     print(f"{order} - {skill1}")
#     print(type(skill1))
for order, skill in filter(filter_nums, enumerate(reversed(skills), 50)):
    print(f"{order} - {skill}")