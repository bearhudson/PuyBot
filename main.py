from bs4 import BeautifulSoup
import requests
import random

url = "https://smile.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/141-3718383-0667750"
headers = {'User-Agent':
               'Mozilla/5.0 (X11; Linux x86_64)'
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/44.0.2403.157 Safari/537.36',
           'Accept-Language': 'en-US, en;q=0.5'
           }

response = requests.session()
request = response.get(url, headers=headers)
page_data = request.text
soup = BeautifulSoup(page_data, 'html.parser')

print(response)
print(soup.prettify())
