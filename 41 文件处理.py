# This opens example file for writing
file = open('example.txt','w',encoding='utf-8')
file.write('Hello, World! 🌎')
file.close()
ding = open('dingzhen.txt','w',encoding='utf-8')
lines = ['丁老爷来咯!\n','在山里我可以听到各种各样的叫声\n']
ding.writelines(lines)
ding.write('知识学报!\n')
ding.close() # 打开文件,写模式(格式化写),编码utf-8
