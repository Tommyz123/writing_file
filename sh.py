#写入数据
hs = [] #先要建立一个hs的清单
while True: #转圈圈，一直跑
	name = input('请输入名字：') #输入的信息，存为name。
	if name == 'q': #如果输入 q 程序就停止。
		break
	sale = input('请输入做的sale： ') 

	#p = [] #一样的东西，这个写的比较具体点
	#p.append(name)
	#p.append(sale)
	#hs.append(p)

	hs.append([name, sale]) #把name和sale的数据存入hs的清单中。
print(hs)



for d in hs: #把d代表hs里面的每一次的输入数据
	print(d[0], d[1]) #d[0]代表第一个数据（名字），d[1]代表第二个数据（销售）。

with open('sales.csv', 'w') as f: #读取数据，w代表写入。保存为sale.csv
	for d in hs:
		f.write(d[0] + ',' + d[1] + '\n') #把数据存入电脑，‘,’让数据自动分开， \n代表回车键