# TwitBot

This is a web scraping twitter bot. It scrapes top headlines from Science News (https://www.sciencenews.org/) and ScienceDaily (https://www.sciencedaily.com/) related to space and astronomy. It then periodically tweets these headlines out with the accompanying link.

The bot uses the Beautiful Soup library for scraping these websites, and the Twitter API to connect to the platform and post the tweets.

The bot also implements a system to prevent duplicate tweets. By converting the story titles into an accompanying hash key, these keys are stored in an excel sheet and checked against before each post. Working with excel is done using the Openpyxl library.

The headlines are tweeted in a revolving fashion via python generator functions.

The bot is deployed to a Heroku server, however due to fees and the duplicate tweet checker not running on the web server, the bot currently has to be run locally.

Regardless, the server and clock files all function as expected.

Here is the link to the bot's twitter page: https://twitter.com/TwitBot_Sci

Note that currently the bot is ran locally at regular, albeit random intervals.



The following links were used as resources:

https://pythonprogramming.org/how-to-create-a-webscraping-twitter-bot-in-python/

https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-and-post-content-to-twitter-with-python-3

https://python.plainenglish.io/building-a-news-scraping-twitter-bot-in-python-28eabe17823e

https://www.knowledgehut.com/blog/programming/how-to-work-with-excel-using-python

https://medium.com/aubergine-solutions/working-with-excel-sheets-in-python-using-openpyxl-4f9fd32de87f

https://www.geeksforgeeks.org/md5-hash-python/

https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39

https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app

https://devcenter.heroku.com/articles/clock-processes-python

https://stackoverflow.com/questions/71712258/error-could-not-build-wheels-for-backports-zoneinfo-which-is-required-to-insta

https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html

https://stackoverflow.com/questions/13866926/is-there-a-list-of-pytz-timezones
