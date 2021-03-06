from bs4 import BeautifulSoup
import requests
import random
import re
import fbconsole as F
import json

def findPOS(word):
  if word in dictionary:
    return dictionary[word]

def mapPOS(facebookword):
  facebook_map = {}
  facebookword = facebookword.lower()
  word = facebookword.translate(None, '",!.?!@#$%^&*()_-:')
  if word in dictionary:
    return dictionary[word]

def talk(talk_word):
  #which words come after other words
  prev = ''
  words_dict = {}
  for word in split_facebook_text:
    word = word.lower()
    word = word.translate(None, '"')
    if word == 'xyx':
      prev = ''
    elif prev not in words_dict:
      words_dict[prev] = [word]
    else:
      words_dict[prev].append(word)
      prev = word

  # print words_dict.get(talk_word)

  for i in range(15):
    next = words_dict.get(talk_word)
    if(next):
      last = talk_word
      talk_word = random.choice(next)
      if last != talk_word:
        print talk_word,

def talk():
  

def grab_words(POS):
  word_array = []
  dict_keys = fb_POS.keys()
  for key in dict_keys:
    if isinstance(key, str):
      if re.findall(POS, key) and isinstance(key, str):
        word_array.append(fb_POS[key])
  return word_array      

def writefile(filename, data):
  f = open(filename,'w')
  f.write(data)

def appendfile(filename, data):
  f = open(filename,'a')
  f.write(data)

def dictionary():
  with open('dictionary.json', 'r') as f:
    dictionary = json.load(f) 
  return dictionary


def main():
  talk('')


with open('facebook_dictionary.json', 'r') as f:
  fb_dictionary = json.load(f)  

dictionary = dictionary()

facebook_text = open('facebookwords.txt', 'r').read()

split_facebook_text = facebook_text.split()
# for word in split_facebook_text:
#   if word != 'xYx':
#     POS = mapPOS(word)
#     if POS:
#       for char in list(POS):
#         if char in fb_dictionary:
#           if word not in fb_dictionary[char]:
#             fb_dictionary[char].append(word)

# with open('facebook_dictionary5.json', 'w') as f:
#   json.dump(fb_dictionary, f)
  
# create dictionary
# raw_dict_text = open('dictionary.txt', 'r').read()
# dict_list = raw_dict_text.split(',')
# count = 1
# index = ''
# dictionary = {}
# for word in dict_list:
#   if count == 1:
#     dictionary[word] = ''
#     index = word
#     count = 2 
#   elif count == 2:
#     dictionary[index] = word
#     count = 1
#     print word
# with open('jsontest.json', 'w') as f:
#   json.dump(dictionary, f)


  

# map facebook words to parts of speech
# prev = ''
# fb_POS = {}
# for word in split_facebook_text:
#   word = word.lower()
#   word = word.translate(None, '"')
#   if word == 'xyx':
#   	prev = ''
#   elif word not in fb_POS:
#     POS = mapPOS(word)
#     if POS != None and POS not in fb_POS.keys():
#       fb_POS[POS] = [word]
#       count = count + 1
#       print word + ' '+ str(count)
#     elif POS != None:
#       fb_POS[POS].append(word)


# with open('facebook_dictionary.json', 'w') as fb:
#   json.dump(fb_POS,fb)   




# with open('facebook_dictionary.json', 'r') as fb:
#   fb_POS = json.load(fb) 


# fb_word_array = ''   
# fb_words = open('facebookwords.txt', 'r').read().split()
# for fb_word in fb_words:
#   if mapPOS(fb_word) == None:
#     fb_word_array = fb_word + ' '
    # appendfile('whatarethesewords.txt', str(fb_word_array))





if __name__ == '__main__':
  main()