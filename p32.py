import math

def computePartA(N):

    if N < 0:
        N = N * -1

    return recursivePartA(1, N, N)

# assume l = 1 first time being called
def recursivePartA(l, u, N):


    # Check whether the square root falls between intervals

    # N is not a square
    if( l > u ):
        return "Sorry dude, N is not a square."


    mid = (l + u) // 2

    # Check to see if the given number is a square of middle
    if( N == mid * mid ):
        return str(mid)

    # If N is not a square, increment value of l
    elif( N > mid * mid ):

        return recursivePartA(mid + 1, u, N)

    # If N is not a square, increment value of u
    elif( N < mid * mid ):

        return recursivePartA(l, mid - 1, N)
    
def powerOfNumberRecursive(x, y):
    # is x = y^n
    # assume x goes into y evenly
    # passed in first power of x
    # base case because (y^n)/nx = 1 if x = y^n
    # if y = 1 than there will be no power that can be added to 1 to change x from 1

    if x % y != 0:
        return 0

    if y == 1:
        return 0

    # if y > 1 than an exponent will exist such that x > 1 as long as y is divided by x
    else:
        return 1 + powerOfNumberRecursive(x, y // x)

def computePartC(N):

    if N < 0:
        N = N * -1
    if N == 1:
        return 1

    k = 2
    while(k <= (math.log(N, 2) // 1)):

        result = recursivePartC(1, N, N, k)

        if result:
            return result
        k = k + 1

    return -1

# assume l = 1 first time being called
def recursivePartC(l, u, N, k):


    # Check whether the square root falls between intervals

    # N is not a square
    if( l > u ):
        return 0


    mid = (l + u) // 2

    # Check to see if the given number is a square of middle
    if( N == pow(mid, k) ):
        return mid

    # If N is not a square, increment value of l
    elif( N > pow(mid, k) ):

        return recursivePartC(mid + 1, u, N, k)

    # If N is not a square, increment value of u
    elif( N < pow(mid, k) ):

        return recursivePartC(l, mid - 1, N, k)
    

def main():
    N =	int(input("Enter a value for N: "))
    print(computePartC(N))

main()
