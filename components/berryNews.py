import requests, json, os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import api_keys as api

# From https://newsapi.org

# https://newsapi.org/v1/articles?source=techcrunch&apiKey=db597713532b42f8a87a98487954b034

baseUrl = "https://newsapi.org/v1/articles"

source = "bbc-news"


def getRequestJSON(url):
    response  = requests.get(url)
    return response.json()


def getString():

    url = baseUrl + '?source=' + source + '&apiKey=' + api.newsApiKey

    responseJSON = getRequestJSON(url)

    articles = responseJSON['articles']

    headlines = ""

    for article in articles:
        headlines += article['title']
        headlines += ". "

    message = "Here are the latest titles from BBC News: {} . That is all for the news today. ".format(headlines.encode('ascii', 'ignore').decode('ascii'))

    return message
