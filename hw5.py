def pascalLine(num):
    if num == 0: return [1]
    elif num == 1: return [1, 1]
    else:
        pasc = list(None for i in range(num+1))
        
        for i in range(num):
            if (i==0):
                pasc[i] = 1
            else:
                p = pascalLine(num-1)
                pasc[i] = p[i] + p[i-1]
        pasc[-1] = 1
        return pasc

def levy(num):
    if num==0: return 'F'
    else:
        return 'L' + levy(num-1) + 'RR' + levy(num-1) + 'L'


def base(n, b):
    if n<=1:
        return str(n)
    else:
        ans = str(base(n//b,b)) + str(n%b)
        if ans[0] == '0':
            return ans[1:]
        return ans


if __name__=='__main__':
    import doctest
    print(doctest.testfile('hw5TEST.py'))

