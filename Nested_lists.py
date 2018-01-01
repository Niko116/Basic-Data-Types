names = []
scores = []
 
for x in range(int(input())):
	name = input()
	score = float(input())
	names.append(name)
	scores.append(score)
	
minElem = min(scores)
for a in range(len(scores)):
	if minElem in scores:
		indexOfSec = scores.index(minElem)
		del scores[indexOfSec]
		del names[indexOfSec]

secondMinElem = []
minElem = min(scores)
for a in range(len(scores)):
	if minElem in scores:
		indexOfSec = scores.index(minElem)
		secondMinElem.append(names[indexOfSec])
		del scores[indexOfSec]
		del names[indexOfSec]
	
secondMinElem.sort()
for name in secondMinElem:
	print(name)