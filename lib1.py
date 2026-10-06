import os
from datetime import datetime

#first part
print("我现在在哪?",os.getcwd())
print("todo.json存在吗?",os.path.exists("todos.json"))
print("server.log存在吗?",os.path.exists("server.log"))

files=os.listdir()
print("这个目录里有",len(files),"个文件")

print("拼出来的路径",os.path.join("data","todos.json"))

#part two
now=datetime.now()
print("原始时间对象:",now)
print("格式化后:",now.strftime("%Y-%m-%d %H:%M:%S"))