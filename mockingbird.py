from bs4 import BeautifulSoup
import requests
import random
import re
import fbconsole as F
import json

def find_word(POS):
  word_pool = []
  with open('facebook_dictionary.json', 'r') as f:
    fb_dictionary = json.load(f)
  keys = fb_dictionary.keys()
  for key in keys:
    if re.search(POS,key) != None:
      words = fb_dictionary[key]
      for word in words:
        word = word.lower()
        word = word.translate(None, '",!.?!@#$%^&*()_-:')
        word_pool.append(word)
  return random.choice(word_pool)





print find_word('D').title(), find_word('N')






# if __name__ == '__main__':
#   main()