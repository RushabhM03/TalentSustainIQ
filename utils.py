import os
from dotenv import load_dotenv
import requests

load_dotenv()

def getnews():
    url = "https://newsapi.org/v2/everything?q=jobs&apiKey={}".format(os.getenv('NEWS_API_KEY'))
    data = requests.get(url)
    data = data.json()
    #print(data)
    return data['articles'], data['totalResults']