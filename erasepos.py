from bs4 import BeautifulSoup
import requests
import random
import re
import fbconsole as F
import json
import string


def erasePOS(word,POS):
  with open('dictionary.json', 'r') as f:
    dictionary = json.load(f)  
  #find words part of speech (exampe is ViN)
  dictionary_POS = dictionary[word]
  #determines whether the POS provided matches the current POS
  if re.search(POS,dictionary_POS) != None:
    key = dictionary_POS.translate(None,POS)
    dictionary[word] = key
    with open('dictionary.json', 'w') as f:
      json.dump(dictionary, f)
    with open('facebook_dictionary.json', 'r') as f:
      fb_dictionary = json.load(f) 
    
    if word in fb_dictionary[POS]:
      old_array = fb_dictionary[POS]
      fb_dictionary[POS] = []
      for old_word in old_array:
        if word != old_word:
          fb_dictionary[POS].append(old_word)

    with open('facebook_dictionary.json', 'w') as f:
      json.dump(fb_dictionary, f)
  print word + ' is no longer a ' + POS


word = raw_input("What's the word?")
POS = raw_input("What's the part of speech?")
erasePOS(word, POS)






# if __name__ == '__main__':
#   main()