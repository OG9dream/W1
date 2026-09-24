line="小明,95,18"
print("原始",line)

parts=line.split(",")
print("after split",parts)
print("第一段:",parts[0],"第二段",parts[1])

new_line="|".join(parts)
print("after join",new_line)

fixed=new_line.replace("|",",")
print("after replace",fixed)
 
print("after above",line)

log = "2026-09-09 10:23:01 ERROR 数据库连接失败"
pieces = log.split()
print(pieces)
print("级别是:", pieces[2])