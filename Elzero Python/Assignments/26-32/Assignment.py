# Assignment 1
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))
print(unique_list)
print(type(unique_list))
print(unique_list[:-1])
# Assignment 2
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums.union(letters))
print(nums | letters)
print(nums | letters.copy())
# Assignment 3
my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
# Assignment 4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
# Assignment 5
skills = {
    "HTML": 90,
    "CSS" : 80,
    "Python" : 30,
}
print(f"{list(skills.keys())[0]} progress Is {skills["HTML"]}%")
print(f"{list(skills.keys())[1]} progress Is {skills["CSS"]}% ")
print(f"{list(skills.keys())[2]} progress Is {skills['Python']}% ")
skills.update({"AI": 20})
print(f"{list(skills.keys())[3]} progress Is {skills["AI"]}% ")