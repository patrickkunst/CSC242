# Patrick Kunst
# CSC 241
# lab1.py

def printTwoLargest():
    x=1 #Sets initial value for while loop
    nums = []
    while x>0:
        n = str(input('Please enter a number: '))
        if '.' in n:
            x = float(n)
        else:
            x = int(n)
        if x > 0:
            nums.append(x)

    #Sort numbers, get largest, then remove to get second largest

    if len(nums)==0:
        print('No positive numbers were entered')
    else: 
        nums.sort()
        l = max(nums)
        print('The largest is {}'.format(l))

    if len(nums)>1:
        nums.pop()
        sl = max(nums)
        print('The second largest is {}'.format(sl))

def printWordsLines(txt_file):
    f = open(txt_file)
    lines = f.readlines()
    f.close()

    num_lines = len(lines)

    words = 0
    for line in lines:
        w = line.split()
        for x in w:
            words += 1

    print('The file {} contains {} words and {} lines.'.format(txt_file, words, num_lines))

    
def reverseDict(d):
    rev = dict()

    for k in d.keys():
        rev[d[k]] = k
    return rev

if __name__=='__main__':
    import doctest
    print(doctest.testfile('lab1TEST.py'))
