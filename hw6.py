# Patrick Kunst
# CSC 242
# hw6.py

from web import LinkCollector
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
from urllib.error import URLError

class ImageCollector(HTMLParser):

    def __init__(self, url):
        HTMLParser.__init__(self)
        self.url = url
        self.images = set()

    def handle_starttag(self, tag, attrs):
        if tag=='img':
            for attr, val in attrs:
                if attr=='src':
                    self.images.add(urljoin(self.url, val))

    def getImages(self):
        return self.images

from web import Crawler

class ImageCrawler(Crawler):

    def __init__(self):
        Crawler.__init__(self)
        self.img = set()

    def crawl(self, url, depth, relativeOnly=True):
        ic = ImageCollector(url)
        try:
            ic.feed(urlopen(url).read().decode())
        except(URLError, UnicodeDecodeError):
            pass

        self.img.update(ic.getImages())

        Crawler.crawl(self, url, depth, relativeOnly)

    
    def getImages(self):
        return self.img


def scrapeImages(url, filename, depth, relativeOnly=True):
    file = open(filename, 'w')

    if depth>0:
        ic = ImageCrawler()
        ic.crawl(url, depth, relativeOnly)

        for img in ic.getImages():
            file.write('<img src=' + img + '>')

        scrapeImages(url, filename, depth-1, relativeOnly)



if __name__=='__main__':
    import doctest
    print(doctest.testfile('hw6TEST.py'))
    








        
