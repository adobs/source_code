"""
classes.py

Create the MyHTMLParser class, which inherits properties from the HTMLParser 
class.  The main functionality is that an instance of MyHTMLParser captures the 
tags used in the HTML associated with that object.
"""

# simple  HTML and XTHML parser
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    
    def __init__(self):
        """ Initialize and reset this instance """
        
        self.reset()  
        self.start = []

    def handle_starttag(self, tag, attrs):
        """ Add start tag to list on object """

        self.start.append(tag)
