lines = [
    "2026-09-08 09:12:03 INFO 用户登录成功 user=goat",
    "2026-09-08 09:15:47 INFO 查询订单 order=A1001",
    "2026-09-08 09:20:11 WARNING 内存使用率 85%",
    "2026-09-08 09:31:52 ERROR 数据库连接失败",
    "2026-09-08 09:40:05 INFO 用户登录成功 user=admin",
    "2026-09-09 10:02:33 ERROR 支付超时 order=A1002",
    "2026-09-09 10:23:01 INFO 定时任务完成",
    "2026-09-09 11:05:19 WARNING 磁盘剩余空间不足",
    "2026-09-09 11:30:44 ERROR 数据库连接失败",
    "2026-09-09 12:01:00 INFO 用户退出 user=goat",
]
with open("server.log","w",encoding="utf-8")as f:
    for line in lines:
        f.write(line+"\n")

print("已生成server.log，一共",len(lines),"行")