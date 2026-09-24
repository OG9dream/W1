import re

text = "2026-09-08 09:12:03 INFO 用户登录成功 user=goat order=A1001"

print("所有数字:",re.findall(r"\d+",text))

print("日期:",re.findall(r"\d{4}-\d{2}-\d{2}",text))

m=re.search(r"ERROR",text)
print("search的结果",m)

if m:
    print("这行有问题")
else:
    print("这行没问题")