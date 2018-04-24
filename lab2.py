# Patrick Kunst (Collaborated with Kevin Trainor
# Lab 2, CSC 242

class Animal:
    def __init__(self, spec='default', noise='default', a=0):
        self.species = spec
        self.language = noise
        self.age = a

    def __repr__(self):
        return 'Animal(\'{}\',\'{}\',{})'.format(self.species, self.language, self.age)

    def setSpecies(self, s):
        self.species = s

    def setLanguage(self, l):
        self.language = l

    def setAge(self, a):
        self.age = int(a)

    def speak(self):
        print('I am a {} year-old {} and I {}.'.format(self.age, self.species, self.language))
              
def processAnimals(file_name):
    file = open(file_name)
    lines = file.readlines()

    for l in range(len(lines)):
        lines[l] = lines[l].replace('\n', '') #Removes newline char to read better
        lines[l] = lines[l].split(',')
        
    an_List = []
    for x in lines:
        a = Animal(x[0], x[1], x[2])
        a.speak()
        an_List.append(a)

    return an_List

if __name__=='__main__':
    import doctest
    print( doctest.testfile('lab2TEST.py') )

