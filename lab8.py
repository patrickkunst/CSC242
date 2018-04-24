# Patrick Kunst
# Lab 8
# CSC 242

def count(lst, target):
    num = 0

    if type(lst)!=list:
        if lst == target:
            return 1
        return 0

    else:
        num = 0
        for x in lst:
            num += count(x, target)
        return num


from html.parser import HTMLParser
from urllib.request import urlopen

class HeadingParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.heads = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}
        self.flag = False
        self.content = list()

    def handle_starttag(self, tag, attrs):
        if tag in self.heads:
            self.flag = True

    def handle_endtag(self, tag):
        if tag in self.heads:
            self.flag = False

    def handle_data(self, data):
        if self.flag==True and data.strip() != '':
            self.content.append(data.strip())

    def getheadings(self):
        return self.content


def testHP(url):
    parse = HeadingParser()
    parse.feed(urlopen(url).read().decode())
    return parse.getheadings()

if __name__=='__main__':
    import doctest
    print(doctest.testfile('lab8TEST.py'))





















    
    
