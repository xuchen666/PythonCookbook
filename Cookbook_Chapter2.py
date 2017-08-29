#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:18:24 2017

@author: xuchenwang
"""

# 2.1 Splitting strings on any multiple delimiters
'''
You need to split a string into fields, but the delimiters (and spacing around them) 
aren’t consistent throughout the string.
'''
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
re.split(r'[;,\s]\s*',line)
re.split(r'(?:,|;|\s)\s*',line)
re.split(r'([;,\s])\s*',line)



# 2.2 Matching text at the start or end of the string
'''
You need to check the start or end of a string for specific text patterns, 
such as filename extensions, URL schemes, and so on.
'''

'''
Use startswith() or endswith() method, params: tuple, return: True/False
'''

url = 'http://www.python.org'

url.startswith('http:')        
url.endswith('org')


from urllib.request import urlopen

if url.startswith(('http:','https','ftp')):
    urlopen(url).read()
    
'''
import re
url = 'http://www.python.org'
re.match('http:|https:|ftp:',url)
'''



# 2.3 Matching strings using shell wildcard patterns
'''
You want to match text using the same wildcard patterns as are commonly used 
when working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.).
'''

'''
Wildcard:
    * --- everything, 0,1 or more chars
    ? --- exactly 1 char
    [seq]  ---  any 1 char in the sequence
    [!seq]  ---   any 1 char not in the sequence
'''

'''
fnmatch(),fnmatchcase(ori,match):  return True/False
'''

from fnmatch import fnmatch,fnmatchcase
fnmatch('a.txt','?.txt')




# 2.4 Matching or searching for text patterns
'''
You want to match or search text for a specific pattern.
'''

''' Simple case: str.find(), str.startswith(), str.endswith() '''
text = 'yeah, but no, but yeah, but no, but yeah'
text.find('no')   # return the first location of occurence


''' Complicated case: regular expression, import re '''
import re

# Simple case
text1 = '11/27/2012'
m = re.match('\d+/\d+/\d+',text1) # only check the first match
m.group() # returns the match 

m = re.match('\d+/\d+/\d+$',text1)  # match exactly the pattern
'''
\d : [0-9] only 1 digit
+: 1 or more chars the same as before
\d+: 1 or more digits
$: end of the string
'''


# Perform matches with the same pattern
datepat = re.compile('\d+/\d+/\d+')
datepat.match(text1)
datepat.find(text1)


# Find all matches in a string: findall() returns a list of matches
#                               finditer() returns matches iteratelly
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

re.findall('\d+/\d+/\d+',text)

for m in re.finditer('(\d+)/(\d+)/(\d+)',text):
    print(m.groups())


# Capture groups '()'
m = re.match('(\d+)/(\d+)/(\d+)',text1)
m.groups()
m.group(0)
m.group(1)




# 2.5 Searching and replacing text
'''
You want to search for and replace a text pattern in a string.
'''

'''Simple case: str.replace() '''
'''Complicated case: re.sub() '''
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
newtext = re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)
newtext,n = re.subn(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)




# 2.6 Searching and replacing case-insensitive text
'''
You need to search for and possibly replace text in a case-insensitive manner.
'''

text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python',text,flags=re.IGNORECASE)

# a callable function as a substitution
def matchcase(word): 
    def replace(m):
        text = m.group() 
        if text.isupper():
            return word.upper() 
        elif text.islower():
            return word.lower() 
        elif text[0].isupper():
            return word.capitalize() 
        else:
            return word 
    
    return replace

re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)




# 2.7 Specify a regular expression for the shortest match
'''
You’re trying to match a text pattern using regular expressions, but it is identifying 
the longest possible matches of a pattern. Instead, you would like to change it to find 
the shortest possible match.
'''
'''
\"\" : 引号
.: 任意单个字符, except for newline \n
*: 匹配任意字符， 0，1，多个， greedy
*?: nongreedy
'''

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
text2 = 'Computer says "no." Phone says "yes."'

str_pat.findall(text1)
str_pat.findall(text2)

re.findall(r'\"(.*?)\"',text2)




# 2.8 Writing a regular expression for multiple patterns
'''
You’re trying to match a block of text using a regular expression, but you need 
the match to span multiple lines.
'''
'''
Dot(.) : except for newline. (?:.|\n)
(?:  ) : noncapture group
'''

text1 = '/* this is a comment */' 
text2 = '''/* this is a
           ... multiline comment */ ... '''
           
comment = re.compile(r'/\*(.*?)\*/')
comment.findall(text1)
comment.findall(text2)

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)

'''
comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)  # makes . matches all chars
comment.findall(text2)
'''




# 2.9 Normalizing unicode text to a standard representation
'''
You’re working with Unicode strings, but need to make sure that all of the strings 
have the same underlying representation.
Certain characters can be represented by more than one valid sequence of code points. 
'''

s1 = 'Spicy Jalape\u00f1o' 
s2 = 'Spicy Jalapen\u0303o'

import unicodedata
t1 = unicodedata.normalize('NFC',s1)  # NFC NFD KNFC KNFD
t2 = unicodedata.normalize('NFC',s2)

''.join(c for c in t1 if not unicodedata.combining(c))





# Working with unicode characters in regular expressions
'''
You are using regular expressions to process text, but are concerned about the handling of 
Unicode characters.
'''

num = re.compile('\d+')
num.match('\u0661\u0662\u0663').group()




# 2.11 Stripping unwanted characters from strings
'''
You want to strip unwanted characters, such as whitespace, from the beginning, end, 
or middle of a text string.
'''

s = ' hello world \n'
s.strip()  
s.lstrip()
s.rstrip()
'''
s.strip(): strip newline, whitespace
s.strip('-')
'''

# Inner space: .replace(), .sub()
s.replace(' ','')
re.sub('\s+',' ',s)





# 2.12 Sanitizing and cleaning up text
'''
Some bored script kiddie has entered the text “pýtĥöñ” into a form on your web page 
and you’d like to clean it up somehow.
'''

s = 'pýtĥöñ\fis\tawesome\r\n'

remap = {
        ord('\t'): ' ',
        ord('\f'): ' ',
        ord('\r'): None
        }
a = s.translate(remap)

'''
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD',a)
b.translate(cmb_chrs)
'''

'''
digitmap = { c: ord('0') + unicodedata.digit(chr(c))
             for c in range(sys.maxunicode)
             if unicodedata.category(chr(c)) == 'Nd' }
'''

'''
b = unicodedata.normalize('NFD',a)
b.encode('ascii','ignore').decode('ascii')
'''





# 2.13 Aligning text strings
'''
You need to format text with some sort of alignment applied.
'''

'''.ljust(),.rjust(),.center()'''
text = 'Hello World'
text.ljust(20)
text.rjust(20)
text.center(20)

text.rjust(20,'*')


'''format(): work with any value, besides string'''
format(text,'>20')
format(text,'<20')
format(text,'^20')

format(text,'=>20s')
format(text,'*^20s')

'{:>10s} {:>10s}'.format('Hello', 'World')




# 2.14 Combining and concatenating strings
'''
You want to combine many small strings together into a larger string.
'''

''' join(): join sequence (list,tuple,dict,...) to string '''
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)

''' + operator '''





# 2.15 Interpolating variables in strings
'''
You want to create a string in which embedded variable names are substituted 
with a string representation of a variable’s value.
'''

''' format() method '''
'{name} has {n} messages.'.format(name='Wang',n=5)


name,n = 'Wang',5
'{name} has {n} messages.'.format_map(vars())


class Info(object):
    def __init__(self,name,n):
        self.name = name
        self.n = n
a = Info('Wang',5)
'{name} has {n} messages.'.format_map(vars(a))


class subsafe(dict):   # inheritance dict class
    def __missing__(self,key):
        return '{'+key+'}'
del n
'{name} has {n} messages.'.format_map(subsafe(vars()))

''' Hide sub behind a small utility function
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
print(sub('Hello {name}'))
'''

'''
name,n = 'Wang',5
'%(name) has %(n) messages.'% vars()
'''

'''
import string
s = string.Tempelate('$name has $n messages.')
s.substituted(vars())
'''





# 2.16 Reformatting text to a fix number of columns
'''
You have long strings that you want to reformat so that they fill a user-specified 
number of columns.
'''

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \ the eyes, not around the eyes, don't look around the eyes, \ look into my eyes, you're under."

import textwrap

textwrap.fill(s,70)
textwrap.fill(s,40)
textwrap.fill(s,40,initial_indent='    ')
textwrap.fill(s,40,subsequent_indent='  ')

'''terminal size
import os
os.get_terminal_size().columns  # OSErrer: Operation not supported by device
'''




# 2.17 Handling HTML and XML entities in text
'''
You want to replace HTML or XML entities such as &entity; or &#code; with their corresponding 
text. Alternatively, you need to produce text, but escape certain charac‐ ters (e.g., <, >, or &).
'''

s = 'Elements are written as "<tag>text</tag>".'
import html
html.escape(s)
html.escape(s,quote=False)

s = 'Spicy Jalapeño'
s.encode('ascii', errors='xmlcharrefreplace')

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
p.unescape(s)

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape 
unescape(t)





# 2.18 Tokenizing text
'''
You have a string that you want to parse left to right into a stream of tokens.
'''

text = 'foo = 23 + 42 * 10'

tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
              ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

# define all of the possible tokens
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)' 
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
'''
?P<TAGNAME> is used to assign a name to the pattern.
'''
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# Create a scanner object, which repeated calls .match.
scanner = master_pat.scanner('foo = 42')
m = scanner.match()
mlastgroup,m.group()
m = scanner.match()
m.lastgroup,m.group()


from collections import namedtuple
Token = namedtuple('Token',['type','value'])

def generate_tokens(pat,text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match,None):
        yield Token(m.lastgroup,m.group())
        
for tok in generate_tokens(master_pat,'foo = 42'):
    print(tok)
    
    
    
    
# 2.19 Writing a simple recursive decent parser
'''
You need to parse text according to a set of grammar rules and perform actions or build an 
abstract syntax tree representing the input. The grammar is small, so you’d prefer to just 
write the parser yourself as opposed to using some kind of framework.
'''

import re
import collections

# Token specification
NUM    = r'(?P<NUM>\d+)'
PLUS   = r'(?P<PLUS>\+)'
MINUS  = r'(?P<MINUS>-)'
TIMES  = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS     = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NUM,PLUS,MINUS,TIME,DIVIDE,RPAREN,LPAREN,WS]))

# Tokenizer
Token = collections.namedtuple('Token',['type','value'])

def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match,None):
        tok = Token(m.lastgroup,m.group())
        if tok.type != 'WS':
            yield tok
            
# Parser
class ExpressionEvaluator(object):
    '''
    Implementation of a recursive descent parser.
    implements a single grammar rule.  Use the ._accept() method
    to test and accept the current lookahead token.  Use the ._expect()
    method to exactly match and discard the next token on on the input
    (or raise a SyntaxError if it doesn't match).
    '''
    def parse(self,text):
        self.tokens = generate_tokens(text)
        self.tok = None        # last symbol
        self.nexttok = None    # next symbol
        self._advance()
        return self.expr()
    
    def _advance(self):
        ''' Advance one token ahead '''
        self.tok,self.nexttok = self.nexttok,next(self.tokens,None)
        
    def _accept(self,toktype):
        '''Test and consume the next token if it matches toktype'''
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False
        
    def _except(self,toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected'+ toktype)
            
    # Grammar rules follow
    def expr(self):
        ''' expression ::= term { ('+'|'-') term }* '''
        
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval
        
        
    def term(self):
        ''' term ::= factor { ('*'|'/') factor }* '''
        
        termval = self.factor()
        while self._accept('TIME') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIME':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval
        
        
    def factor(self):
        ''' factor ::= NUM | ( expr ) '''
        
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            factval = self.expr
            self._accept('RPAREN')
            return factval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')
            
            
e = ExpressionEvaluator()
e.parse('2')
e.parse('2 + 3')





# 2.20 Performing text operations on byte strings
'''
You want to perform common text operations (e.g., stripping, searching, and replace‐ ment) 
on byte strings.
'''

a = b'Hello, world!'     # a byte string
a.decode('ascii')        # decode into a string

'{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')


