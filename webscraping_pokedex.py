# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:49:14 2019

@author: Brandon
"""
import os
import urllib
from bs4 import BeautifulSoup as bs
import re
os.chdir("C:\\Users\\Brand\\OneDrive\\文档\\GitHub\\Pokemon-Simulator-in-Python")
import pandas as pd


pokedex=open("pokedex.txt","r")
#url="https://pokemondb.net/pokedex/game/sword-shield"
#pokedex=urllib.request.urlopen(url).read()
soup=bs(pokedex,'lxml')

#print(soup.prettify())

info_cards=soup.find_all('span', {"class":"infocard-lg-data text-muted"})
pokemon_dict={}
for index,card in enumerate(info_cards):
    text=card.text
    text=text[0:len(text)//2].split(" ")
    pokeid=index+1
    pokename=text[1]
    poke_type1=text[2]
    try:
        poke_type2=text[4]
    except:
        poke_type2=None
    pokemon_dict[pokeid]={"id":pokeid,"name":pokename,"type1":poke_type1,"type2":poke_type2}
    
    
url="https://www.serebii.net/swordshield/galarpokedex.shtml"
pokemon_page=urllib.request.urlopen(url).read()
pokemon_soup=bs(pokemon_page,'lxml')

stats=pokemon_soup.findAll("td",{"align":"center","class":"fooinfo"})

stats_list=[]
for num in stats:
    stats_list.append(num.get_text("|",strip=True))

i=0
for index in pokemon_dict.keys():
    pokemon_dict[index]["hp"]=stats_list[11*i+5]
    pokemon_dict[index]["attack"]=stats_list[11*i+6]
    pokemon_dict[index]["defense"]=stats_list[11*i+7]
    pokemon_dict[index]["spatk"]=stats_list[11*i+8]
    pokemon_dict[index]["spdef"]=stats_list[11*i+9]
    pokemon_dict[index]["speed"]=stats_list[11*i+10]
    ability=stats_list[11*i+3].split('|')
    pokemon_dict[index]["ability1"]=ability[0]
    try:
        pokemon_dict[index]["ability2"]=ability[1]
    except:
        pokemon_dict[index]["ability2"]=None
    
    try:
        pokemon_dict[index]["hiden_ability"]=ability[2]
    except:
        pokemon_dict[index]["hiden_ability"]=None
    i=i+1
    

poke_df=pd.DataFrame.from_dict(pokemon_dict,orient="index")
poke_df.to_csv("C:\\Users\\Brand\\OneDrive\\文档\\GitHub\\Pokemon-Simulator-in-Python\\galar_pokedex.csv",index=False)





    
    
    
    