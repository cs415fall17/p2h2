# David Tauraso and Jacques Beauvoir

# all the computations for HW 1 shall be done using binary arithmetic
# only the user input and the final output will be in decimal.
# dec2bin and bin2dec convert between binary and decimal.

# functions provided: Add, Mult, Divide and many supporting functions such as
# Compare to compare two unbounded integers, bin2dec and dec2bin etc.

# missing functions: subtraction, exp, gcd, Problem1, Problem2, Problem3 and the main function
# for user interface

########################################################
### SAMPLE INPUT/OUTPUT                              ###
########################################################
# Problem1
# Inputs: 99,101,101,99
# Output: 3621042145110495340304913321770092884828963481118630680783443137199360424701178235489444339150903695510140270221458360654677736177726261420668704432019096568923217654887729426654819147812495289601990198
# actual: 3621042145110495340304913321770092884828963481118630680783443137199360424701178235489444339150903695510140270221458360654677736177726261420668704432019096568923217654887729426654819147812495289601990198

# Problem1
# Inputs: 101,100,102,101
# Output: -73624909023231670869261708087644352879856062771895622746310308401235838873720979357266761267201142320719562605934027588808477220968934718015196126899431090054281838673459558997083139194957867884875198351
# actual: -73624909023231670869261708087644352879856062771895622746310308401235838873720979357266761267201142320719562605934027588808477220968934718015196126899431090054281838673459558997083139194957867884875198351

# Problem2
# Inputs: 921,97,376,49
# Output: Quotient: 223346796471162164452913306468608511973357088088077011223389370777657713512498752849853123746821473506392127360180733334528455377517683142902106402854175807704081
#         Remainder: 868589458788803459890025777897148259540992011101528169885851420031124037456917859918715079950453053934476646860356569316780185


# actual: quotient: 223346796471162164452913306468608511973357088088077011223389370777657713512498752849853123746821473506392127360180733334528455377517683142902106402854175807704081
#         remainder: 868589458788803459890025777897148259540992011101528169885851420031124037456917859918715079950453053934476646860356569316780185

# Problem3
# Input: 71
# Output: Numerator: 3028810706851429109067025637383
#         Denominator: 624893729741902836283505236800
#>>> 
#                    3028810706851429109067025637383
#                      624893729741902836283505236800
##########################################################

import random as rand___
from random import SystemRandom
import sys
import time

sys.setrecursionlimit(10000000)

from random import *

def shift(A, n):
    if n == 0:
        return A
    return [0] + shift(A, n-1)

   
def mult(X, Y):
    # mutiplies two arrays of binary numbers
    # with LSB stored in index 0

    if zero(Y):
        return [0]
    Z = mult(X, div2(Y))

    if even(Y):
        return add(Z, Z)
    else:
        return add(X, add(Z, Z))


def Mult(X, Y):

    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    return bin2dec(mult(X1,Y1))


def zero(X):
    # test if the input binary number is 0
    # we use both [] and [0, 0, ..., 0] to represent 0
    if len(X) == 0:
        return True
    else:
        for j in range(len(X)):
            if X[j] == 1:
                return False
    return True


def div2(Y):
    if len(Y) == 0:
        return Y
    else:
        return Y[1:]


def even(X):
    if ((len(X) == 0) or (X[0] == 0)):
        return True
    else:
        return False


def add(A, B):
    # assume A and B are reversed bitstrings
    A1 = A[:]
    B1 = B[:]
    n = len(A1)
    m = len(B1)
    if n < m:
        for j in range(len(B1)-len(A1)):
            A1.append(0)
    else:
        for j in range(len(A1)-len(B1)):
            B1.append(0)
    N = max(m, n)
    C = []
    carry = 0
    for j in range(N):
        C.append(exc_or(A1[j], B1[j], carry))
        carry = nextcarry(carry, A1[j], B1[j])
    if carry == 1:
        C.append(carry)
    return C


def Add(A,B):
    return bin2dec(add(dec2bin(A), dec2bin(B)))


def exc_or(a, b, c):
    return (a ^ (b ^ c))


def nextcarry(a, b, c):
    if ((a & b) | (b & c) | (c & a)):
        return 1
    else:
        return 0 

        
def bin2dec(A):
    if len(A) == 0:
        return 0
    val = A[0]
    pow = 2
    for j in range(1, len(A)):
        val = val + pow * A[j]
        pow = pow * 2
    return val


def reverse(A):
    B = A[::-1]
    return B


def trim(A):
    if len(A) == 0:
        return A
    A1 = reverse(A)
    while ((not (len(A1) == 0)) and (A1[0] == 0)):
        A1.pop(0)
    return reverse(A1)


def compare(A, B):
    # compares A and B outputs 1 if A > B, 2 if B > A and 0 if A == B
    A1 = reverse(trim(A))
    A2 = reverse(trim(B))
    if len(A1) > len(A2):
        return 1
    elif len(A1) < len(A2):
        return 2
    else:
        for j in range(len(A1)):
            if A1[j] > A2[j]:
                return 1
            elif A1[j] < A2[j]:
                return 2
        return 0


def Compare(A, B):
    return bin2dec(compare(dec2bin(A), dec2bin(B)))


def dec2bin(n):
    # creates binary number in reverse
    #print(n)
    if n == 0:
        return []

    # if negative store in 2's 
    #if n == -1:

    m = n // 2
    A = dec2bin(m)
    fbit = n % 2
    #print([fbit] + A)
    return [fbit] + A


def map(v):
    if v==[]:
        return '0'
    elif v ==[0]:
        return '0'
    elif v == [1]:
        return '1'
    elif v == [0,1]:
        return '2'
    elif v == [1,1]:
        return '3'
    elif v == [0,0,1]:
        return '4'
    elif v == [1,0,1]:
        return '5'
    elif v == [0,1,1]:
        return '6'
    elif v == [1,1,1]:
        return '7'
    elif v == [0,0,0,1]:
        return '8'
    elif v == [1,0,0,1]:
        return '9'   

        
def bin2dec1(n):
    if len(n) <= 3:
        return map(n)
    else:
        temp1, temp2 = divide(n, [0,1,0,1])
        return bin2dec1(trim(temp1)) + map(trim(temp2))


def pad(X, Y):
    X1 = X[:]
    Y1 = Y[:]
    len_X1 = len(X1)
    len_Y1 = len(Y1)
    if len_X1 > len_Y1:
        for x in range(len_X1 - len_Y1):
            Y1.append(0)
    else:

        for x in range(len_Y1 - len_X1):
            X1.append(0)

    return (X1, Y1)


def flipBits(X):
    Y = []
    for j in range(len(X)):
        if X[j] == 0:
            Y.append(1)
        else:
            Y.append(0)
    return Y


def divide(X, Y):
    # finds quotient and remainder when A is divided by B
    if zero(X):
        return ([],[])
    (q,r) = divide(div2(X), Y)

    q = add(q, q)
    r = add(r, r)
    
    if not even(X):
        r = add(r,[1])

    if (not compare(r,Y) == 2):
        r = sub(r, Y)
        q = add(q, [1])

    return (q,r)


def Divide(X, Y):
    (q,r) = divide(dec2bin(X), dec2bin(Y))
    return (bin2dec(q), bin2dec(r))


def twosComplement(X):
    # X is a number that is already in twos complement (so positive numbers
    # should have an extra 0 at the beginning).
    # Returns the twos complement of X (as a binary number).
    X1 = flipBits(X)
    X1 = add(X1, [1])
    return X1


def twosComp2Dec(X):
    # Given a reversed bitstring that is stored in two's complement, the
    # function will return that number in decimal. The returned value
    # can be positive or negative depending on the last bit in the bitstring.
    if X[len(X) - 1] == 1:
        return bin2dec(twosComplement(X)) * -1

    return bin2dec(X)


def subtract(X, Y):
    #X and Y are positive numbers and are decimals
    #The returned value is a decimal number that can
    #be positive or negative.
    X1 = dec2bin(X)
    Y1 = dec2bin(Y)
    
    return twosComp2Dec(sub(X1, Y1))
    

def sub(X, Y):
    # X and Y are positive, binary numbers
    # The result is the binary representation of X - Y in twos complement.
    (X1, Y1) = pad(X, Y)
    X1.append(0) #Add one extra bit for the flags for two's complement
    Y1.append(0)
    Y1 = twosComplement(Y1) #Subtract

    result = add(X1, Y1)

    # hack off extra carry bit
    if len(result) > len(X1):
        result = result[:len(result) - 1]
    
    return result
    

def exp(X, Y):
    # Takes in two reversed binary strings and returns
    # a binary string of X^Y.
    if zero(Y):
         return [1]
    z = exp(X, div2(Y))

    if even(Y):
        return mult(z, z)
    else:
        return mult(X, mult(z, z))


def gcd(X, Y):
    if zero(Y):
        return X
    (q, r) = divide(X, Y)
    return gcd(Y, r)



def addSum(n1, d1, n2, d2):
    N = add(mult(n1, d2), mult(n2, d1))
    D = mult(d1, d2)

    (N1, D1) = reduceFraction(N, D)

    return (N1, D1)#reduceFraction(N, D)


def reduceFraction(N, D):
    x = gcd(N, D)
    (N1, R1) = divide(N, x)
    (D1, R2) = divide(D, x)
    
    return (N1, D1)


# for all problems
def randomGenerator(n):
    # if n <= 50
    # generates a random integer with n bits
    # documentation doesn't mention how many bits are in the number
    d = SystemRandom()
    s = [d.randrange(2) for i in range(bin2dec(n) - 2)]

   
    return [1] + s + [1]

# problem 1
def modExp(X, Y, Z):
    # Takes in two reversed binary strings and returns
    # a binary string of X^Y mod Z.
    if zero(Y):
         return [1]

    z = modExp(X, div2(Y), Z)
    if even(Y):
        a = mult(z, z)
        (q, r) = divide(a, Z)
        return r
    else:
        a = mult(X, mult(z, z))
        (q, r) = divide(a, Z)
        return r

def primality(N):
    # assume N is a reversed bit array
    # pick a number from [1] to N
    # the random number must be in range 1 < random_number < N
    random_number = randomGenerator(dec2bin(len(N)) )
    while not (compare(random_number, [1]) == 1 and compare(random_number, N) == 2):
            random_number = randomGenerator(dec2bin(len(N)))

    if compare(modExp(random_number, sub(N, [1]), N), [1]) == 0:
        return [1]
    return [0]


def primality2(N, k):

    # calls primality 
    # generate random number k times

    for i in range(bin2dec(k)):
        #print()
        if compare(primality(N), [0]) == 0:
            print("No")
            return False
    # test k random numbers
    #if random_number is passes the test then return true
    print("yes")
    return True
        

def primality3(N, k):
    
    # an array for testing N with -> 2,3,5,7
    a = [2,3,5,7] # note: all these numbers must be converted to nbinary 
    

    for i in range(len(a)):
        binaryA = dec2bin(a[i])
        binaryN = N
        binaryZero = dec2bin(0)
        binaryOne = dec2bin(1)

        (q,r) = divide(binaryN, binaryA)
        # remainder == 0
        if( compare(r, binaryZero) == 0 ):
            # quotient == 1
            if( compare(q, binaryOne) == 0 ):
                print("yes")
                return True
            # quotient > 1
            print("No")     
            return False
        
        
    return primality2(N, k)
def problem1():
    # N is a binary integer
    N = dec2bin(int(input("enter a number")))

    # k is a binary confidence integer
    k = dec2bin(int(input("enter a confidence parameter")))

    return primality3(N, k)
# problem 2
def primality4(n, k):
    # n <= 50
    v = randomGenerator(n)
    while( primality3(v, k) == False) :
        v = randomGenerator(n)
    return v

#primality3(dec2bin(23), dec2bin(1))
def problem2():

    n = dec2bin(int(input("enter a number")))

    while compare(n, dec2bin(50)) == 1:
        n = dec2bin(int(input("your number is not <= 50 enter a number")))

    k = dec2bin(int(input("enter a confidence parameter")))

    # n is binary number <= 50
    # k is the confidence parameter
    return bin2dec(primality4(n, k))

def subW2sCompliment(X, Y, s):
    # has no idea X may be negative
    #print(bin2dec(X), bin2dec(Y))
    # designed to work with egcd
    # X and Y are positive, binary numbers
    # The result is the binary representation of X - Y in twos complement.
    if len(Y) == 1 and Y[0] == 0:
        return (X, s)
    (X1, Y1) = pad(X, Y)
    X1.append(0) #Add one extra bit for the flags for two's complement
    Y1.append(0)
    Y1 = twosComplement(Y1) #Subtract
    result = add(X1, Y1)

    # hack off extra carry bit
    negative_bit = result[len(result) - 1]
    if len(result) > len(X1):
        result = result[:len(result)]

    # (0)' = [1,0]
    # last bit should be sign bit
    s = [negative_bit]
    # converts it out of 2's compliment so the actual binary representation of the value can be used
    return (twosComplement(result), s)

def egcd(a,b):

    # b == 0
    if compare(b, [0]) == 0:
        # default set s to 3
        return ([1], [0], a, [1,1])

    # claims noneType error
    (q, r) = divide(a, b)

    (x1, y1, d, s) = egcd(b, r)

    # (y1, x1 - floor(a/b), d)
    #x1 - floor(a/b)y1
    (q2, r2) = divide(a, b)

    #x1 - r2y1
    # multiply doesn't assume wether one of its operands is negative
    # f-loor(a/b) (-x)
    # s > 1 so y1 must be negative
    if compare(s,[1]) == 1:
        # if y1 is a negative add the two numbers together,
        # then set s to 1
        new_x =	add(x1, mult(q2,y1))
        s = [1]
        # else subtract as usual

    # s == 1
    else:

        #x1 - r2y1                    
        #  subW2sCompliment(0, mult(q2, y1)) = -100
        # x1 - floor(a/b)y1
        # x is negative and - floor(a/b)y1 is nagative
        # first_part = 0 - floor(a/b)y1
        # second_part = x1 + first_part
        # result = 0 - second_part
        (result_from_from_second_term, s1) = subW2sCompliment([0], mult(q2, y1), s)
        positive_sub_part = add(x1, result_from_from_second_term)

        (actual_result, s) = subW2sCompliment([0], positive_sub_part, s)
        new_x = actual_result
        #s = s2
        # subW2sCompliment(0,  add(x1, subW2sCompliment(0, mult(q2, y1))))
        #(new_x, s) = subW2sCompliment(x1, mult(q2, y1), s)
        #if compare(s1, [])
        s = [0,1]

    #print(bin2dec(y1), bin2dec(new_x), bin2dec(d), bin2dec(s))
    #print()
    return (y1, new_x, d, s)

# should work with modinverse teacher wrote
def modinv(a, n):
    # computes a^(-1) mod n
    # claims non type error
    (x, y, d, s) = egcd(a, n)
    if compare(d, [1]) != 0:
        return []
    #print(bin2dec(x), bin2dec(y))

    #binaryX = dec2bin(x)
    #binaryY = dec2bin(n)
    (quotient, remainder) = divide(x, n)
    #print("after divide")
    #print(bin2dec(remainder), s)


    if compare(s, [0, 1]) == 0:
        #print("remainder then")
        #print(bin2dec(remainder))
        return remainder
    else:
        #print("correct")
        (q, r) = divide(x, n)
        remainder = sub(mult(add(q, [1]), n), x)
        #print(bin2dec(remainder))
        return remainder
def findE(k, p, q):
    # e = generate random number with k bits
    e = randomGenerator(k)
    while( compare(gcd(e, mult(sub(p, [1]),  sub(q, [1])) ), [1]) != 0 ):
        e = randomGenerator(k)
    return e
    # while compare(gcd(e, (p - 1)(q - 1)), [1]) != 0
        # e = generate random number with k bits
    # return e
def rsaAlgorithm(n, k):
    #n = dec2bin(50)
    #k = dec2bin(50)
    p = primality4(n, k)
    q = primality4(n, k)
    # stopped working when 50 bit numbers started being used
    # run untill b == 1
    #while compare(b, [1]) != 0:
    while( compare(p, q) == 0 ):
        p = primality4(n, k)
        q = primality4(n, k)
    N = mult(p, q)
    #print("N", bin2dec(N))
    #p = dec2bin(5)
    #q = dec2bin(7)

    e = findE(n, p, q)
    #print(len(e), len(p), len(q))
    #print("e", bin2dec(e), "p", bin2dec(p), "q", bin2dec(q))
    #print()
    # claimed non
    #print(bin2dec(e))
    # appropriate e's are generated such that an inverse can't be computed(wolfram alpha agrees with this)
    phi = mult(sub(p, [1]),  sub(q, [1]))
    #e = dec2bin(11)
    #phi = dec2bin(24)
    d = modinv(e, phi)
    #print("d", bin2dec(d), "(p - 1)(q - 1)", bin2dec(phi))
    #print()
    #(a, b) = divide(mult(e, d), phi)
    #print(bin2dec(e), "*", bin2dec(d), "mod", bin2dec(phi), "=", bin2dec(b))
    print("N", bin2dec(N))
    print("E", bin2dec(e))
    print("D", bin2dec(d))
    M = dec2bin(int(input("Please enter a message.  It has to be an integer\n")))
    #print(bin2dec(M))
    #exit()
    # 231, 74
    #print("message")
    #print(bin2dec(M))
    #encrypt = M^e mod N
    encrypt = modExp(M, e, N)
    print("encrypted message")
    print(bin2dec(encrypt))
    #decrypt = encrypt^d mod N
    decrypt = modExp(encrypt, d, N)
    print("decrypted message")
    print(bin2dec(decrypt))

def problem3():
    # n is binary number <= 50
    # k is confidence parameter
    n = dec2bin(int(input("enter a number\n")))
    while compare(n, dec2bin(50)) == 1:
        n = dec2bin(int(input("your number is not <= 50 enter a number\n")))

    k = dec2bin(int(input("enter a confidence parameter\n")))
    rsaAlgorithm(n, k)
    #for x in range(1,30):
     #   rsaAlgorithm(n, k)

#print("egcd test")
#print(modinv(dec2bin(345), dec2bin(767)))
#print("problem3 test")
#problem3()
def main():
    moreInput = True
    while moreInput:
        print("Which option would you like to choose? (1, 2, 3, or 4)")
        print("1. faster primality test")
        print("2. generate an n bit randome number and test if it is prime")
        print("3. rsa")
        print("4. Quit")
        selection = input("Your selection: ")

        if selection == "1":
            print(problem1())
        elif selection == "2":
            print(problem2())
        elif selection == "3":
            problem3()
        elif selection == "4":
            moreInput = False
        else:
            print("Unknown input.")
main()
#instructions for running:
#python3 p2.py