counter = 2
f1 = 1
f2 = 1
fibNum = 0

while len(str(fibNum)) < 1000:
	fibNum = f1 + f2
	f1 = f2
	f2 = fibNum
	counter += 1

print counter
