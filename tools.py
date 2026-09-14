scroes= [95, 88, 76, 60, 100]
print("最大值",max(scroes))
print("最小值",min(scroes))
print("总值",sum(scroes))
print("平均值",sum(scroes)/len(scroes))

print("从小到大",sorted(scroes))
print("从大到小",sorted(scroes,reverse=True))

print("全部",(scroes[:]))
print("前3",(scroes[:3]))
print("中间2个",(scroes[1:3]))
print("倒数2个",(scroes[-2:-1]))