class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        print("你好我是",self.name,"今年",self.age,"岁")
    
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score

    def study(self):
        print(self.name,"正在学习")

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject

    def teach(self):
        print(self.name,"教",self.subject,"科")

s=Student("kb",8,5)
t=Teacher("mj",23,"basketball")

s.say_hello()
t.say_hello()
s.study()
t.teach( )