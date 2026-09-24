total=0
line_count=0

with open("server.log","r",encoding="utf-8")as f:
    for line in f:
        total=total+1
        if "ERROR" in line:
            line_count=line_count+1
            print(line.strip())

print("总行数：",total)
print("ERROR行数：",line_count)    