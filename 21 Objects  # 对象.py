"""An object is an "instance" of a class. A class is simply a template for creating objects,
 which are individual copies of the class with actual values.
一个对象是一个类的“实例”。类只是一个创建对象的模板，对象是类的一个独立副本，具有实际值。
# 类似形参和实参"""
class Student:
  student_id = 0
  name = ''
  year = 0
  gpa = 0.0
  enrolled = False
wednesday = Student()
wednesday.student_id = 1113
wednesday.name = 'Wednesday Addams'
wednesday.year = 11
wednesday.gpa = 4.0
wednesday.enrolled = True
print(vars(wednesday))

# Output: {'student_id': 1113, 'name': 'Wednesday Addams', 'year': 11, 'gpa': 4.0, 'enrolled': True}

class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False #我们需要为类中的每个属性提供一个默认值或“占位符”，这个值实际上并不会传递给我们所创建的对象。

bobs_burgers = Restaurant()# bobs_burgers 对象从一开始就从未从 Restaurant 类中接收到过值！
# 我们必须像这样手动设置它们：
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

dingzhens = Restaurant()
dingzhens.name = 'dingzhens'
dingzhens.category = 'Smoking'
dingzhens.rating = 1.5
dingzhens.delivery = True

cxk = Restaurant()
cxk.name = 'ikun'
cxk.category = 'fried chicken place'
cxk.rating = 5.0
cxk.delivery = True

print(vars(cxk))
print(vars(dingzhens))
print(vars(bobs_burgers))