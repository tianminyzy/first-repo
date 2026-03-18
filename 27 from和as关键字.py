# from random import choice, sample
# from random import sample as samp, choice as choi
# 每一个函数都要配对自己的 as
# 我们可以使用 from 关键字从模块中导入一个或多个对象，例如内置类、方法或变量。
# import random as rd 我们可以使用 as 关键字给一个模块起别名
from random import sample as samp

example = samp(['Stark', 'Targaryen', 'Baratheon', 'Greyjoy', 'Lannister'], 2)

print(f'Example:{example[0]} {example[1]}')