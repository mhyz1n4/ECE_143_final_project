#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:47:41 2020

@author: yaojunyang
"""


import numpy as np


def sort_bigrams(theta_bi,bigrams,n):
    '''
    sort the bigram features with the weight of features
    of the regression
    input:theta_bi,type:list,list of weight of features
    input:bigram,type:list,list of bigrams
    input:n,type:int,how many bigram you want by sorted weight
    '''
    assert isinstance(theta_bi,list)
    assert isinstance(bigrams,list)
    assert isinstance(n,int)
    max_index = np.argsort(theta_bi)[-n:][::-1]
    max_index = max_index[1:]
    print(max_index)
    print(len(theta_bi[max_index]))
    #print(np.array(bigrams)[max_index - 1])
    tmp_bigram = np.array(bigrams)[max_index]
    print(tmp_bigram)
    tmp_pair = {bigrams[i]: theta_bi[i] for i in max_index}
    return tmp_pair