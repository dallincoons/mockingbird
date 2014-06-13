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

  # soup = BeautifulSoup(html)
  # divs = soup.findAll('div')
  # txt = ''
  # for div in divs:
  #   txt += str(div)	

f = open('facebooktext.txt', 'w')
f.write(html)


matches = re.findall(r"<p>([a-zA-Z0-9 !-)(?.,;:'\"_+= -]*)", open('facebooktext.txt', 'r').read())


f = open('facebookwords.txt', 'a')
for match in matches:
  stripped_text = HTMLParser.HTMLParser().unescape(match)
  if stripped_text != '':
    f.write(' ' + stripped_text + ' xYx ')



# if __name__ == "__main__":
#     while True:
#         run()
#         time.sleep(60) # 3600 seconds = 1 hour