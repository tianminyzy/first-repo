'''.append() method adds an item to the end of the list.
.append() 方法将一个项目添加到列表的末尾。
.insert() method adds an item to a specific index.
.insert() 方法将一个项目添加到特定索引。
.remove() method removes an item from a list based on the value.
.remove() 该方法根据值从列表中移除一个元素。
.pop() method removes the item at a particular index.
.pop() 该方法移除特定索引处的元素。'''
dna = ['AUG', 'AUC', 'UCG']

dna.append('UAA')     # ['AUG', 'AUC', 'UCG', 'UAA']
dna.insert(2, 'GAU')  # ['AUG', 'AUC', 'GAU', 'UCG', 'UAA']
dna.remove('AUC')     # ['AUG', 'GAU', 'UCG', 'UAA']
dna.pop(0)            # ['GAU', 'UCG', 'UAA']

books=['Harry Potter','1984','The Fault in Our Stars','The Mom Test','Life in Code']
books.append('Pachinko')
books.remove('The Fault in Our Stars')
books.pop(1)
print(books)