import re


def report():
    with open("server.log", "r", encoding="utf-8") as f:
        total=0
        for line in f:
            total=total+1
        print("="*5,"日志分析报告","="*5)
        print("文件: server.log")
        print("总行数为",total)
    #report()
    
def type_counts():
    counts={}
    list=[]
    with open("server.log", "r", encoding="utf-8") as f:
        for line in f:
            parts=(line.split())
            list.append(parts[2])
        for n in list:
            if n in counts:
                counts[n]=counts[n]+1
            else:
                counts[n]=1
        print("--- 各级别条数 ---")
        for type,n in counts.items():
            print(type,":",n) 
    #type_counts() 

def dates():
    d={}
    print("--- 出现过的日期 ---")
    with open("server.log", "r", encoding="utf-8") as f:
        for line in f:
            parts=(line.split())
            d[parts[0]]=1
        print(d.keys())
    #dates()

def details():
    print("--- 错误明细 ---")
    with open("server.log", "r", encoding="utf-8") as f:
        for line in f:
            parts=(line.split())
            if  parts[2]=="ERROR":
                print(line.strip()) 
    #details()

def main():
    report()
    type_counts()
    dates()
    details()
main()