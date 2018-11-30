#!/bin/python3
from bs4 import BeautifulSoup
import requests

# Download Page
r = requests.get('http://www2.cych.org.tw/WebToNewRegister/webSerchDrSch.aspx?No=020')

# Check if success
if r.status_code == requests.codes.ok:
  # Parse
  soup = BeautifulSoup(r.text, 'html.parser')

  # fetch schedule with classname
  tds = soup.select('table.boder2 > tr > td')
  for td in tds:
    print(td.prettify())