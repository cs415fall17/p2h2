import math

def compute(l, N):

    # Check whether the square root falls between intervals                  
    while( l <= N ):
        mid = math.floor(l+N/2)
        # Check to see if the given numbre is a square of middle             
        if( mid*mid == N ):
            print(N)
            return 0
        # If N is not a square, increment value of l                         
        elif( N > mid*mid ):
            l =mid + 1
            # If N is not a square, increment value of u                     
        elif( N < mid*mid ):
            # Assign value of u                                              
            u =mid - 1
        else:
            # N is not a square                                              
            print ("Sorry dude, N is not a square.")
            break
def main():
    l =	int(input("Enter value for l: "))
    N =	int(input("Enter a value for N: "))
    compute(l, N)

main()