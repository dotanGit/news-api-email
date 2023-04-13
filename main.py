import requests
from send_email import send_email

api_key = 'd9fc059bc7514e188ef8ef919c0f48d3'
url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-03-13&' \
      'sortBy=publishedAt&apiKey=d9fc059bc7514e188ef8ef919c0f48d3'

# Make a request
request = requests.get(url)


# Get a dictionary with data
content = request.json()   # return the content as a dictionary

# Access the articles and descriptions
body = ''
for article in content['articles']:
    if article['title'] is not None:
        body = body + article['title'] + '\n' + article['description'] + 2*'\n'

body = body.encode('utf-8')
send_email(body)
