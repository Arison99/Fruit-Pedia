# app.py
from flask import Flask, render_template, request
import requests
from dataclasses import dataclass
from typing import List
import json

app = Flask(__name__, template_folder='custom_templates')

@dataclass
class Fruit:
    name: str
    family: str
    order: str
    genus: str
    nutritions: dict

    @classmethod
    def from_api_data(cls, data):
        return cls(
            name=data.get('name', ''),
            family=data.get('family', ''),
            order=data.get('order', ''),
            genus=data.get('genus', ''),
            nutritions=data.get('nutritions', {})
        )

def fetch_fruits():
    """Fetch fruits data from the Fruityvice API"""
    try:
        response = requests.get('https://www.fruityvice.com/api/fruit/all')
        response.raise_for_status()
        return [Fruit.from_api_data(item) for item in response.json()]
    except requests.RequestException:
        # Fallback data in case API is unavailable
        return [
            Fruit('Apple', 'Rosaceae', 'Rosales', 'Malus', 
                 {'calories': 52, 'carbohydrates': 14, 'protein': 0.3}),
            Fruit('Banana', 'Musaceae', 'Zingiberales', 'Musa',
                 {'calories': 96, 'carbohydrates': 22, 'protein': 1.2}),
            # Add more fallback fruits if needed
        ]

@app.route('/')
def index():
    return render_template('index.html', fruits=[])

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    if not query:
        return render_template('search_results.html', fruits=[])
    
    all_fruits = fetch_fruits()
    matching_fruits = [
        fruit for fruit in all_fruits
        if query in fruit.name.lower() or
           query in fruit.family.lower() or
           query in fruit.genus.lower()
    ]
    return render_template('search_results.html', fruits=matching_fruits)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')