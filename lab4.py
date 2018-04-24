# Patrick Kunst
# Lab 4
# CSC 242

class Mapping(dict):
    def __init__(self, myDict = dict()):
        for k in myDict.keys():
            if k in self:
                dict.pop(self, self[k])
            self[k] = myDict[k]
            self[myDict[k]] = k

    def __repr__(self):
        return "Mapping({})".format(dict.__repr__((self)))

    def pop(self, k):
        if k in self.keys():
            dict.pop(self, self[k])
            if k in self.keys(): dict.pop(self, k)
                     
    def __setitem__(self, k, v):
        if k in self:
            dict.pop(self, k)
            
        dict.__setitem__(self, k, v)
        dict.__setitem__(self, v, k)

if __name__=='__main__':
    import doctest
    print(doctest.testfile('lab4TEST.py'))
