# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:14:03 2017

@author: mskara
"""
original =
        {
         'id' : 100000,
         'type' : 'method',
         'name' : 'test_function',
         'folder': 'XX',
         'len_text': 400,
         'last_update': datetime.datetime(2017, 4, 24, 11, 15, 57, 104056),
         'last_user' : 'scaravex',
         'file_reference': 'YY.py',
         'last_modification': datetime.datetime(2017, 4, 24, 11, 15, 57, 104056),
         }

updated =
        {
          'id' : 100000,
          'language': 'english',
          'errors' : 5,
          'structure' : 0.8,
          'relative_errors' : 0.04,
          'days_last_review' : 100.33,
          'complete_description' : 0,
          'core_file' : 0,
          'FileModificationVsReadme' : 0,
          }


def get_score(updated):
    '''
    function which determines a score for each method
    '''
    score = 100
    if (errors>0):
        score-=1
    if relative_errors>=threshold:
        score-=1
    if days_last_review>=100:
        score-=1

    return score
    
