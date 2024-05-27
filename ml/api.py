from flask import Flask, jsonify, request
from flask_cors import CORS

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ingredient_parser import ingredient_parser
import recommendation_system

app = Flask(__name__)
CORS(app)
@app.route('/', methods=["GET"])
def hello():
 return HELLO_HTML

HELLO_HTML = """
     <html><body>
         <h1>✨ Welcome to my api: Curry-On! ✨ </h1>
         <h2> &nbsp &nbsp &nbsp &nbsp  ai based recipe recommendation system👨‍🍳 - your ingredients our recipe 🍔 🥗 🍗 🍜 🥤</h2>
         <p> &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp Please add some ingredients to the url to receive top 3 recipe recommendations.
            You can do this by adding "/recipe?ingredients= Pasta Tomato ....." to the current url.
         <p>
     </body></html>
     """

@app.route('/recipe', methods=["GET"])
def recommend_recipe():
 ingredients = request.args.get('ingredients')
 recipe = recommendation_system.RecSys(ingredients)
    

 response = {}
 count = 0    
 for index, row in recipe.iterrows():
        response[count] = {
                            'recipe': str(row['recipe']),
                            'score': str(row['score']),
                            'ingredients': str(row['ingredients']),
                            'url': str(row['url'])
                          }
        count += 1
 return jsonify(response)
if __name__ == "__main__":
   app.run(host="0.0.0.0",port=5001 ,debug=True)

