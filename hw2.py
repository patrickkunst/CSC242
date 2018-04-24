class Pizza:
    def __init__(self, s='M', top=set()):
        self.size = s
        self.toppings = set(top)

    def __repr__(self):
        return 'Pizza(\'{}\',{})'.format(self.size, self.toppings)

    def __eq__(self, other):
        return self.size == other.size and self.toppings == other.toppings

    def setSize(self, s):
        self.size = s

    def getSize(self):
        return self.size

    def addTopping(self, top):
        self.toppings.add(top)

    def removeTopping(self, top):
        self.toppings.discard(top)

    def price(self):
        if self.size == 'S':
            p = 6.25 + .7*len(self.toppings)
        elif self.size == 'M':
            p = 9.95 + 1.45*len(self.toppings)
        elif self.size == 'L':
            p = 12.95 + 1.85*len(self.toppings)

        return p

def orderPizza():
    print('Welcome to Python Pizza!')
    size = input('What size pizza would you like (S,M,L): ')
    top_set = set()
    top = 'DEFAULT'#For while loop
    while top != '':
        top = input('Type topping to add (or Enter to quit): ')
        if top != '':
            top_set.add(top)
    cust_pizza = Pizza(size, top_set)
    print('Thanks for ordering!')
    print('Your pizza costs ${}'.format(cust_pizza.price()))
    return cust_pizza

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw2TEST.py'))


        
