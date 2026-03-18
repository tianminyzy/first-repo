import math

# 坐标数据
MY_LOCATION = (60.472023, 8.468946)
friends = {
    "TIM": (40.713047, -74.007233),
    "AYAKA": (35.689487, 139.691711),
    "DINGZHEN": (31.903200, 88.752701)
}


def calculate_distance(pos1, pos2):
    lat1, lon1 = pos1
    lat2, lon2 = pos2
    R = 6371  # 地球半径(km)

    # 将角度转换为弧度
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


# 寻找最远的朋友
furthest_friend = ""
max_distance = 0

for name, coords in friends.items():
    dist = calculate_distance(MY_LOCATION, coords)
    print(f"{name} 距离你: {dist:.2f} 公里")

    if dist > max_distance:
        max_distance = dist
        furthest_friend = name

print(f"\n结论：距离你最远的朋友是 {furthest_friend}，距离为 {max_distance:.2f} 公里。")

"""MY_LOCATION = (60.472023,8.468946)
TIM = (40.713047,-74.007233)
AYAKA = (35.689487,139.691711)
DINGZHEN = (31.903200,88.752701)
friends = TIM + AYAKA + DINGZHEN
print(friends)"""

"""# valid tuple
t1 = ('hi',)

# valid tuple
t2 = 'hi',

# not a tuple
t3 = ('hi')
如果只有一个项目，请确保它在旁边有一个逗号 , 。"""