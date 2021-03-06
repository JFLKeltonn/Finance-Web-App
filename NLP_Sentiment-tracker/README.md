# Sentiment Tracker

## Description
Develop a Sentiment Tracking Algorithm that tracks the sentiment of the market from the previous day and attribute a score from 0 to 100, with 0 being "Defeated" and 100 being "Euphoria". Likely no value towards actual investing, but can be helpful in timing entry positions.

## Methodology
### Packages and Dependencies
For general use:
1. Pandas
2. Scipy
3. Numpy

Charting and Visualisations:
1. Seaborn
2. Matplotlib

Machine Learning and Text Analysis:
1. sklearn
2. spacy
3. Tensorflow/Keras [If we planning to use Neural Networks]

Processing and Serialising Models for storage
1. Pickle [sklearn]
2. JobLib [sklearn]
3. Keras has a method to convert to json

Scraping:
1. Twint/Tweepy
2. bs4
3. selenium

### Scraping of unstructured text data
#### Data Sources:
- Twitter
- MarketWatch??
- Yahoo Finance??

#### Data Storage
Probably going to store the text in a csv file, before importing into dataframe via pandas for tokenisation and model selection.

### Model Selection and Determining Sentiment Score

#### Step 1: Classify tweets based on sentiment
TEMPORARY IMPLEMENTATION USING SUPERVISED CLASSIFICATION
Develop a classifier using traditional models (logistic classifier, decision trees) using mannually labelling for Supervised Machine Learning.

FINAL IMPLEMENTATION GOAL
Use RNN to create a more accurate classifier model for tweet sentiments.

#### Step 2: Collect Classifier Statistics for trailing 100 days
[To be filled...]

