#Patrick Kunst
#CSC 242
#Lab 3

class Stack:
    def __init__(self, ls=list()):
        '''Constructs an empty stack, or init with a list of items'''
        self.stack = list(ls)

    def __repr__(self):
        return 'Stack({})'.format(self.stack)

    def push(self, item):
        '''takes an item as input and pushes it to top'''
        self.stack.append(item)

    def pop(self):
        '''removes an item and returns the item at the top of stack'''
        x = self.stack[-1]
        self.stack = list(self.stack[:-1])
        return x

    def isEmpty(self):
        '''returns True if stack is empty, false otherwise'''
        if len(self.stack) == 0:
            return True
        return False

    def __len__(self):
        '''returns the length of the stack'''
        return len(self.stack)

    def __getitem__(self, index):
        '''returns the item at the index'''
        return self.stack[index]

def parenthesesMatch(p):
    myStack = Stack()
    parenDict = {')':'(', ']':'[', '}':'{'}#To make if statements easier
    for c in p:
        if c in parenDict.values(): myStack.push(c)

        elif c in parenDict.keys():
            if myStack.isEmpty() or myStack.pop() != parenDict[c]: return False 

    if myStack.isEmpty(): return True#Check if any opening marks leftover
    return False


if __name__=='__main__':
    import doctest
    print( doctest.testfile('lab3TEST.py') )
