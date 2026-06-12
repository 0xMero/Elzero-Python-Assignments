# Assignment 1
name = input("Enter your name: ").strip().capitalize()
print(f"Hello, {name}")
# Assignment 2
age = int(input("Enter your age: ").strip())
messages = ["Hello Your Age Is Under 16, Some Articles Is Not Suitable For You", "Hello Your Age Is: " + str(age) + ", All Articles Is Suitable For You"]
print(messages[age >= 16])
# Assignment 3
first_name = input("Enter your first name: ").strip().capitalize()
second_name = input("Enter your Second name: ").strip().capitalize()
print(f"Hello {first_name} {second_name:.1s}.")
# Assignment 4
email = input("Enter you email: ").strip()
print(f"Your name is {email.split("@")[0].capitalize()}")
print(f"Email Service Provider Is {email.split("@")[1].split(".")[0]}")
print(f"Top Level Domain Is {email.split("@")[1].split(".")[1]}")