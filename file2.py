print("read:一口气全读")
with open("test.txt","r",encoding="utf-8")as f:
    content=f.read()
    print(content)
print("ending1")

print("for line in f:一次读一行")
with open("test.txt","r",encoding="utf-8")as f:
    for line in f:
        print(line.strip())
print("ending2")