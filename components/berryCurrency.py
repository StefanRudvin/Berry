import requests, json

currencies = ['GBP', 'EURO']

url = "http://api.fixer.io/latest?symbols={},{}".format(currencies[0], currencies[1])

def getString():
    return "The {} to {} currency rate is {}.".format(currencies[0], currencies[1], parseCurrency())

def parseCurrency():
    data = getRequestJSON(url)
    gbpRate = round(data['rates'][currencies[0]], 3)
    return (1-gbpRate) + 1;


def getRequestJSON(url):
    response  = requests.get(url)
    return response.json()
