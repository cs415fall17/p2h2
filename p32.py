
def computePartA(N):

    l = 1

    if N < 0: N = N * -1

    u = N
    # Check whether the square root falls between intervals      

    while( l <= u ):

        mid = (l+u) // 2

        # Check to see if the given number is a square of middle             
        if( (mid*mid) == N ):
            return str(mid)
        # If N is not a square, increment value of l                         
        elif( N > (mid*mid) ):
            l =mid + 1

            # If N is not a square, increment value of u                     
        elif( N < (mid*mid) ):
            # Assign value of u                                              
            u =mid - 1

    # N is not a square                                              
    return "Sorry dude, N is not a square."

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

def computePartC(N):

    l = 1

    if N < 0: N = N * -1

    u = N
    # Check whether the square root falls between intervals      

    while( l <= u ):

        mid = (l+u) // 2

        # Check to see if the given number is a square of middle             
        if( (mid*mid) == N ):
            return str(mid)
        # If N is not a square, increment value of l                         
        elif( N > (mid*mid) ):
            l =mid + 1

            # If N is not a square, increment value of u                     
        elif( N < (mid*mid) ):
            # Assign value of u                                              
            u =mid - 1

    # N is not a square                                              
    return "Sorry dude, N is not a power."

def main():
    N =	int(input("Enter a value for N: "))
    print(compute(N))

main()