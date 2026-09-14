students=[]

while True:
    print()
    print("=====学生成绩管理=====")
    print("1.录入学生成绩")
    print("2.查看成绩单")
    print("3.查看统计")
    print("4.退出")
    choice=input("请选择功能:(输入数字)")

    if choice== "1" :
        count=int(input("要录入几个学生"))
        for i in range(count):
            name=input("请输入学生姓名:")
            score=int(input("请输入"+name+"的成绩:"))
            students.append({"name":name,"score":score})
        print("成功录入")

    elif choice== "2" :
        if len(students)==0:
            print("数据还没有录入，请返回录入")
        else:
            for s in students:
                print(s["name"],s["score"])

    elif choice== "3" :
        scores=[]
        for s in students: 
            scores.append(s["score"])
        print("总分",sum(scores))
        print("平均分",round(sum(scores)/len(scores) ,2 ))
        print("最高分",max(scores))
        print("最低分",min(scores))
         
    elif choice== "4" :
        print("再见")
        break

    else:
        print("错误选项")