from bs4 import BeautifulSoup
import requests

response = requests.get("https://smile.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/141-3718383-0667750")
page_data = response.text
soup = BeautifulSoup(page_data, 'html.parser')

print(soup.prettify())
