tries = 5
the_file = None
while tries != 0:
    try:
        file_name = input("Enter the name of the file you want to open: ")
        the_file = open(file_name)
        print(the_file.read())
        break
    except FileNotFoundError:
        tries -= 1
        print("File Not found.", "Please Enter the name of the file again")
    finally:
        if the_file != None:
            the_file.close()
else:
    print("Your tries ran out")