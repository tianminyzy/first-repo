import random
def play():
    symbols = ['🍒','🍇', '🍉', '7️⃣']
    playing = True
    while playing:
        print("--- 欢迎来到 Python 老虎机！ ---")
        results = random.choices(symbols,k = 3)
        print('|'.join(results))
        if results == ['7️⃣','7️⃣','7️⃣']:
            print("Jackpot! 💰")
        else:
            print("Thanks for playing!")
        answer = input('\n想再玩一轮吗?(Y/N):').  upper()
        if answer != 'Y':
            playing = False
            print('\n游戏结束,感谢游玩!')
play()
# 为什么要把代码放进 play() 函数？
#     组织性：你的主程序逻辑被包裹在一个命名清晰的盒子（函数）里。
#     可重用性：如果你以后写一个更大的游戏中心程序，你只需要一行 play() 就能直接调用这个老虎机小游戏。