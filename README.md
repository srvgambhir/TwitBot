# TwitBot

This is a web scraping twitter bot. It scrapes top headlines from Science News (https://www.sciencenews.org/) and ScienceDaily (https://www.sciencedaily.com/) related to space and astronomy. It then periodically tweets these headlines out with the accompanying link.

The bot uses the Beautiful Soup library for scraping these websites, and the Twitter API to connect to the platform and post the tweets.

The bot also implements a system to prevent duplicate tweets. By converting the story titles into an accompanying hash key, these keys are stored in an excel sheet and checked against before each post. Working with excel is done using the Openpyxl library.

The headlines are tweeted in a revolving fashion via python generator functions.

The following links were used as resources;
https://pythonprogramming.org/how-to-create-a-webscraping-twitter-bot-in-python/
https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-and-post-content-to-twitter-with-python-3
https://python.plainenglish.io/building-a-news-scraping-twitter-bot-in-python-28eabe17823e

https://www.knowledgehut.com/blog/programming/how-to-work-with-excel-using-python
https://medium.com/aubergine-solutions/working-with-excel-sheets-in-python-using-openpyxl-4f9fd32de87f

https://www.geeksforgeeks.org/md5-hash-python/

https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39
