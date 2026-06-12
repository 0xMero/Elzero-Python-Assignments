# Assignment 1
# num = int(input("Enter a number: ").strip())
# if num > 0:
#     printd_numbers = 0
#     while num > 1:
#         if num == 7:
#             num -= 1
#         else:
#             num -=1
#             print(num)
#             printd_numbers +=1
#     print(f"{printd_numbers} numbers has been printed.")    
# else:
#     print("Number must be greater than 0")
# Assignment 2
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
# index = 0
# ignored_number_of_friends = 0
# capitalized_freinds = []
# while index < len(friends):
#     if friends[index].capitalize() == friends[index]:
#         capitalized_freinds.append(friends[index])
#         index += 1
#     elif friends[index].lower() == friends[index]:
#         ignored_number_of_friends += 1
#         index += 1
# print(capitalized_freinds)
# print(f"Friends printed successfully, {ignored_number_of_friends} ignored")
# Assignment 3
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]
index = 0; 
while skills:
    print(f"{skills.pop(0)}")
# my_friends = []
# max_Friends_number = 4
# while max_Friends_number != 0:
#     friend = input("Type your friend name to add: ")
#     if friend == friend.upper():
#         print("Invalid name")
#     elif friend == friend.lower():
#         my_friends.append(friend.capitalize())
#         print(f"{friend} added => Changed the first letter to uppercase letter")
#         max_Friends_number -= 1
#         print(f"{max_Friends_number} left to add")
#     else:
#         my_friends.append(friend)
#         print(f"{friend} added")
#         max_Friends_number -= 1
#         print(f"{max_Friends_number} left to add")