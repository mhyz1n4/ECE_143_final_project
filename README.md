# ECE_143_final_project
An repository for amazon review dataset analysis

## Dataset
We are using the amazon review dataset provided by CSE course. The dataset can be downloaded by following this link: https://cseweb.ucsd.edu/~jmcauley/datasets.html. For this project, we only analysed Software, Electronics, Prime Pantry and Sports & Outdoors categories. 

## File Structure
```demonstration/all_function.py``` this file contains all the functions needed for analysing the dataset.

```demonstration/demonstration.ipynb``` this jupyter file contains how to use the function in ```all_function.py``` and visualization of the data analysis we did for the project. Notice that the results are different from PPT because there's some randomness in our method. The jupyter file is only for workflow demonstration purposes. To get the results in our PPT, please refer to the jupyter notebook file in the example folders. 

```software, sports_and_outdoors, electronics``` these folder are examples of our project analysis.

## Usage
The use of '''baseline.py''' is visualized in the Jupyter notebooks file '''Visualizations.ipynb'''. The all_graph_in_presentation folder contains all graphs we use in presentation. 
The baseline module is first loaded and unpacked. The 'stopwords' corpus is downloaded from the natural language toolkit (nltk). Amazon data is loaded in as a .json file and stored in a list. Using the 'only_adj_and_noun' function, reviews are removed if there is no rating or review text, reviews are reduced to only adjectives and nouns, and a list of unigrams, bigrams, and resulting review text is returned. 'bigram_to_feature' sorts bigrams by frequency and returns the 1000 most frequent bigrams in reviews. Next, a bag of words vector is created by looping the 'feature' function over all the data. Next a Ridge regression is run using 'regression'. Next, sort bigrams by their regression coefficient using 'sort_bigrams'. Next we can sort data by rating using 'data_by_rating'. 'only_adj_and_noun' can be reapplied to these sorted data sets and sorted by most common using Counter. These can all be visualized as a user pleases. Data can alternatively be processed by year by inputting 'all_data' (output of 'read_data'), into 'data_by_year'. Data is output into a pandas dataframe and can be split using the .groupby(['reviewtime']) and .get_group("year") methods.
For visualization part, because of the randomness of the regression, the graph in the plot example may different from the graph in the presentation.
![image](https://github.com/mhyz1n4/ECE_143_final_project/blob/master/all_graph_in_presentation/method.png)

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

wordcloud
