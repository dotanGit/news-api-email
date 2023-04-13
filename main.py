import requests
from send_email import send_email
from langdetect import detect

topic = "tesla"

api_key = 'd9fc059bc7514e188ef8ef919c0f48d3'
url = 'https://newsapi.org/v2/everything?' \
      f'q={topic}&' \
      'from=2023-03-13&' \
      'sortBy=publishedAt&' \
      'apiKey=d9fc059bc7514e188ef8ef919c0f48d3'   # if I add &langauge=en the articles will be in english ,  each line is a parameter and the first one is a code

# Make a request
request = requests.get(url)


# Get a dictionary with data
content = request.json()   # return the content as a dictionary

# Access the articles and descriptions
body = ''
for article in content['articles'][:10]:
    if article['title'] is not None:   # checks that there is a title
        lang = detect(article['title'] + ' ' + article['description'])   # detect function return the langauge in keywords such as 'en' for english
        if lang == 'en':
            body = "Subject: Today's news" + '\n' + \
                   body + article['title'] + '\n'\
                   + article['description'] +\
                   '\n' + article['url'] + 2*'\n'
        else:
            continue

body = body.encode('utf-8')   # this is an email protocol for strings
send_email(body)
