def _fibonacchi(nthDegree):
	if nthDegree == 0:
		return 0
	elif nthDegree == 1:
		return 1
	else:
	 	fibNum = _fibonacchi(nthDegree-1) + _fibonacchi(nthDegree-2) 
	 	return fibNum
print(_fibonacchi(int(input("which fibonacchi number do you want to know?:"))))
