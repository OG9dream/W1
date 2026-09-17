def line(n=30):
    print("="*n)

def greet(name,greeting="你好"):
    print(greeting+name)

line()
line(10)
line(20)

greet("goat")
greet("MJ","good morning")
greet("LJ",greeting="night night")