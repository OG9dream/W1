import json

todos=[
    {"内容": "学完 json", "完成": True},
    {"内容": "写 todo.py", "完成": False}
    ]

#part one
text=json.dumps(todos,ensure_ascii=False)
print("===dumps后(字符串)===")
print(text)
print("他的类型:",type(text))

#part two
back=json.loads(text)
print("===loads后===")
print(back)
print("他的类型:",type(back))
print("第二条的内容:",back[1]["内容"])

#part three
with open("todos.json","w")as f:
    json.dump(todos,f,ensure_ascii=False,indent=2)

#part four
with open("todos.json","r")as f:
    data=json.load(f)
print("===从文件读回来===")
print(data)
print("条数:",len(data))