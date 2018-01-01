n = int(input())
c = str(input())
numbers = c.split(" ")
numbers = list(map(int, numbers))
maxElem = max(numbers)
for a in range(len(numbers)):
	if maxElem in numbers:
		indexOfSec = numbers.index(maxElem)
		del numbers[indexOfSec]
	
print(max(numbers))