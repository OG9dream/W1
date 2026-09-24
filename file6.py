import re

with open("server.log","r",encoding="utf-8")as f:
    text=f.read()

dates=re.findall("\d{4}-\d{2}-\d{2}",text)
print("找到的日期",dates)

counts={}
for d in dates:
    if d in counts:
        counts[d]=counts[d]+1
    else:
        counts[d]=1

print("===每天条数===")
for day,n in counts.items():
    print(day,":",n)