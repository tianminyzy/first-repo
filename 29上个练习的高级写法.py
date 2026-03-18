from math import pi
from random import choice

# 使用字典存储数据
planet_radii = {
    'Mercury': 2440,
    'Venus': 6052,
    'Earth': 6371,
    'Mars': 3390,
    'Saturn': 58232
}
#
#字典是关联性的。它存储的是“映射关系”。

#    键 (Key)：就像目录或标签（如 'Earth'）。

#   值 (Value)：是标签背后的具体内容（如 6371）。

#   优点：查找速度极快！你不需要数它在第几个，直接喊名字就能拿到数据。

rp = choice(list(planet_radii.keys())) # 随机选一个行星
r = planet_radii[rp]                   # 直接获取对应的半径

area = 4 * pi * (r ** 2)
print(f"{rp} 的表面积是: {area:,.2f} km²")
# {:,.2f} 中的逗号表示添加千分位，.2f 表示保留两位小数
# 冒号 : 其实是一个分割符：
#     冒号左边：是要处理的变量（默认为空）。
#     冒号右边：是具体的格式化指令