import requests
import datetime

# API key
api_key = 'YOUR_API_KEY'

# Define the endpoint
url = 'https://newsapi.org/v2/everything'

parameters = {
    'q': 'technology', # query phrase
    'pageSize': 10,  # maximum is 100
    'apiKey': api_key, # your own API key
    'from': str(datetime.date.today() - datetime.timedelta(days=7)), # Getting news from the last week
    'to': str(datetime.date.today()),
    'language': 'en', # English language
 }

# Make the HTTP GET request to News API
response = requests.get(url, params=parameters)

# Convert the response to JSON format and pretty print it
response_json = response.json()

# Check if the request was successful
if response.status_code == 200:
    for article in response_json['articles']:
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print('-' * 80)
else:
    print("Error occured in fetching the news.")
    