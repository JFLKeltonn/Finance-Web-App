import pandas as pd
import twint
from datetime import date
from datetime import timedelta
from os.path import exists
from string import punctuation

def scrape():
    queries = ["$SPY", "$QQQ", "Economy", "Inflation", "Federal Reserve", "$XLF", "$XLE","$XLK", "$XLY", "$XLU", "$XLRE", "$XLM", "$XLP","$XLI", "Unemployment"]
    stop = date.today()
    start = stop - timedelta(days = 1)
    my_df = pd.DataFrame()

    for q in queries:
        c = twint.Config()
        c.Pandas = True
        c.Search = q
        c.Lang = "en"
        c.Limit = 10
        c.Since = start.strftime("%Y-%m-%d")
        c.Until = stop.strftime("%Y-%m-%d")
        c.Geo = "40.654578, -98.700148, 2500km"
        twint.run.Search(c)
        Tweets_df = twint.storage.panda.Tweets_df
        my_df = my_df.append(Tweets_df)
    return my_df

def notLink(myString):
    if len(myString) <5:
        return True
    elif myString[:4] != "http":
        return True
    else:
        return False

def cleanText(myString):
    vektor = myString.split()
    lastValue = ""
    for word in vektor:
        cleanWord = ""
        checkValue = True
        for letter in word:
            if letter == '@':
                checkValue = False
            if letter.isalpha() or letter in punctuation or letter.isdigit():
                cleanWord += letter
        if checkValue and notLink(cleanWord):
            lastValue += cleanWord + " "
    return lastValue

def parseData(rawData):
    df = rawData[["nlikes","nretweets","tweet"]]
    df["Cleaned"] = df["tweet"].apply(cleanText)
    df["Weight"] = df["nlikes"] + df["nretweets"]
    del df['nlikes']
    del df['nretweets']
    return df
