item = ['🍔 Cheeseburger','🍟 Fries','🥤 Soda','🍦 Ice Cream','🍪 Cookie']

def welcome():
  menu_display = "\n".join(item)
  return f"Welcome! Today's Menu: \n{menu_display}\nPlease enter a number (1-5): "

choice_index = int(input(welcome()))
order = item[choice_index - 1]
print(order)