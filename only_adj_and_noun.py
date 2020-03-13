#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:53:13 2020

@author: yaojunyang
"""


import string
from nltk.corpus import stopwords
import spacy

def only_adj_and_noun(all_data):
    '''
    extract adjective and noun from review text in the data and 
    return uniCount and bigramCount as dictionary of the count of unigrams and
    bigrams with corresponding unigrams and bigrams.
    input:all_data,type:list,all data in data file
    '''
    assert isinstance(all_data,list)
    for content in all_data:
        assert isinstance(content,str)
    # remove data that has missing features
    for i in all_data:
        if 'reviewText' not in i.keys() or 'overall' not in i.keys() or not i['reviewText'] or not i['overall']:
            all_data.remove(i)
#    # obtain a subset of data to reduce computation time
#    all_data = random.choices(all_data, k=60000)

    # set up NLTK and spacy
    bigramCount = defaultdict(int)
    uniCount = defaultdict(int)
    punctuation = set(string.punctuation)
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    nlp = spacy.load("en_core_web_sm")

    # get bigrams and unigrams & get nouns and adjectives from review text
    review_text = []
    for idx, d in enumerate(all_data):
        if idx % 1000 == 0:
            print(idx)
        r = d['reviewText'].translate(translator).lower()
        doc = nlp(r)
        r = [word.text for word in doc if word.text not in stop_words and not word.text.isdigit() and
             word.pos_ in ("NOUN", "ADJ")]
        review_text.append(" ".join(r))
        if r:
            prev = r[0]
            for i in range(1, len(r)):
                bigram = prev + " " + r[i]
                uniCount[r[i]] += 1
                bigramCount[bigram] += 1
                prev = r[i]
            uniCount[r[0]] += 1
    return uniCount, bigramCount, review_text