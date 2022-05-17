# Package management
# Common Libraries
import numpy as np
import pandas as pd
import math
import time
import random
random.seed(1)
from string import punctuation

# Plotting
import matplotlib.pyplot as plt

# Sklearn Tools
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder
from sklearn import linear_model, model_selection,ensemble

# Sklearn Models
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

data = {} # Insert pandas dataframe here
instance = None # insert text here
label = None #insert classification tags here
vectorisers = [TfidfVectorizer(stop_words = "english"), TfidfVectorizer(), CountVectorizer(stop_words = "english"), CountVectorizer()]
xtrain, xtest, ytrain, ytest = model_selection.train_test_split(instance, label, random_state = 2, train_size = .8)