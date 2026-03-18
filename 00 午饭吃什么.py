import random


def interactive_lunch():
    options = ["清蒸鱼", "白灼菜心", "西红柿豆腐汤", "玉米排骨汤", "鸡肉沙拉"]

    while True:
        choice = random.choice(options)
        user_input = input(f"抽到了【{choice}】，满意吗？(y/n): ").lower()

        if user_input == 'y':
            print(f"太棒了，祝你用餐愉快！")
            break
        else:
            print("好吧，那我们再换一个...")
            # 可选：如果完全不想吃这个，可以从列表中移除
            if choice in options:
                options.remove(choice)

            if not options:
                print("列表里的菜都抽完了，去尝试点新花样吧！")
                break


if __name__ == "__main__":
    interactive_lunch()