n = int(input())

name = []
perc = []
for x in range(n):
	m = str(input())
	list = m.split(" ")
	name.append(list[0])
	del list[0]
	sum = 0
	for a in range(len(list)):
		sum += float(list[a])
		
	perc.append(sum / len(list))
	

nameOfStudent = str(input())

indexOfStudent = name.index(nameOfStudent)
print("%.2f" % perc[indexOfStudent])