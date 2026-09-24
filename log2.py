counts={}

with open("server.log","r",encoding="utf-8")as f:
    for line in f:
        level=line.split()[2]
        if level in counts:
            counts[level]=counts[level]+1
        else:
            counts[level]=1

#counts[level]=counts.get(level,0)+1

print(counts)
print("--- 各级别统计 ---")
for level,n in counts.items():
    print(level,":",n)