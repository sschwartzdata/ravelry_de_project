import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

# defining URL and authorization
url = "https://api.ravelry.com/patterns/search.json?craft='crochet’"
API_KEY = os.getenv("API_KEY")
API_USER = os.getenv("API_USER")


response = requests.get(url, auth=(API_USER, API_KEY))
def __resonse_output_(response):
    if response == 'Response [500]':
        return print("outside of OAuth flow, /nthis signals an error on Ravelry's side. We do receive an error notification but please report a bug.")
    else:
        return print("Other error")
print(response)
#crochet_data = response.json()
#print(crochet_data.keys())