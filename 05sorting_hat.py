# Write code below 💖
# 超级分院帽
G = 0
R = 0
H = 0
S = 0
w = "Wrong input."
answer = int(input('''Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk'''))
if answer == 1:
  G = G + 1
  R = R + 1
elif answer == 2:
  H = H + 1
  S = S + 1
else:
  print(w)
answer = int(input('''Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold'''))
if answer == 1:
  H = H + 2
elif answer == 2:
  S =  S + 2
elif answer == 3:
  R = R + 2
elif answer == 4:
  G = G + 2
else:
  print(w)
answer = int(input('''Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum'''))
if answer == 1:
  S = S + 4
elif answer == 2:
  H = H + 4
elif answer == 3:
  R = R + 4
elif answer == 4:
  G = G + 4
else:
  print(w)
output = f'''🦁 Gryffindor = {G}
🦅 Ravenclaw = {R}
🦡 Hufflepuff = {H}
🐍 Slytherin = {S}'''  # f string 用法 f'''描述 = {计算好的变量}'''
print(output)
