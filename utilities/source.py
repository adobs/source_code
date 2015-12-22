"""
source.py

Helper functions.  Based on the URL in the search box, returns information 
(to be JSONified) about tag count and source text 
"""

# Beautiful Soup (bs4) is a Python library for pulling data out of HTML and XML files
from bs4 import BeautifulSoup
import collections
from classes import MyHTMLParser
import urllib2

def convert_url_text(url):
    """ Convert html of a URL (as a string) to a string """

    # urllib2 opens a URL and reads the HTML from the URL
    response = urllib2.urlopen(url)

    html = response.read()

    return html


def is_valid_url(url):
    """ Checks to see if the URL inputted is valid.  Returns boolean string """
    
    try:
        urllib2.urlopen(url)
        return "True"

    except:
        return "False"


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


def escape_html(text):
    """ For an HTML text, escapes characters that would be read as markup

    Adds in a line break after '>' to make reading the text easier 
    """

    edited_text = str(text).replace("<", "&lt;").replace(">", "&gt;<br>")

    return edited_text


def source_text(url):
    """ Based on a URL, outputs the source text of the document """

    html = convert_url_text(url)

    # BeatuifulSoup obejct works with parser with given html
    soup = escape_html(BeautifulSoup(html, "html.parser"))

    return soup
