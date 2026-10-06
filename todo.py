import json
import os

def load_todos():
    if os.path.exists("todos.json"):
        with open("todos.json","r")as f:
            return json.load(f)
    else:
        print("还没有存档")
        return[]

def save_todos(todos):
    with open("todos.json","w")as f:
        json.dump(todos,f,ensure_ascii=False,indent=2)


def show_all(todos):
    if len(todos)==0:
        print("清单是空的,先添加一条")
        return
    print("===我的待办===")
    for i,t in enumerate(todos,1):
        if t["完成"]:
            num=1
        else:
            num=0
        print(i,num,t["内容"])

def add_todo(todos):
    text=input("要添加什么?")
    todos.append({"内容":text,"完成":False})
    save_todos(todos)
    print("已添加:",text)

def finish_todo(todos):
    show_all(todos)
    if len(todos)==0:
        return
    n=int(input("完成第几条?"))
    if n<1 or n>len(todos):
        print("没有这个编号")
        return
    todos[n-1]["完成"]=True
    save_todos(todos)
    print("已完成:",todos[n-1]["内容"])

def delete_todo(todos):
    show_all(todos)
    if len(todos) == 0:
        return
    n = int(input("删除第几条? "))
    if n < 1 or n > len(todos):
        print("没有这个编号")
        return
    gone = todos.pop(n - 1)
    save_todos(todos)
    print("已删除:", gone["内容"])


def main():
    todos = load_todos()
    while True:
        print()
        print("===== 待办清单 =====")
        print("1. 添加待办")
        print("2. 查看全部")
        print("3. 标记完成")
        print("4. 删除待办")
        print("5. 退出")
        choice = input("请选择(1-5): ")

        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            show_all(todos)
        elif choice == "3":
            finish_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "5":
            print("再见!")
            break
        else:
            print("请输入 1~5 之间的数字")


main()