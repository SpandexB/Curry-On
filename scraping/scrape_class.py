import numpy as np
from bs4 import BeautifulSoup
import pandas as pd
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

class extract():


    def __init__(self,url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(url,headers = headers).content, 'html.parser')



    def recipe_name(self):
        try:
            return self.soup.find('h1').text.strip()
        except: 
            return np.nan
        


    def serves(self):
        try:
            return self.soup.find('div', {'class': 'recipe-detail serves'}).text.split(' ',1)[1]
        except:
            return np.nan 
        


    def cooking_time(self):
        try:
            return self.soup.find('div', {'class': 'recipe-detail time'}).text.split('In')[1]
        except:
            return np.nan    



    def difficulty(self):
        try:
            return self.soup.find('div', {'class': 'col-md-12 recipe-details-col remove-left-col-padding-md'}).text.split('Difficulty')[1]
        except:
            return np.nan



    def ingredients(self):
        try:
            ingredients = []
            for li in self.soup.select('.ingred-list li'):
                ingred = ' '.join(li.text.split())
                ingredients.append(ingred)
            return ingredients
        except:
            return np.nan
        



