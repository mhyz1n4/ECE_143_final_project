#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:37:59 2020

@author: yaojunyang
"""


def bigram_to_feature(bi_count):
    '''
    Use the bi_count dictionary to create the list of bigram
    and dictionary of bigram with bigramID.
    input:bi_count,type:dict,dictionary of number of bigram with corresponding bigram
    '''
    assert isinstance(bi_count,dict)
    #get (numbers of bigram, bigram) pairs
    countsBigram = [(bi_count[d], d) for d in bi_count.keys()]
    countsBigram.sort()
    countsBigram.reverse()

    #get the most frequent 1000 bigrams
    bigrams = [c[1] for c in countsBigram[:1000]]
    bigramId = dict(zip(bigrams, range(len(bigrams))))
    return bigrams,bigramId
