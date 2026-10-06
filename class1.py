class Students:
    def __init__(self,name,score):
        print("我正在初始化:", self)
        self.name=name
        self.score=score

s1=Students("小明",89)
print("s1 到底是:", s1) 
s2=Students("小红",67)

print(s1.name,s1.score)
print(s2.name,s2.score)