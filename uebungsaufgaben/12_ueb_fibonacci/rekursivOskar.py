def _fibonacchi(nthDegree):
	if nthDegree == 1:
		return 0
	elif nthDegree == 2  or nthDegree == 3:
		return 1
	elif nthDegree <= 0:
		return("error: value not possible")
	else:
	 	fibNum = _fibonacchi(nthDegree-1) + _fibonacchi(nthDegree-2) 
	 	return fibNum
print(_fibonacchi(int(input("which fibonacchi number do you want to know?: "))))
