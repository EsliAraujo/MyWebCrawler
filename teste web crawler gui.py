# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:29:46 2018

@author: Esli
"""

from bs4 import BeautifulSoup

import requests

url = input("www.guiainvest.com.br/raiox/default.aspx?sigla=abev3")

r  = requests.get("https://" +url)


data = r.text

#soup = BeautifulSoup(data)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

soup.find_all(id="divIndicadores")