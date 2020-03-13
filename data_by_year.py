#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:38:02 2020

@author: yaojunyang
"""

import pandas as pd

def data_by_year(all_data):
    '''
    Create pandas dataframe which contains reviewTime, overall
    rating and reivewText from the all data from source file.
    '''
    assert isinstance(all_data,list)
    for content in all_data:
        assert isinstance(content,str)
    # create dataframe that contains ["reviewTime",'overall', 'reviewText'] columns
    tmp = pd.DataFrame(all_data)
    tmp["reviewTime"] = tmp["reviewTime"].str[-4:]
    a = pd.to_datetime(tmp["reviewTime"])
    tmp["reviewTime"] = a.dt.strftime('%Y')
    year_data = tmp[["reviewTime",'overall', 'reviewText']]
    return year_data