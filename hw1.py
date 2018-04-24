##########################################
#Patrick Kunst, collab with Kevin Trainor#
##########################################

class BankAccount:
    def __init__(self, b=0):
        self.bal = b

    def __repr__(self):
        return 'BankAccount({})'.format(self.bal)

    def set(self, m):
        self.bal = m

    def withdraw(self, m):
        self.bal -= m

    def deposit(self, m):
        self.bal += m

    def balance(self):
        return self.bal

def processAccount(file_name):
    file = open(file_name)
    lines = file.readlines()
    acc = BankAccount()
    acc.set(float(lines[0]))
    for i in range(1, len(lines)):
        amt = float(lines[i][2:-1])#First two characters are w/d and space, rest is the amt
        if lines[i][0] == 'w' or lines[i][0] == 'W':
            acc.withdraw(amt)
        elif lines[i][0] == 'd' or lines[i][0] == 'D':
            acc.deposit(amt)

    return acc
    

    
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw1TEST.py'))
