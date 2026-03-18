class Student:
  def __init__(self, name, year, gpa, enrolled):
# 1. def __init__：自动启动的“构造器”
#
#    双下划线 (__)：在 Python 中，这种前缀和后缀的双下划线表示它是一个“特殊方法”。
#
#    它的职责：初始化。当你执行 daniel = Student(...) 时，Python 内部会自动调用这个函数。
#    你不需要手动写 daniel.__init__(...)，它就像是对象的“出生证明”办理处。
    self.name = name
    self.year = year
    self.gpa = gpa
    self.enrolled = enrolled

daniel = Student('Daniel Li', 10, 4.0, True)
print(vars(daniel))
class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
chincken_town = City('chinckentown','kfc',114514,'ikun')
Tokyo = City('Tokyo','Japan',1145141919810,'Mountfuji')
print(vars(chincken_town))
print(vars(Tokyo))
