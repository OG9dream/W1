import random
goal=random.randint(1, 100)
num=int(input("请输入一个数:"))
while goal!=num:
    if goal<num:
        print("猜小点")
        num=int(input("请重新输入一个数:"))
    else:
        print("猜大点")
        num=int(input("请重新输入一个数:"))
print("congratulation")