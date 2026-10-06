# Python 练习

自学 AI Agent 工程师路线的 Python 练习代码。

## 第 2 周:Python 基础
- `guess1.py` — 猜数字游戏(变量/输入/if/while/random)

## 第 3 周:流程控制
- `score.py` — 成绩等级判断(elif 多分支)
- `forloop.py` — for 循环与 range
- `list1.py` — 列表入门(索引/len/append)
- `total.py` — 遍历列表求总分与平均分
- `tools.py` — max/min/sum/sorted/切片
- `dict1.py` — 字典入门(键值对)
- `students.py` — 列表 + 字典组合
- `report.py` — 成绩录入与自动统计
- `manager.py` — 学生成绩管理脚本(菜单版)

## 运行方式
    python3 文件名.py

## 第 4 周:函数与模块
- `func1.py` — 函数入门(def 定义 / 调用)
- `func2.py` — 参数(形参 parameter / 实参 argument)
- `func3.py` — 返回值 return(与 print 的本质区别)
- `func4.py` — 默认参数 / 关键字参数
- `modules.py` — import 标准库(math / time / random)
- `mytools.py` — 自己写的工具箱模块
- `main.py` — 引入自定义模块
- `try1.py` — 异常处理 try / except
- `manager_v1.py` — 第 3 周过程式版本(对照用)
- `manager2.py` — 第 4 周函数版成绩管理脚本

## 刷题记录(LeetCode / 力扣)
- 1. 两数之和(Two Sum)—— 双重循环暴力法 ✅
- 9. 回文数(Palindrome Number)—— 字符串翻转 `[::-1]` ✅## 第 5 周:文件与文本(2026-09)
学到的:
- 文件读写:`open()` / `with` / 三种模式 `w`(重写)、`a`(追加)、`r`(只读)
- 逐行读文件 `for line in f`,用 `strip()` 去掉行尾 `\n`
- 字符串三件套:`split()` / `join()` / `replace()`,字符串不可变
- 正则入门:`re.findall` / `re.search`(记得写 `r""`)
- 字典计数模式:`counts[k] = counts.get(k, 0) + 1`

脚本:
- `server.log` —— 自己造的样例日志(10 行)
- `log1.py` —— 统计总行数与 ERROR 行数
- `log2.py` —— 统计各级别条数(字典计数)
- `file5.py` / `file6.py` —— 正则练习
- **`log_report.py`** —— 交付物:日志分析报告(总行数 / 各级别 / 日期 / 错误明细)
