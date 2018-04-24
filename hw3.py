# Patrick Kunst
# HW 3

class EmptyStatError(Exception):
    pass

class Stat:
    def __init__(self, ls=list()):
        self.nums = list(ls)

    def __repr__(self):
        return 'Stat({})'.format(self.nums)

    def __len__(self):
        return len(self.nums)

    def add(self, num):
        self.nums.append(num)

    def min(self):
        if len(self) == 0: raise EmptyStatError("empty stat does not have a min")
        return min(self.nums)

    def max(self):
        if len(self)==0: raise EmptyStatError("empty Stat does not have a max")
        return max(self.nums)
    
    def sum(self):
        if len(self)==0: return 0
        return sum(self.nums)

    def mean(self):
        if len(self)==0: raise EmptyStatError("empty Stat does not have a min")
        return sum(self.nums)/len(self.nums)

    def clear(self):
        self.nums = list()

class NotIntError(Exception):
    pass

class intlist(list):
    def __init__(self, ls = list()):
        for item in ls:
            if type(item) != int:
                raise NotIntError(str(item) + " not an int")
        list.__init__(self, ls)

    def __repr__(self):
        return 'intlist({})'.format(list(self))

    def __setitem__(self, index, item):
        if type(item) != int: raise NotIntError(str(item) + " not an int")
        else: list.__setitem__(self, index, item)

    def append(self, item):
        if type(item)==int:
            self = list.append(self, item)
        else: raise NotIntError(str(item) + " not an int")

    def insert(self, index, item):
        if type(item)==int:
            self = list.insert(self, index, item)
        else: raise NotIntError(str(item) + " not an int")

    def extend(self, iterable):
        for item in iterable:
            if type(item) != int:
                raise NotIntError(str(item) + " not an int")
            self.append(item)

    def odds(self):
        oddList = intlist()
        for item in self:
            if item%2 == 1: oddList.append(item)

        return oddList

    def evens(self):
        evenList = intlist()
        for item in self:
            if item%2 == 0: evenList.append(item)

        return evenList
    
    
if __name__ == '__main__':
    import doctest
    print(doctest.testfile('hw3TEST.py'))



