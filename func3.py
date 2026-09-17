def add_print(a,b):
    print(a+b)

def add_return(a,b):
    return(a+b)
    print("这一行会被执行吗")

print("用print")
add_print(1,2)
print()
print("用return")
print("result1",add_return(1,2))
print("result2",add_return(3,4)*2)
print()
#print(add_print(3, 5) * 2)