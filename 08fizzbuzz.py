# Write code below 💖

for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  elif i % 3 == 0:
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  else:
    print(i)
'''为什么这段代码是“教科书级别”的？

    取模运算符 (%) 的熟练运用：利用余数是否为 0 来判断整除关系。

    正确的逻辑优先级：

        最严苛的条件（同时整除 3 和 5，即整除 15）放最前面。

        次要条件（只整除 3 或 5）放中间。

        兜底条件（都不满足）放最后的 else。'''
# 高阶版
for i in range(1, 101):
    output = ""
    if i % 3 == 0: output += "Fizz"
    if i % 5 == 0: output += "Buzz"
    print(output or i) # 如果 output 为空字符串，则打印数字 i
'''这一行代码其实利用了 Python 里的一个非常聪明（甚至有点“偷懒”）的特性，
    叫做 “短路逻辑”（Short-circuit logic）。

要理解这一行，我们需要把它拆开来看：
1. or 的底层逻辑

在 Python 中，or 运算不仅仅返回 True 或 False，它真正的规则是：

    如果左边的值是“真”的，就直接返回左边的值，不再看右边。

    如果左边的值是“假”的，就直接返回右边的值。

2. 什么是“假”值？

在 Python 的逻辑判断中，以下内容会被视为 “假” (Falsy)：

    数字 0

    空字符串 ""

    空列表 []

    None

    False 本身'''