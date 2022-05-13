import pandas as pd
from string import punctuation
import twint
from datetime import date
from datetime import timedelta
from os.path import exists
from apscheduler.schedulers.blocking import BlockingScheduler

def scrape():
    queries = ["$SPY", "$QQQ", "Economy", "Inflation", "Federal Reserve", "$XLF", "$XLE","$XLK", "$XLY", "$XLU", "$XLRE", "$XLM", "$XLP","$XLI", "Unemployment"]
    stop = date.today()
    start = stop - timedelta(days = 1)
    myPath = "" #Insert file pathway here
    for q in queries:
        pathway = "{path}/{currDate}".format(path = myPath, currDate = stop.strftime("%Y-%m-%d"))
        c = twint.Config()
        c.Search = q
        c.Lang = "en"
        c.Store_csv = True
        c.Limit = 100
        c.Since = start.strftime("%Y-%m-%d")
        c.Until = stop.strftime("%Y-%m-%d")
        c.Geo = "40.654578, -98.700148, 2500km"
        c.Output = pathway
        twint.run.Search(c)

scrape()
