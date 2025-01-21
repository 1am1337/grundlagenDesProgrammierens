num1 = 0
num2 = 1
fibNum = 0
while True:
	nthDegree = input("which fibonacchi number do you want to know?:")
	if nthDegree.isdigit():
		for i in range(int(nthDegree)-1):
			fibNum = num1 + num2
			num1 = num2 
			num2 = fibNum
		print(fibNum)
		break
	else:
		print("not a number")