# Patrick Kunst

from tkinter import *
from tkinter.messagebox import showinfo

def mask(word, ex):
    masked = ''
    for i in word:
        if i in ex:
            masked += i
        else:
            masked += '?'
    return masked

class hangman(Frame):
    def __init__(self, word, parent=None):
        self.good = set()
        self.wrong = set()
        self.word = word.upper()
        
        Frame.__init__(self, parent)

        Label(self, text='Word: ').grid(row=0, column=0)
        self.word_entry = Entry(self)
        self.word_entry.grid(row=0, column=1, columnspan=5)
        
        Label(self, text='Right: ').grid(row=1, column=0)
        self.right_entry = Entry(self)
        self.right_entry.grid(row=1, column=1, columnspan=5)
        
        Label(self, text='Wrong: ').grid(row=2, column=0)
        self.wrong_entry = Entry(self)
        self.wrong_entry.grid(row=2, column=1, columnspan=5)

        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(len(letters)):
            def cmd(key=letters[i]):
                self.click(key)
                
            b = Button(self, command=cmd, text=letters[i], width=3, height=3)
            b.grid(row=3+i//6, column=i%6)

    def click(self, l):
        if l in self.word and l not in self.good:
            self.good.add(l)
            self.right_entry.insert(END, l)
            masked_word = mask(self.word, self.good)
            self.word_entry.delete(0,END)
            self.word_entry.insert(END, masked_word)
            if '?' not in masked_word:
                showinfo('Hangman', 'You win!')
            
        elif l not in self.word and l not in self.wrong:
            self.wrong.add(l)
            self.wrong_entry.insert(END, l)
            if len(self.wrong) >= 6:
                showinfo('Hangman', 'You Lose!')

if __name__=='__main__':
    import doctest
    print(doctest.testfile('hw4TEST.py'))




