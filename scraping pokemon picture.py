# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:40:10 2020

@author: qwerdf
"""


import os
import urllib
from bs4 import BeautifulSoup as bs
import re
os.chdir(r"C:\Users\qwerdf\Documents\GitHub\Pokemon-Simulator-in-Python")
import pandas as pd
import requests
from PIL import Image
import urllib.request

pokemon=pd.read_csv("pokemon_data_clean.csv")

result=[]

for Name in pokemon["Name"]:
    try:
        name=Name.lower()
        url=r"https://www.serebii.net/pokemon/{}".format(name)
        pokemon_page=urllib.request.urlopen(url).read()
        pokemon_soup=bs(pokemon_page,'lxml')
        pic_address=pokemon_soup.find("img",{"src":re.compile("\/pokemon\/art/.*\.png")})
        pic_url="https://www.serebii.net"+pic_address['src']
        urllib.request.urlretrieve(pic_url,r'Pokemon_picture\{}.png'.format(name))
    except:
        print("not working for {}".format(name))
    

name=Name.lower()
url=r"https://www.serebii.net/pokemon/{}".format(name)
pokemon_page=urllib.request.urlopen(url).read()
pokemon_soup=bs(pokemon_page,'lxml')
pic_address=pokemon_soup.find("img",{"src":re.compile("\/pokemon\/art/.*\.png")})
pic_url="https://www.serebii.net"+pic_address['src']
urllib.request.urlretrieve(pic_url,r'Pokemon_picture\{}.png'.format(name))
        
        

