"""def add(x, y):
  answer = x + y
  return answer

print(answer)"""
"""The scope of the answer variable is only inside the add() function. It is a local variable that belongs to the local scope of the add() function.
answer 变量的作用域仅限于 add() 函数内部。它是一个局部变量，属于 add() 函数的局部作用域。
Now, a variable created outside of a function is called a global variable and belongs to the global scope, meaning that they can be used by every function.
现在，在函数外部创建的变量称为全局变量，属于全局作用域，这意味着它们可以被每个函数使用。"""

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]
def price_at(i):
    return stock_prices[i-1]


def max_price(a, b):
   return max(stock_prices[a - 1: b]) # 切片包头不包尾,头减尾不减


def min_price(a, b):
    return min(stock_prices[a - 1: b]) # []切片中使用:
print(price_at(7))
print(max_price(1,15))  # 参数传递中间用,
print(min_price(1,15))