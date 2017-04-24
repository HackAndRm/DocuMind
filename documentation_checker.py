# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 22:42:44 2017

@author: mskara
"""

import numpy as np
import re
import language_check
import nltk  ## Natural language preprocessing
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup, SoupStrainer
from pathfinder import find



def normalise(word):
    ''' Normalises words to lowercase and stems and lemmatizes it. '''
    lemmatizer = nltk.WordNetLemmatizer()
    stemmer = nltk.stem.porter.PorterStemmer()
    word = word.lower()
    # word = stemmer.stem_word(word)
    # word = lemmatizer.lemmatize(word)

    return word

path_file = r'C:\Users\mskara\Documents\GitHub\donna\NLP_notes\README.md'
def open_readme(path_file):
    '''function which opens the documentation'''
    file = open(path_file, encoding='iso-8859-1')
    text = file.read()
    array = [] # it could be helpful to obtain an array of data
    for row in file:
        print (row)
        array.append(row)
        
    return text

    
def _calculate_languages_ratios(text):
    '''
    Calculate probability of a README documentation
    to be written in several languages, return a dict
    @param text: Text whose language want to be detected
    @return: Dictionary with languages and unique stopwords seen in text
    '''
    languages_ratios = {}
    # nltk.wordpunct_tokenize() splits all punctuations into separate tokens
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    # Compute per language included in nltk number of unique stopwords appearing
    for language in stopwords.fileids():
        stops = []
        for item in stopwords.words(language):
            stops.extend(wordpunct_tokenize(item))
            stopwords_set = set(stops)
        # stopwords_set   = set(stopwords.words(language))
        words_set       = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements)  # language "score"

    return languages_ratios


def detect_language(text):
    '''
    Calculate probability of given text to be written in languages and
    return the highest scored. It uses a stopwords based approach.
    @param text: Text whose language want to be detected
    @return: Most scored language guessed
    '''
    ratios = _calculate_languages_ratios(text)
    counter = 0
    for items in ratios:
        if ratios[items] <= 1:
            std_language = 'english'
        else:
            most_rated_language = max(ratios, key=ratios.get)
            counter=1
            break
    if counter == 0:  
        most_rated_language = std_language

    return most_rated_language

def count_errors(text, language = 'en-US'):
    '''
    given a corpora of text and a language, it returns the amount of errors
    '''
    tool = language_check.LanguageTool('en-US')
    matches = tool.check(text)
    
    return len (matches)



def search_methods(path):
    '''
    search for functions or methods inside a folder
    returns a list of names of methods
    '''
    # get all directories and sub-directories in current directory
    paths_dirs = find(".", just_dirs=True)
    # get all .py files using a regex
    paths = find(".", regex=".*\.py$")    
    method_names = []
    for items in paths_py:
        method_names.append(items)

    return method_names


    
def search_similars(word = name_function):
    list_of_words = []
    list_of_words.append(word.lower())
    list_of_words.append(word.lower().replace('_',' '))
    s = re.sub('([A-Z]{1})',r'_\1', word).lower()
    list_of_words.append(s)
    list_of_words.append(s.replace('_',' '))
    new_list=[ii for n,ii in enumerate(list_of_words) if ii not in list_of_words[:n]]
    
    return new_list


# examples name_function
name_function = 'plotTwist'
name_function = 'plot_Twist'


def extract_function_indicators(text, name_function):
    '''function which checks if the method is described
    inside the documentation'''
    names = search_similars(name_function)
    
    for i in range(len(names)):
        keyword = names[i]
        if normalise(text).find(keyword)>1: #obtain consistent text
            description = text.split(keyword)[1]
            method_found = keyword
            break;

    return method_found


for names in function_names:
    extract_function_indicators(text, names)
