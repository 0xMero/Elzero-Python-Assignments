# Assignment 1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])
print(friends.pop(0))
print(friends[-1])
print(friends.pop(-1))
# Assignment 2
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[::2])
print(friends[1::2])
# Assignment 3
print(friends[1:4])
print(friends[-2:])
# Assignment 4
friends[-2:] = "Elzero", "Elzero"
print(friends)
friends.insert(0, "Khaled")
print(friends)
friends.append("Mazen")
print(friends)
# Assignment 6
friends[:2] = []
print(friends)
friends.remove(friends[-1]) 
print(friends)
# Assignment 7
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
employees.extend(school)
friends.extend(employees)
print(friends)
# Assignment 8
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(f"Sorted list From A-Z: {friends}")
friends.sort(reverse=True)
print(f"Sorted list From Z-A: {friends}")
# Assignment 9
print(len(friends))
# Assignment 10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])