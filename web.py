# web.py

##### html crash course #####

# see sample.html

'''
html - hypertext markup language

text document with content "marked up"
for display in a browser

editors:
   text editor
   wysiwyg editor

create sample.html:
    tags
    attributes

<a href='http://cnn.com' target=blank>CNN</a>

opening tag <a>
closing tag </a>
data is stuff in between "CNN"
href is an attribute
'http://cnn.com' is the value of the href attribute

most tags come in pairs, but
not all tags have closing tag: <br>,<img>
    

'''

##### using Python to access html documents #####

'''
html documents are really text files
if file is on your local computer, open it!


>>> len( open('sample.html').read())
1163
>>> 
>>> # what about remote files?
>>> from urllib.request import *
>>> response = urlopen( 'http://cnn.com' )
>>> html = response.read().decode()
>>> html[:150]
'<!DOCTYPE html><html class="no-js"><head><meta content="IE=edge,chrome=1" http-equiv="X-UA-Compatible"><meta charset="utf-8"><meta content="text/html"'
>>> 
>>> html.count('<a>')
0
>>> html.count('</a>')
219
>>> 
>>> # retrieve and save files
>>> urlretrieve( 'http://a57.foxnews.com/images.foxnews.com/content/fox-news/tech/2018/03/02/terrifying-video-goes-viral-after-shark-charges-at-scuba-diver/_jcr_content/par/featured_image/media-0.img.jpg/931/524/1520008797346.jpg?ve=1&tl=1&text=big-top-image', 'newShark.jpg')
('newShark.jpg', <http.client.HTTPMessage object at 0x0148D510>)
>>> 
'''

##### HTMLParser #####

'''
HTMLParser - parses (breaks up) an html document
into usable pieces.  when you 'feed' the parser
it automatically calls three methods as the items
are encountered

    handle_starttag - <a href='...'>
    handle_data - CNN
    handle_endtag - </a>

in HTMLParser, these three methods are
"stubs", i.e. implementation is pass.
we get the behaviour we want by
subclassing (inheriting from) HTMLParser
and overriding these methods
'''

from html.parser import HTMLParser

class PrintParser( HTMLParser ):

    # inherit init and feed

    # overrides
    def handle_starttag(self,tag,attrs):
        print('handle_starttag',tag,attrs)
    def handle_data(self,data):
        print('handle_data',data)
    def handle_endtag(self,tag):
        print('handle_endtag',tag )
        

'''
>>> p = PrintParser()
>>> p.feed( open('sample.html').read() )
...
handle_starttag li []
handle_starttag a [('href', 'http://cnn.com'), ('target', 'blank')]
handle_data CNN
handle_endtag a
handle_endtag li
...
'''

#### urljoin #####
'''
we want to collect links (hrefs in <a> tag)
they can either be

absolute - http://cnn.com
relative - doc.html

we need to store them in absolute form
urljoin turns relative urls into absolute urls

>>> from urllib.parse import urljoin
>>> urljoin( 'http://cnn.com', 'doc.html' )
'http://cnn.com/doc.html'
>>> urljoin( 'http://cnn.com', 'http://cnn.com' )
'http://cnn.com'
>>> urljoin( 'http://cnn.com', 'http://cnn.com/doc.html' )
'http://cnn.com/doc.html'
>>> urljoin( 'http://cnn.com/pics', 'pics/shark.jpg' )
'http://cnn.com/pics/shark.jpg'
>>> 

'''

##### LinkCollector #####
'''
want this to work:
>>> lc = LinkCollector( 'http://cnn.com' )
>>> lc.feed( urlopen('http://cnn.com').read().decode() )
>>> lc.getAbsolutes()
... set of absolute links would be listed ...
>>> lc.getRelatives()
... set of relative links would be listed ...
>>> lc.getLinks()
... set of all links would be listed ...
'''


from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin

class LinkCollector(HTMLParser):

    # init? yes
    def __init__(self,url):
        # do I need this?
        HTMLParser.__init__(self)
        # add attributes
        self.url = url
        self.relativeLinks = set()
        self.absoluteLinks = set()

    def handle_starttag(self,tag,attrs):
        if tag=='a':
            for attr,val in attrs:
                if attr=='href':
                    #print( tag, attr, val )
                    link = urljoin( self.url, val )
                    if val[:4]=='http': # absolute
                        self.absoluteLinks.add( link )
                    else: # relative
                        self.relativeLinks.add( link )
                        


    def getRelatives(self):
        return self.relativeLinks
    def getAbsolutes(self):
        return self.absoluteLinks
    def getLinks(self):
        return self.relativeLinks.union( self.absoluteLinks )


'''
>>> lc = LinkCollector( 'http://cnn.com' )
>>> lc.feed( urlopen('http://cnn.com').read().decode())
>>> len( lc.getRelatives() )
81
>>> len( lc.getAbsolutes() )
26
>>> len( lc.getLinks() )
106
>>> 

'''

'''
make this work:
>>> scrapeLinks( 'http://cnn.com', 'cnn.html')
... read all links from cnn and write to an html file called cnn.html ...

'''

def scrapeLinks(url,filename):

    # use a LinkCollector to get the links
    lc = LinkCollector(url)
    lc.feed( urlopen(url).read().decode() )

    # write them out to a file
    file = open(filename,'w')
    file.write( '<html><body>\n')
    for link in lc.getLinks():
        file.write( '<a href={}> {} </a><br>\n'.format(link,link) )
    file.write( '</body></html>')
    file.close()
    
##### Crawler #####
        
'''
want this to work:
>>> c = Crawler()
>>> c.crawl( 'http://www.kli.org/', 2, True)
... recursively crawl all relative (True) links
found at kli.org to a depth of 2 ...
>>> c.getCrawled()
... set of urls that were crawled (read the html) ...
>>> c.getFound()
... set of urls that were found as links.  It
includes the crawled ones but also includes founds
links that have not been read and also dead links ...
>>> c.getDead()
... returns urls that failed to be read ...
'''

from urllib.error import URLError
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib.parse import urljoin
from http.cookiejar import CookieJar # need to do more

# based on Perkovic text book but
# with some changes

class Crawler():   # does not inherit

    def __init__(self):
        self.crawled = set()
        self.found = set()
        self.dead = set()

    # c.crawl( 'http://www.kli.org/', 2, True)
    def crawl(self,url,depth,relativeOnly=True):

        # read the html found at url
        lc = LinkCollector(url)
        try:
            lc.feed( urlopen(url).read().decode() )
        except (UnicodeDecodeError, URLError):
            self.dead.add( url )
            
        self.crawled.add( url )

        # extract the links within that html
        if relativeOnly:
            found = lc.getRelatives()
        else:
            found = lc.getLinks()
        self.found.update( found )  # set's version of extend is update

        # recursively crawl all the (new) links found
        if depth>0:
            for link in found:
                if link not in self.crawled:
                    self.crawl(link,depth-1,relativeOnly)
            

    def getCrawled(self):
        return self.crawled
    def getFound(self):
        return self.found
    def getDead(self):
        return self.dead
    

##### hw example - model for ImageCrawler #####


# like ImageCollector
class ButtonParser(HTMLParser):
    ''' collects actions associated to buttons '''

    def __init__(self):
        HTMLParser.__init__(self) 
        self.actions = set()

    def handle_starttag(self,tag,attrs):
        if tag=='button':
            #print( tag, attrs)
            for attr,val in attrs:
                if attr=='onclick':
                    # collect the val
                    self.actions.add( val)

    def getActions(self):
        return self.actions


# collect Button Actions across
# multiple pages

# like ImageCrawler

class ButtonCrawler(Crawler):

    def __init__(self):
        Crawler.__init__(self)
        self.actions = set()

    # extend crawl method
    def crawl(self,url,depth,relativeOnly=True):
        # splice in Button collection
        bp = ButtonParser()
        try: # may fail
            bp.feed( urlopen(url).read().decode() )
        except (URLError, UnicodeDecodeError):
            pass

        self.actions.update( bp.getActions() )

        # call parent's crawl
        Crawler.crawl(self,url,depth,relativeOnly)


    def getActions(self):
        return self.actions











