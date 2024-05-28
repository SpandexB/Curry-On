# Curry On - Recipe Recommendation System

## Overview

**Curry On** is a machine learning project that recommends the top 3 recipes based on the ingredients provided by the user. The project involves web scraping, data cleaning, text vectorization using TF-IDF, similarity computation, and a web interface to interact with the recommendation system.

## Features

- **Ingredient-based Recipe Recommendations**: Enter ingredients and get the top 3 recipe suggestions.
- **Web Scraping**: Scraped recipes from a website using BeautifulSoup.
- **Data Processing**: Cleaned and parsed the scraped data.
- **TF-IDF Vectorization**: Vectorized the recipes for similarity calculations.
- **Similarity Function**: Calculated recipe similarities to generate recommendations.
- **API Creation**: Built an API using Flask to serve the recommendations.
- **Web Interface**: Created a website using HTML, CSS, and integrated the API using JavaScript.

## Project Structure

curry-on/
│
├── api/
│ ├── app.py # Flask API
│ ├── model.py # ML model and similarity functions
│ └── requirements.txt # Dependencies
│
├── data/
│ ├── recipes.csv # Cleaned and parsed recipes dataset
│ └── scrape.py # Web scraping script
│
├── web/
│ ├── index.html # Website HTML
│ ├── styles.css # Website CSS
│ └── app.js # JavaScript to integrate API
│
├── README.md # Project README file
└── .gitignore # Git ignore file


## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/curry-on.git
    cd curry-on
    ```

2. **Set up the Python environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r api/requirements.txt
    ```

4. **Run the API**:
    ```bash
    cd api
    python app.py
    ```

5. **Open the website**:
    Open `web/index.html` in your web browser.

## Usage

1. Open the **Curry On** website.
2. Enter the ingredients you have.
3. Click on the "Get Recipes" button.
4. The top 3 recommended recipes will be displayed.

## Technical Details

### Web Scraping
- **Library**: BeautifulSoup
- **Script**: `data/scrape.py`
- **Output**: `data/recipes.csv`

### Data Cleaning and Parsing
- Cleaned and formatted the scraped data to ensure consistency and usability.

### TF-IDF Vectorization
- **Library**: Scikit-learn
- **Method**: TF-IDF vectorization to convert text data into numerical vectors.

### Similarity Calculation
- Computed cosine similarity between the ingredient vector and recipe vectors to find the most similar recipes.

### API
- **Framework**: Flask
- **Endpoints**:
  - `/predict` (POST): Takes ingredients as input and returns the top 3 recipes.

### Web Interface
- **HTML/CSS**: For the basic structure and styling of the website.
- **JavaScript**: To make API calls and dynamically update the webpage with recipe recommendations.

## Dependencies

Update the `api/requirements.txt` with the following libraries:

```plaintext
Flask==x.x.x
beautifulsoup4==x.x.x
scikit-learn==x.x.x
pandas==x.x.x
numpy==x.x.x
requests==x.x.x```


