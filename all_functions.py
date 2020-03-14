import json
import numpy as np
from collections import defaultdict, Counter
import string
from sklearn import linear_model
import sys
import nltk
import random
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import matplotlib
import os
import pandas as pd
import spacy

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
    all_data = all_data[:60000]
    return all_data

def only_adj_and_noun(all_data):
    '''
    extract all the nouns and adjectives bigrams from review text.
    '''
    
    assert isinstance(all_data, list)
    
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

def feature(text, bigrams, bigramId):
    '''
    get bag of words features from bigrams dictionary
    '''
    
    assert isinstance(text, str)
    assert isinstance(bigrams, list)
    assert isinstance(bigramId, dict)
    
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

def bigram_to_feature(bi_count):
    '''
    turn bigram counts to keys and (bigram, count) pairs
    '''
    
    assert isinstance(bi_count, dict)
    
    #get (numbers of bigram, bigram) pairs
    countsBigram = [(bi_count[d], d) for d in bi_count.keys()]
    countsBigram.sort()
    countsBigram.reverse()

    #get the most frequent 1000 bigrams
    bigrams = [c[1] for c in countsBigram[:1000]]
    bigramId = dict(zip(bigrams, range(len(bigrams))))
    return bigrams,bigramId

#    #create bag of words vector features
#    feat = [0]*len(bigrams)
#    words = text.split()
#    for i in range(len(words)-1):
#        bigram = words[i] + " " + words[i+1]
#        try:
#            feat[bigramId[bigram]] += 1
#        except KeyError:
#            continue
#    feat.append(1) #offset
#    return feat

def data_by_rating(all_data, rating):
    '''
    get data that has certain rating
    '''
    
    assert isinstance(all_data, list)
    assert isinstance(rating, float)
    
    # get data that has certain rating
    ratings_data = []
    for d in all_data:
        if d['overall'] == rating:
            ratings_data.append(d)
    return ratings_data

def data_by_year(all_data):
    '''
    create dataframe that contains ["reviewTime",'overall', 'reviewText'] columns
    '''
    assert isinstance(all_data, list)
    
    tmp = pd.DataFrame(all_data)
    tmp["reviewTime"] = tmp["reviewTime"].str[-4:]
    a = pd.to_datetime(tmp["reviewTime"])
    tmp["reviewTime"] = a.dt.strftime('%Y')
    year_data = tmp[["reviewTime",'overall', 'reviewText']]
    return year_data

def regression(x,y):
    '''
    train reression model
    '''
    
    assert isinstance(x, list)
    assert isinstance(y, list)
    
    reg = 1.0
    clf_bi = linear_model.Ridge(reg, fit_intercept=False)
    clf_bi.fit(x, y)
    theta_bi = clf_bi.coef_
    pred_bi = clf_bi.predict(x)
    return theta_bi, pred_bi

def sort_bigrams(theta_bi,bigrams,n):
    '''
    sort bigrams based on the corresponding theta_bi
    '''
    
    assert isinstance(theta_bi, list)
    assert isinstance(n, int)
    assert isinstance(bigrams, list)
    
    max_index = np.argsort(theta_bi)[-n:][::-1]
    max_index = max_index[1:]
    print(max_index)
    print(len(theta_bi[max_index]))
    #print(np.array(bigrams)[max_index - 1])
    tmp_bigram = np.array(bigrams)[max_index]
    print(tmp_bigram)
    tmp_pair = {bigrams[i]: theta_bi[i] for i in max_index}
    return tmp_pair, max_index

def process_year_data(all_data):
    '''
    all the nouns and adjectives bigrams from dataframe
    '''
    
    assert isinstance(all_data, pd.DataFrame)
    
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
