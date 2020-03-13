#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:37:41 2020

@author: yaojunyang
"""


def feature(text, bigrams, bigramId):
    '''
    Combine the words in review text as bigram to prepare
    the feature for regression.
    input:text,type:str,review text
    input:bigrams,type:list,list of bigram
    input:bigramId,type:dictionary,dictionary of bigram with ID
    '''
    assert isinstance(text,str)
    assert isinstance(bigrams,list)
    for content in bigrams:
        assert isinstance(content,str)
    assert isinstance(bigramId,dict)
    #create bag of words vector features
    feat = [0]*len(bigrams)
    words = text.split()
    for i in range(len(words)-1):
        bigram = words[i] + " " + words[i+1]
        try:
            feat[bigramId[bigram]] += 1
        except KeyError:
            continue
    feat.append(1) #offset
    return feat