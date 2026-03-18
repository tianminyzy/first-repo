"""dictionary = {
  key1: value1, 键:值
  key2: value2,
  key3: value3
}"""
laptop = {
  'brand': 'Apple',
  'model': 'Macbook Pro',
  'size': 14,
  'year': 2023
} # 字典中的每个键必须是唯一的，并与特定的值相关联。这种配对允许高效地检索数据。键还必须是不可变的，例如字符串
print(laptop['model'])
# Output: Macbook Pro 要访问字典中特定键关联的值，我们使用 [ ] 括号，并将键放在括号内。

# Creating a dictionary
student_info = {'name': 'Alice', 'age': 9, 'grade': 'A'}

# Accessing dictionary elements 访问字典元素
print('Name:', student_info['name'])
print('Age:', student_info['age'])
print('Grade:', student_info['grade'])

# Modifying dictionary elements 修改字典元素
student_info['age'] = 10
print('Updated Age:', student_info['age'])
# Dictionary methods
print('Keys:', student_info.keys())
print('Values:', student_info.values())
print('Items:', student_info.items())