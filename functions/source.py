# Beautiful Soup is a Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup

import urllib2

# simple  HTML and XTHML parser
from HTMLParser import HTMLParser

import collections

# from htmlentitydefs import name2codepoint


class MyHTMLParser(HTMLParser):
    
    def __init__(self):
        """ Initialize and reset this instance """
        
        self.reset()  
        self.start = []
        self.end = []

    def handle_starttag(self, tag, attrs):
        """ Add start tag to list on object """

        self.start.append(tag)

        # for attr in attrs:
        #     print "     attr:", attr
    def handle_endtag(self, tag):
        """ Add end tag to list on object """
        self.end.append(tag)


    # def handle_data(self, data):
    #     print "Data     :", data
    # def handle_comment(self, data):
    #     print "Comment  :", data
    # def handle_entityref(self, name):
    #     c = unichr(name2codepoint[name])
    #     print "Named ent:", c
    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = unichr(int(name[1:], 16))
    #     else:
    #         c = unichr(int(name))
    #     print "Num ent  :", c
    # def handle_decl(self, data):
    #     print "Decl     :", data

def convert_url_text(url):
    """ Convert html of a URL (as a string) to a string """  # check that it is a string

    # urllib2 opens a URL and reads the HTML from the URL
    response = urllib2.urlopen(url)
    html = response.read()

    return html


def count_tags(url):
    """ Based on a URL, outputs count of the tags in the document """

    counter = {}

    html = convert_url_text(url)

    # MYHTMLParser object is able to be fed HTML, where it can recognize tags
    parser = MyHTMLParser()
    parser.feed(html)
   
    tags = parser.start

    # iterate through and count tags
    for tag in tags:
        counter[tag] = counter.get(tag, 0) + 1

    ordered_counter = collections.OrderedDict(sorted(counter.items()))
    
    return ordered_counter


def source_url(url):
    """ Based on a URL, outputs the source text of the doument """

    html = convert_url_text(url)

    # BeatuifulSoup obejct works with parser with given html 
    soup = BeautifulSoup(html, "html.parser")

    return soup
