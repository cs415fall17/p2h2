def powerOfNumber(x, y):
	# is x = y^n
	# passed in first power of x
	n = 1
	while(x < y):
		x = x * x
		n = n + 1
	return n

def powerOfNumberRecursive(x, y):
	# is x = y^n
	# assume x goes into y evenly
	# passed in first power of x
	# base case because (y^n)/nx = 1 if x = y^n
	# if y = 1 than there will be no power that can be added to 1 to change x from 1
	if y == 1:
		return 0
	# if y > 1 than an exponent will exist such that x > 1 as long as y is divided by x
	else:
		return 1 + powerOfNumberRecursive(x, y // x)

print(powerOfNumberRecursive(2, 8))
print(powerOfNumberRecursive(2, 2))
print(powerOfNumberRecursive(2, 16))
print(powerOfNumberRecursive(3, 9))