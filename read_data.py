#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:52:32 2020

@author: yaojunyang
"""

import json
import os

def read_data(f_name):
    '''
    read all data from source files and return them as a list.
    '''
    assert isinstance(f_name,str)
    all_data = []
    assert os.path.exists(f_name)
    print(f_name)
    with open(f_name, 'r') as f:
        line = f.readline()
        #print(line)
        while line:
            data = json.loads(line)
            all_data.append(data)
            line = f.readline()
    return all_data