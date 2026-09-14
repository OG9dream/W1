students = []

count = int(input("要录入几个学生?"))

for i in range(count):
    name = input("请输入学生姓名:")
    score = int(input("请输入" + name + "的成绩:"))
    students.append({"name": name, "score": score})

print()
print("===== 成绩单 =====")
for s in students:
    print(s["name"], s["score"])

scores = []
for s in students:
    scores.append(s["score"])

total = sum(scores)

print("----- 统计 -----")
print("人数:", len(students))
print("总分:", total)
print("平均分:", total / len(students))
print("最高分:", max(scores))
print("最低分:", min(scores))

pass_count = 0
for s in students:
    if s["score"] >= 60:
        pass_count = pass_count + 1
print("及格人数:", pass_count)