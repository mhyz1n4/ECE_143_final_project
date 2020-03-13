# ECE_143_final_project
An repository for amazon review dataset analysis

## Dataset
We are using the amazon review dataset provided by CSE course. The dataset can be downloaded by following this link: https://cseweb.ucsd.edu/~jmcauley/datasets.html. For this project, we only analysed Software, Electronics, Prime Pantry and Sports & Outdoors categories. 

## File Structure
```baseline.py``` this file contains all the functions needed for analysing the dataset.

```Visualizations.ipynb``` this jupyter file contains how to use the function in ```baseline.py``` and visualization of the data analysis, which is in the presentation.

```software``` this folder is an example of our project.

## Usage
The use of '''baseline.py''' is visualized in the Jupyter notebooks file '''Visualizations.ipynb'''. The baseline module is first loaded and unpacked. The 'stopwords' corpus is downloaded from the natural language toolkit (nltk). Amazon data is loaded in as a .json file and stored in a list. Using the 'only_adj_and_noun' function, reviews are removed if there is no rating or review text, reviews are reduced to only adjectives and nouns, and a list of unigrams, bigrams, and resulting review text is returned. 'bigram_to_feature' sorts bigrams by frequency and returns the 1000 most frequent bigrams in reviews. 

## Third Party Modules
json

numpy

collections (defaultdict, Counter)

string

sklearn (linear_model)

sys

nltk

random

nltk.corpus (stopwords)

matplotlib

pandas

spacy
