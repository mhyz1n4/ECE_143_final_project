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

def only_adj_and_noun(all_data):
    # remove data that has missing features
    for i in all_data:
        if 'reviewText' not in i.keys() or 'overall' not in i.keys() or not i['reviewText'] or not i['overall']:
            all_data.remove(i)
    # obtain a subset of data to reduce computation time
    all_data = random.choices(all_data, k=60000)

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

def bigram_to_feature(text, bi_count):
    #get (numbers of bigram, bigram) pairs
    countsBigram = [(bi_count[d], d) for d in bi_count.keys()]
    countsBigram.sort()
    countsBigram.reverse()

    #get the most frequent 1000 bigrams
    bigrams = [c[1] for c in countsBigram[:1000]]
    bigramId = dict(zip(bigrams, range(len(bigrams))))

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

def data_by_rating(all_data, rating):
    # get data that has certain rating
    ratings_data = []
    for d in all_data:
        if d['overall'] == rating:
            ratings_data.append(d)
    return ratings_data

def data_by_year(all_data):
    # create dataframe that contains ["reviewTime",'overall', 'reviewText'] columns
    tmp = pd.DataFrame(all_data)
    tmp["reviewTime"] = tmp["reviewTime"].str[-4:]
    a = pd.to_datetime(tmp["reviewTime"])
    tmp["reviewTime"] = a.dt.strftime('%Y')
    year_data = tmp[["reviewTime",'overall', 'reviewText']]
    return year_data

def process_year_data(all_data):
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
