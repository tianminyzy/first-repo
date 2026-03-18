"""Sometimes, we want our functions to perform a specific task,
but the task varies depending on different input(s). And that's where parameters come in.
有时，我们希望我们的函数执行特定的任务，但任务根据不同的输入而变化。这就是参数的作用所在。

Parameters are just a fancy word for input. They are variables that a functions takes in.
They go inside the parentheses in the function definition and are used inside the function.
参数只是输入的一个花哨说法。它们是函数接收的变量。它们位于函数定义的括号内，并在函数内部使用。
An argument is the value sent to the function when the function is called.
当函数被调用时，参数是发送给函数的值。
So what's the difference between a parameter and an argument? Why are there two words for what seems like the same thing?
那么参数和实参有什么区别？为什么看似是同一件事，却有兩個詞？

    The parameter is the variable listed inside the parenthesis in the function definition (when we define the function).
    参数是在函数定义（定义函数时）括号中列出的变量。
    The argument is the value sent to the function (when we call the function).
    参数是传递给函数的值（当我们调用函数时）。
"""
#           这里是 Parameter (参数名) 形参
def fortune(mood):
    print(f"Because you feel {mood}, your fortune is: ...")

#           这里是 Argument (具体值) 实参
fortune("happy")

def distance_to_miles(distance):
  return distance / 1.609
# Well, print() functions can be anywhere in the program
# — inside or outside of a function, whereas return is the output of a function;
# you don't need to print out whatever you are returning.
# 嗯， print() 函数可以在程序的任何地方——在函数内部或外部；
# 而 return 是函数的输出；你不需要打印你正在返回的内容
"""As a rule of thumb:
作为一个经验法则：
    Use return in a function when you want to send value(s) from one point in the code to another.
    在函数中使用 return ，当你想从代码的一个点向另一个点发送值时。
    Use print() in a function when you want to display some text to the user.
    在函数中使用 print() ，当你想向用户显示一些文本时。"""

print(distance_to_miles(3000))
