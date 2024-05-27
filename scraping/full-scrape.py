import pandas as pd 
import time
import numpy as np
from scrape_class import extract

recipe_df = pd.read_csv("input/recipe_urls.csv")

attribs = ['recipe_name', 'serves', 'cooking_time', 'difficulty', 'ingredients']

data = {attrib: [] for attrib in attribs}
data['recipe_urls'] = []


for i, url in enumerate(recipe_df['recipe_urls']): 
    recipe_scraper = extract(url)
    for attrib in attribs:
        data[attrib].append(getattr(recipe_scraper, attrib)())
    
    data['recipe_urls'].append(url)

    extracted_df = pd.DataFrame(data)

    columns = ['recipe_urls'] + attribs
    extracted_df = extracted_df[columns]

    extracted_df.to_csv(r"input/extracted_recipes.csv", index=False)
    
    if i % 912 != 0:
        print(f'Step {i} completed---------------------------------------------uwu')    
    time.sleep(np.random.randint(1, 5))


