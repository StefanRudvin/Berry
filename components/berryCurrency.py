import requests

url = "http://api.fixer.io/latest?symbols=GBP,EUR"

def getCurrencyString():
    return "The euro to pound currency rate is {}.".format(parseCurrency())

def parseCurrency():
    data = getRequestJSON(url)
    gbpRate = round(data['rates']['GBP'], 3)
    return (1-gbpRate) + 1;


def getRequestJSON(url):
    response  = requests.get(url)
    return response.json()
