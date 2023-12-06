#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

url = input("Enter the url of the website: ")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.string
print(f'Title of the webpage: {title}')