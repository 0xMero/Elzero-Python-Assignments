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