admins = ["Ammar", "Yasser", "Elsayed", "Walaa"]
name = input("Enter your name: ").strip().capitalize()
if name in admins:
    print("Authorized!")
    option = input("Choose What you want to do (Update, Remove) your name from admins: ").strip().capitalize()
    if option == "Update":
        Newname = input("Enter the new name: ").strip().capitalize()
        admins[admins.index(name)] = Newname
        print("Updated List:")
        print(admins)
    elif option == "Remove":
        print("You have been removed from admins.")
        admins.remove(name)
else:
    print("You are not authorized to view this page. Want to add your name to admins?")
    choice = input("Enter Y or N: ").strip().capitalize()
    if choice == "Y":
        print("You have been added to the list")
        admins.append(name)
        print(f"Updated List: {admins}")
    else:
        print("You were not added.")