import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import path

df_recipes = pd.read_csv(path.PARSED_PATH)

df_recipes['ingredients_parsed'] = df_recipes.ingredients_parsed.values.astype('U')

tfidf = TfidfVectorizer()
tfidf.fit(df_recipes['ingredients_parsed'])
tfidf_recipe = tfidf.transform(df_recipes['ingredients_parsed'])

with open(path.TFIDF_MODEL_PATH, "wb") as f:
     pickle.dump(tfidf, f)
with open(path.TFIDF_ENCODING_PATH, "wb") as f:
     pickle.dump(tfidf_recipe, f)


print("TF-IDF transformation completed and model saved successfully.")
