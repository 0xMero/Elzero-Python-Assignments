# Assignment 1
import hashlib
name = "Ammar"
age = 18
city = "Mansourah"
print(f"\"Hello '{name}', How You Doing \\ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {city}")
# Assignment 2
print(f"\"Hello '{name}', How You Doing \\ \
\\ \"\"\" Your Age Is \"{age}\"\" + \
       And Your Country Is: {city}")
# Assignment 3
name = "Elzero"
print(name[1])
print(name[2])
print(name[5])
# Assignment 4
print(name[1:4])
print(name[::2])
print(name[-2::-2])
# Assignment 5
name = "#@#@Elzero#@#@"
print(name.strip("#@"))
# Assignment 6
num = "9"
print(num.rjust(4,"0"))
num = "15"
print(num.rjust(4,"0"))
num = "130"
print(num.rjust(4,"0"))
num = "950"
print(num.rjust(4,"0"))
num = "1500"
print(num.rjust(4,"0"))
# Assignment 7
name_one = "Osama"
print(name_one.rjust(20, "@"))
name_two = "Osama_Elzero"
print(name_two.rjust(20, "@"))
# Assignment 8
name_one = "OSamA"
print(name_one.swapcase())
name_two = "osaMA"
print(name_two.swapcase())
# Assignment 9
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))
# Assignment 10
name = "Elzero"
print(name.find("z"))
# Assingment 11
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3", "Love", 1))
# Assignment 12
print(msg.replace("<3", "Love"))
# Assignment 13
name = "Osama"
age = 38
country = "Egypt"
print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")

flag = [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 102, 55, 97, 54, 101, 125]
for i in flag:
    print(chr(i), end='')
print()