#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:47:40 2020

@author: yaojunyang
"""

from sklearn import linear_model


def regression(x,y):
    '''
    Ridge regression of rating with the bigram or unigram feature. 
    input:x,type:list,list of bigram or unigram feature
    input:y,type:list,list of rating
    '''
    assert isinstance(x,list)
    assert isinstance(y,list)
    for content in y:
        assert isinstance(content,float)
    reg = 1.0
    clf_bi = linear_model.Ridge(reg, fit_intercept=False)
    clf_bi.fit(x, y)
    theta_bi = clf_bi.coef_
    pred_bi = clf_bi.predict(X_2)
    return theta_bi, pred_bi