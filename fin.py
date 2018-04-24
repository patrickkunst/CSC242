# Final?

from html.parser import HTMLParser

class CodeCollector(HTMLParser):

    def __init__(self, url):
        HTMLParser.__init__(self)

        self.code = list()
        self.url = url
        self.flag = False

    def handle_starttag(self, tag, attrs):
        if tag=='code':
            self.flag = True

    def handle_data(self, data):
        if self.flag == True:
            self.code.append(data)

    def handle_endtag(self, tag):
        self.flag = False

    def getCode(self):
        return self.code


    
