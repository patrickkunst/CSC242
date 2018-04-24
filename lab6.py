def silly(n):
    if n==0: pass
    elif n==1: print('*!', end='')
    else:
        print('*', end='')
        silly(n-1)
        print('!', end='')

def stars(n):
    if n==1: print('*')
    else:
        stars(n-1)
        print('*'*n)
        stars(n-1)

def pattern(n):
    if n==1: print('1', end='')
    else:
        pattern(n//2)
        pattern(n//2)
        print(n, end='')


if __name__=='__main__':
    import doctest
    print(doctest.testfile('lab6TEST.py'))
