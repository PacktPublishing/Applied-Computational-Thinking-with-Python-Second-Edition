import requests 
import time 
from bs4 import BeautifulSoup 
import logging 

# Define the URL to Scrape 
url = 'http://quotes.toscrape.com' 

#  Make an HTTP Request
response = requests.get(url) 

# Parse the HTML Content
soup = BeautifulSoup(response.content, 'html.parser') 

# Locate Quote Containers
quote_containers = soup.find_all('div', class_='quote') 

# Loop Through Containers and Extract Data 
for quote_container in quote_containers: 
    quote = quote_container.find('span', class_='text').text 
    author = quote_container.find('small', class_='author').text 
    print(f"{quote} — {author}") 
