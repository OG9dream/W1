print("-"*5+"安全除法计算器"+"-"*5)

try:
    a=int(input("请输入被除数"))
    b=int(input("请输入除数"))
    result=round(a/b,2)
    print(a,"除以",b,"的结果=",result)
except ValueError:
    print("你输入的不是数字，请返回重新输入")
except ZeroDivisionError:
    print("b(除数)不能为零，请返回重新输入")
except Exception as e:
    print("出错了:", e)

print("程序正常运行")