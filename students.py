student=[{"name":"小明","score":95},{"name":"小红","score":88},{"name":"小刚","score":60}]
print("有几个学生",len(student))
print("第一个学生",student[0])
print("第一个学生的名字",student[0]["name"])
print("第一个学生的成绩",student[0]["score"])
for s in student:
    print(s["name"],"的成绩是",s["score"])
total=0
for s in student:
    total=total+s["score"]
print("总分",total)
print("平均分",total/len(student))
student.append({"name": "小美", "score": 100})
print("现在有", len(student), "个学生")
