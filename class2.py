class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def say_hello(self):
        print("大家好,我是",self.name)

    def is_pass(self):
        return self.score>=60 

    def add_score(self,n):
        self.score+=n
    
s1=Student("小红",60)
s2=Student("小明",55)

s1.say_hello()
s2.say_hello()

print(s1.name,"及格吗?",s1.is_pass())
print(s2.name,"及格吗?",s2.is_pass())

s2.add_score(10)
print("加分后",s2.name,"的成绩是",s2.score)
print("加分后",s2.name,"的成绩及格吗？",s2.is_pass())