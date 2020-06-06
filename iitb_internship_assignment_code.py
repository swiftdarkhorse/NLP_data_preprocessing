# -*- coding: utf-8 -*-
"""IITB_Internship_Assignment_Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KdCGrQkKF81mLWEVaX5pF2A812CVP5Bq
"""

from google.colab import drive
drive.mount('/content/drive/')

import lxml
from bs4 import BeautifulSoup as bs
import re
import nltk
import codecs
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords 
from nltk.stem import PorterStemmer 
from nltk.stem import 	WordNetLemmatizer

#Converting XML File into Text String

def read_xml(file_path):
    #file_path = "/content/drive/My Drive/Colab Notebooks/The Blog Authorship Dataset/11253.male.26.Technology.Aquarius.xml"
    content = []
    try:  #If the XML is correctly encoded in UTF-8 Format opening the file as it is
        with open(file_path, "r") as file:        
             content = file.readlines()
             content = "".join(content)
             bs_content = bs(content, "lxml")
             content = re.sub('<[^<]+>', "", content)
        return content

    except:  #If the XML is not correctly encoded in UTF-8 Format opening it by converting it
        with codecs.open(file_path, "r", encoding = "utf-8", errors = "ignore") as file:        
             content = file.readlines()
             content = "".join(content)
             bs_content = bs(content, "lxml")
             content = re.sub('<[^<]+>', "", content)
        return content

#Taking File name as input from User

file_name = input("Enter the XML File name\n")
file_path = "/content/drive/My Drive/Colab Notebooks/The Blog Authorship Dataset/" + str(file_name)
file_content = read_xml(file_path)
seperated_file_content = list(filter(lambda x : x != '', file_content.split('\n\n')))
no_of_paragraphs = len(seperated_file_content)

#Question 1: Tokenization

tokenizer = RegexpTokenizer(r'\w+')
#Word Tokenization
word_tokens = tokenizer.tokenize(file_content)
#Sentence Tokenization
sentence_tokens = sent_tokenize(file_content)
#Displaying Word Tokens and Sentence Tokens
print("The word tokens are:")
print(word_tokens)
print("\n")
print("The sentence tokens are:")
print(sentence_tokens)

# Question 2: Frequency Distribution (per Paragraph)

pairs = []
#Finding Frequency Distribution for each Paragraph in text
for i in range(no_of_paragraphs):
   word_token_para = tokenizer.tokenize(seperated_file_content[i])
   wordfreq = []
   for w in word_token_para:
       wordfreq.append(word_token_para.count(w))
   pairs = pairs + list(zip(word_token_para, wordfreq))
   print("Word-Frequency Pairs for paragraph " + str(i+1) + "\n" + str(list(zip(word_token_para, wordfreq))) + "\n")

# Question 3: Stopwords and Non-Stopwords

#Extracting Stop Words from Word Tokens
stop_words = set(stopwords.words('english')) 
stop_words_list = []
for w in word_tokens: 
    if w in stop_words: 
        stop_words_list.append(w) 
print("The stop word are:")      
print(stop_words_list)
print("\n")
#Extracting Non-Stop Words from Word Tokens
non_stop_words_list = []
for w in word_tokens: 
    if w not in stop_words: 
        non_stop_words_list.append(w)   
print("The non-stop word are:")    
print(non_stop_words_list)

# Question 4: Lexicon Normalization

#Stemming Words in Word Tokens
ps = PorterStemmer() 
stemmed_word_tokens = []
for w in word_tokens:
  stemmed_word_tokens.append(ps.stem(w))
print("The stemmed word tokens are:")
print(stemmed_word_tokens)
print("\n")
#Lemmatizing Words in Word Tokens
wnl = WordNetLemmatizer()
lemmatized_word_tokens = []
for w in word_tokens:
  lemmatized_word_tokens.append(wnl.lemmatize(w))
print("The lemmatized word tokens are:")
print(lemmatized_word_tokens)