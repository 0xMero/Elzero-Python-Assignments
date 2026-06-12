# Assignment 1
# class Game:
#     def __init__(self, name, developer, year, price_in_egypt):
#         self.name = name
#         self.developer = developer
#         self.year = year
#         self.price_in_egypt = price_in_egypt
    
#     def price_in_pounds(self):
#         return self.price_in_egypt
# game_one = Game("Ys", "Falcom", 2010, 780)

# print(f"Game Name Is \"{game_one.name}\", ", end="")
# print(f"Developer Is \"{game_one.developer}\", ", end="")
# print(f"Release Date Is \"{game_one.year}\", ", end="")
# print(f"Price In Egypt Is {game_one.price_in_pounds()}", end="")

# Needed Output
# "Game Name Is "Ys", Developer Is "Falcom", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"

# Assignment 2
# class User:
#     def __init__(self, fname, lname, age, gender):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.gender = gender

#     def full_details(self):
#         if self.gender.capitalize() == "Male":
#             return f"Hello Mr {self.fname} {self.lname:.1s}. [{40 - self.age}] Years To Reach 40"
#         elif self.gender.capitalize() == "Female":
#             return f"Hello Mrs {self.fname} {self.lname:.1s}. [{40 - self.age}] Years To Reach 40"
#         else:
#             print("Please Type the gender correctly (male or female)")
# user_one = User("Osama", "Mohamed", 38, "Male")
# user_two = User("Eman", "Omar", 25, "Female")

# print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
# print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40
# Assignment 3
# class Message:
#     def print_message():
#         return "Hello From Class Message"
    # Write Class Content

# print(Message.print_message())

# Output
# Hello From Class Message
# Assignment 4
# class Games:
#     def __init__(self, game_name):
#         self.game_name = game_name
            
#     # Write Class Content
#     def show_games(self):
#         if type(self.game_name) == int:
#             print(f"I Have {self.game_name} Game.")
#         elif type(self.game_name) == list:
#             print("I Have Many Games:")
#             for game in self.game_name:
#                 print(f"-- {game}")
#         elif type(self.game_name) == str:
#             print(f"I Have One Game Called \"{self.game_name}\"")
# my_game = Games("Shadow Of Mordor")
# my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
# my_games_count = Games(80)

# my_game.show_games()
# # Ouput
# # I Have One Game Called "Shadow Of Mordor"

# my_games_names.show_games()
# # Ouput
# # I Have Many Games:
# # -- Ys II
# # -- Ys Oath In Felghana
# # -- YS Origin

# my_games_count.show_games()
# # Output
# # I Have 80 Game.
# Assignment 5
# Main Class
# class Members:

#   def __init__(self, n, p):

#     self.name = n

#     self.permission = p

#   def show_info(self):

#     return f"Your Name Is {self.name} And You Are {self.permission}"

# # Create Admin Class Here
# class Admins(Members):
#     pass
# # Create Moderators Class Here
# class Moderators(Members):
#     def __init__(self, n, p):
#        super().__init__(n, p)
       
# member_one = Admins("Osama", "Admin")
# member_two = Moderators("Ahmed", "Moderator")

# print(member_one.show_info())
# # Output
# # Your Name Is Osama And You Are Admin

# print(member_two.show_info())
# # Output
# # Your Name Is Ahmed And You Are Moderator
# Assignment 6
class A:

  def __init__(self, one):

    self.one = one

class B:

  def __init__(self, two):

    self.two = two

class C:

  def __init__(self, three):

    self.three = three

# Write The Class Called "Name" Here
class Name(A, B, C):
    def __init__(self, *strings):
      for i, j in zip(strings, Name.__bases__):
        j.__init__(self, i)
        
    def show_name(self):
        full_word = ""
        for attr in self.__dict__:
          full_word += self.__dict__[attr]
        return full_word
the_name = Name("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero