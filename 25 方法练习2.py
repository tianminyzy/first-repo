class Pokemon:
  def __init__(self,entry,name,types,description,is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught
  def speak(self):
      print(self.name * 2)
  def display_details(self):
      print(f"Entry Number:{self.entry}\nName: {self.name}\nType:{self.types}\nDescription:{self.description}")
pikachu = Pokemon(25,'Pikachu','Electric Pokemon','''It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.
Pikachu has already been caught!''',True)
pikachu.display_details()
pikachu.speak()
