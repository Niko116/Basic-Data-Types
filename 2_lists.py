n = int(input())
list_1 = []
for x in range(n):
	c = str(input())
	list_2 = c.split(" ")
	if list_2[0] == 'insert':
		i = int( list_2[1])
		e = int( list_2[2])
		list_1.insert(i, e)
	elif  list_2[0] == 'print':
		print(list_1)
	elif  list_2[0] == 'remove':
		e = int(list_2[1])
		list_1.remove(e)
	elif  list_2[0] == 'append':
		e = int(list_2[1])
		list_1.append(e)
	elif  list_2[0] == 'sort':
		list_1.sort()
	elif  list_2[0] == 'pop':
		list_1.pop()
	elif  list_2[0] == 'reverse':
		list_1.reverse()
		
		

