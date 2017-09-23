import math

def compute(N):

    l = 1
    u = N
    # Check whether the square root falls between intervals      
    limit = 0            
    while( l <= u ):
        if limit == 10:
            break
        mid = math.floor(l+u/2)
        print(mid)
        # Check to see if the given numbre is a square of middle             
        if( (mid*mid) == N ):
            return N
        # If N is not a square, increment value of l                         
        elif( N > (mid*mid) ):
            l =mid + 1
            # If N is not a square, increment value of u                     
        elif( N < (mid*mid) ):
            # Assign value of u                                              
            u =mid - 1
        else:
            # N is not a square                                              
            print ("Sorry dude, N is not a square.")
            break
        limit = limit + 1
def main():
    N =	int(input("Enter a value for N: "))
    print(compute(N))

main()