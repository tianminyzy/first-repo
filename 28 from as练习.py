from math import pi
from random import choice as ch
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
] # []list 列表是有序的。它就像一个储物柜，抽屉上贴着 0, 1, 2, 3... 的编号。

#    优点：适合按顺序存储东西。

#   局限：如果你想知道地球的半径，列表帮不了你，因为它只存了“地球”这个名字。
random_planet = ch(planets)
rp = random_planet  # as只能给模块或函数取别名,不能给变量取
r = 0 # 初始化变量r
if rp == 'Mercury':
  r = 2440
elif rp == 'Venus':
  r = 6052
elif rp == 'Earth':
  r = 6371
elif rp == 'Mars':
  r = 3390
elif rp == 'Saturn':
  r = 58232
else:
  print('Oops!An error occurred.')
area = round(4 * pi * (r ** 2))
# round() 在 Python 中有一个特殊的行为：它并不是简单的四舍五入，而是“四舍六入五取偶”
if area > 0:
    # {:,.2f} 中的逗号表示添加千分位，.2f 表示保留两位小数
    # 冒号 : 其实是一个分割符：
    #     冒号左边：是要处理的变量（默认为空）。
    #     冒号右边：是具体的格式化指令。
    print(rp)
    print(f'The area of the planet is {area}km²')
