from bs4 import BeautifulSoup
import requests
import random
import re
import fbconsole as F
import json
import string

def findPOS(word):
  with open('dictionary.json', 'r') as f:
    dictionary = json.load(f)
    if dictionary[word]:   
      return dictionary[word]
    else:
      return 'Not found!'

def findFB(POS, word):
  with open('facebook_dictionary.json', 'r') as f:
    fb_dictionary = json.load(f)
    if word in fb_dictionary[POS]:
      return 'found'

word = raw_input("Enter a word: ")
POS = raw_input("Enter a POS: ")
print 'dictionary: ' + findPOS(word)
# print findFB(POS, word)





# if __name__ == '__main__':
#   main()