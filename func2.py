students=["小红","小明"]
scores=[88,85]
def line(n):
    print("="*n)

def say_hello(name):
    print("你好"+name+"欢迎使用python!")

def show_case(name,score):
    print(name,"的成绩是",score,"分")

line(10)
say_hello(students[0])
show_case(students[0],scores[0])
line(10)
say_hello(students[1])
show_case(students[1],scores[1])