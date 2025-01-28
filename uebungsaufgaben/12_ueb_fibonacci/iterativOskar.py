import sys
sys.set_int_max_str_digits(1000000)
num1 = 0
num2 = 1
fibNum = 1
nthDegree = 1000000
for i in range(nthDegree):
	fibNum = num1 + num2
	num1 = num2 
	num2 = fibNum
print(num1)