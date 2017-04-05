import requests

def request_get(url):

    x = requests.request('GET', url)

    return(x.json())


