#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:38:02 2020

@author: yaojunyang
"""



def data_by_rating(all_data, rating):
    '''
    Create the list of data with specific rating.
    input:all_data,type:list,all data from data file
    input:rating,type:int,the rating that users type
    '''
    assert isinstance(all_data,list)
    for content in all_data:
        assert isinstance(content,str)
    assert isinstance(rating,int)
    # get data that has certain rating
    ratings_data = []
    for d in all_data:
        if d['overall'] == rating:
            ratings_data.append(d)
    return ratings_data