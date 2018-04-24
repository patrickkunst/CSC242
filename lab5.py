# Patrick Kunst
# Lab 5

from tkinter import *
from tkinter.messagebox import showinfo

class UnitError(Exception):
    pass

class Temperature:
    def __init__(self, t=0.0, s='C'):
        try:
            self.temp = float(t)
        except(ValueError):
            raise ValueError('could not convert string to float: ' + t)
        good_scales = {'C', 'F'}
        if type(s) != str or s.upper() not in good_scales:
            raise UnitError('Unrecognized temperature unit ' + repr(str(s)))

        self.scale = s.upper()

    def __repr__(self):
        return 'Temperature({},{})'.format(self.temp, repr(self.scale))

    def __str__(self):
        return '{}°{}'.format(self.temp, self.scale)

    def convert(self):
        if self.scale == 'F':
            return Temperature(((5/9)*self.temp - 32), 'C')
        else:
            return Temperature(((9/5)*self.temp + 32), 'F')

            
    def __eq__(self, other):
        # convert both to farenheit to make comparison
        if self.scale != 'F':
            temporary = self.convert()
            t1 = temporary.temp
        else: t1 = self.temp

        if other.scale != 'F':
            temporary = other.convert()
            t2 = temporary.temp
        else: t2 = other.temp

        return t1 == t2

class TempConverter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)

        Label(self, text='Temperature: ').grid(row=0, column=0)
        
        self.temp_entry = Entry(self)
        self.temp_entry.grid(row=0,column=1,columnspan=8)

        Label(self, text='Unit (C or F): ').grid(row=1, column=0)
        
        self.unit_entry = Entry(self)
        self.unit_entry.grid(row=1, column=1, columnspan=8)
        def cmd():
            self.onClick(self.temp_entry.get(), self.unit_entry.get())
            
        Button(self, command=cmd, text='Click to convert', width = 15).grid(
            row=2, column=2)

    def onClick(self, t, s):
        try:
            t = float(t)
        except(ValueError):
            showinfo('Error:', 'Temperature must be a decimal or integer')

        if s.upper() not in {'C', 'F'}:
            showinfo('Error:', 'Unit should be either C or F')
        else:
            temp_obj = Temperature(t, s)
            showinfo('Conversion', str(temp_obj) + '=' + str(temp_obj.convert()))
if __name__ == '__main__':
    import doctest
    print(doctest.testfile('lab5TEST.py'))


            
