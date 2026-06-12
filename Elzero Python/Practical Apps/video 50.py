password = "Very_$tr0ng_P@55word"
tries = 0
while tries < 5:
    password_input = input("Enter your password: ")
    if password_input == password:
        print("Correct Pass!")
        break
    print("Wrong Password , try again!")
    tries +=1
    print(f"{5- tries} left")
if tries == 5:
    print("You failed to enter your pass.")