import pandas as pd
from bs4 import BeautifulSoup
import requests


url = "https://www.jamieoliver.com/recipes/category/course/mains/"
url2 = "https://www.allrecipes/recipes/"

page = requests.get(url)

recipe_url_df = pd.DataFrame()

soup = BeautifulSoup(page.text, "html.parser")

recipe_urls = pd.Series([a.get("href") for a in soup.find_all("a")])

recipe_urls = recipe_urls[(recipe_urls.str.count("-")>0) 
                         & (recipe_urls.str.contains("/recipes/")==True)
                         & (recipe_urls.str.contains("-recipes/")==True)
                         & (recipe_urls.str.contains("course")==False)
                         & (recipe_urls.str.contains("books")==False)
                         & (recipe_urls.str.endswith("recipes/")==False)
                         ].unique()


df = pd.DataFrame({"recipe_urls":recipe_urls})
df['recipe_urls'] = "https://www.jamieoliver.com" + df['recipe_urls'].astype('str')

recipe_url_df = pd.concat([recipe_url_df, df]).copy()


recipe_url_df.to_csv("input/recipe_urls.csv", sep="\t", index=False)




