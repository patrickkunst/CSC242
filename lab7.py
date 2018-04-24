# Patrick Kunst
# Lab 7
# CSC 242

def printPattern(a, b=0):#FIX LATER
    if a==1:
        print(' '*b + '*')
    else:
        printPattern(a//2, b)
        print(' '*b + '*'*a)
        printPattern(a//2, b+a//2)

    

def gcd(m, n):
    if m==0:
        return n

    elif n==0:
        return m

    elif m>n:
        return(gcd(n, m-n))

    else:
        return(gcd(m, n-m))

def f(x):
    if x==0:
        return 0

    elif x==1:
        return 1

    else:
        return (f(x-1) + f(x-2))/2

if __name__=='__main__':
    import doctest
    doctest.testfile('lab7TEST.py')
