#! /usr/bin/Python

from bs4 import BeautifulSoup
import requests
import mechanize
from mechanize import Browser
import urllib2
import HTMLParser
import re
import HTMLParser
re.DOTALL
import os
import json

def mapPOS(facebookword):
  facebook_map = {}
  facebookword = facebookword.lower()
  word = facebookword.translate(None, '",!.?!@#$%^&*()_-:')
  if word in dictionary:
    return dictionary[word]
def dictionary():
  with open('dictionary.json', 'r') as f:
    dictionary = json.load(f) 
  return dictionary
dictionary = dictionary()

# def run():
br = Browser()
br.set_handle_robots( False )
url = 'https://www.facebook.com/login/'
html = urllib2.urlopen(url)


br.open(url)


br.form = list(br.forms())[0]
br.form['email'] = 'emilylimabean@gmail.com'
br.form['pass'] = 'ItsaSunnyDay62'
req = br.submit()

html = req.read()
	
f = open('facebooktext.txt', 'w')
f.write(html)
f.close()


matches = re.findall(r"<p>([a-zA-Z0-9 !-)(?.,;:'\"_+= -]*)", open('facebooktext.txt', 'r').read())
os.remove('C:\Python27\mockingbird\\facebooktext.txt')

with open('facebook_dictionary.json', 'r') as fb:
  fb_dictionary = json.load(fb)

unknown = open('unknown_facebook_words', 'a')
f = open('facebookwords.txt', 'a')
for match in matches:
  stripped_text = HTMLParser.HTMLParser().unescape(match)
  if stripped_text != '':
    f.write(stripped_text + ' xYx ')
    words = stripped_text.split()
    for word in words:
      word = str(word).lower().translate(None, '",!.?!@#$%^&*()_-:<>')
      POS = mapPOS(word)
      if POS:
        for char in list(POS):
          if char in fb_dictionary.keys():
            fb_dictionary[char].append(word)
          else:
            fb_dictionary[char] = []
      else:
        unknown.write(word + ', ')

with open('facebook_dictionary.json', 'w') as fb:
  json.dump(fb_dictionary, fb)