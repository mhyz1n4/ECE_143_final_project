#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:24:32 2020

@author: yaojunyang
"""

import string
from nltk.corpus import stopwords
import spacy

def process_year_data(all_data):
    '''
    Process data of different year and return the frequency of bigrams
    '''
    assert isinstance(all_data,str)
    for content in all_data:
        assert isinstance(content,str)
    # initialize NLTK and spacy
    bigramCount = defaultdict(int)
    punctuation = set(string.punctuation)
    stop_words = set(stopwords.words('english'))
    translator = str.maketrans('', '', string.punctuation)
    nlp = spacy.load("en_core_web_sm")

    # process the dataframe
    review_text = []
    for idx, d in enumerate(all_data['reviewText']):
        if idx % 1000 == 0:
            print(idx)
        r = d.translate(translator).lower()
        doc = nlp(r)
        r = [word.text for word in doc if word.text not in stop_words and not word.text.isdigit() and
             word.pos_ in ("NOUN", "ADJ")]
        if r:
            prev = r[0]
            for i in range(1, len(r)):
                bigram = prev + " " + r[i]
                bigramCount[bigram] += 1
                prev = r[i]
    return bigramCount