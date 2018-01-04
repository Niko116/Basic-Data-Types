n = int(input())
list = str(input()).split()
for x in range(n):
	list[x] = int(list[x])
	
list = tuple(list)
print(hash(list))