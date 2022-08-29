import random
import time

from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
import requests
from twitter import OAuth, Twitter

import tokens

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

oauth = OAuth(
    tokens.ACCESS_TOKEN,
    tokens.ACCESS_SECRET,
    tokens.CONSUMER_KEY,
    tokens.CONSUMER_SECRET
)

t = Twitter(auth=oauth)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

def scrape_sd():
    url = 'https://www.sciencedaily.com/news/space_time'
    response = requests.get(url, headers=HEADERS)
    results = BeautifulSoup(response.text, 'html.parser')

    top = results.find(id="heroes")
    
    headlines = top.find_all('a')

    for headline in headlines:
        title = headline.text.strip()
        link = 'https://www.sciencedaily.com' + headline['href']
        #print(title)
        #print(link)
        yield '"%s" %s' % (title, link)
        

def scrape_sn():
    url = 'https://www.sciencenews.org/topic/space'
    response = requests.get(url, headers=HEADERS)
    results = BeautifulSoup(response.text, 'html.parser')

    articles = results.find_all('article')

    for article in articles:
        headline = article.find('h3').find('a')
        title = headline.text.strip()
        link = headline['href']
        #print(title)
        #print(link)
        yield '"%s" %s' % (title, link)


def main():
    print('Start')
    news_sources = ['scrape_sd', 'scrape_sn']
    news_iterators = []
    for source in news_sources:
        news_iterators.append(globals()[source]())
    while True:
        for i, iterator in enumerate(news_iterators):
            try:
                tweet = next(iterator)
                print(tweet, end='\n\n')
                #time.sleep(10)
            except StopIteration:
                news_iterators[i] = globals()[news_sources[i]]()

main()