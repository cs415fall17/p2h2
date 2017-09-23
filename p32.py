def main():
    l = 1
    N = 10
    # Check whether the square root falls between intervals                                                                                      
    while( l <= U ):
        mid = math.floor(l+N/2)
        # Check to see if the given numbre is a square of middle                                                                                 
        if mid * mid == square:
            return N
        # If N is not a square, increment value of l                                                                                             
        elif N > mid * mid:
            l =	mid + 1	
	      # If N is not a square, increment value of u

        elif N < mid * mid:
            # Assign value of u
            u =	mid - 1
        else:
            # N is not a square                                                                                                                  
            print("Sorry dude, N is not a square.")
            break;
    return 0;

main()