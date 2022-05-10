# Sentiment Tracker

## Description
Develop a Sentiment Tracking Algorithm that tracks the sentiment of the market from the previous day and attribute a score from 0 to 100, with 0 being "Defeated" and 100 being "Euphoria". Likely no value towards actual investing, but can be helpful in timing entry positions.

## Methodology

### Scraping of unstructured text data
#### Data Sources:
- Twitter
- MarketWatch??
- Yahoo Finance??

#### Model Selection and Determining Sentiment Score

Create or import a bag of words of positive and negative words and rate all scraped text data based on their score. Find the total score for the day, and collect the sentiment scores over the past 100+ or so days. Use Machine Learning to approximate the probability distribution of the sentiment scores. With the upper bound as score 100 and the lower bound as score 0, we normalise the probability distribution and fit new data every day to find its sentiment score.
