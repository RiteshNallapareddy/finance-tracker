from flask import Blueprint, jsonify, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

news_bp = Blueprint('news', __name__)

def format_articles(articles):
    # Format each article
    result = []
    for article in articles[:10]: # limit to 10 articles
        result.append({
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'publishedAt': article['publishedAt']
        })
    return result

@news_bp.route('/news', methods=['GET'])
def get_news():
    url = f'https://newsapi.org/v2/everything?q=stock+market+finance&sortBy=publishedAt&apikey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])

    return jsonify(format_articles(articles))
        
@news_bp.route('/news/stock', methods=['GET'])
def get_stock_news():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error' : 'Symbol is required'}) , 400
    
    url = f'https://newsapi.org/v2/everything?q={symbol}&sortBy=publishedAt&apikey={NEWS_API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])

    return jsonify(format_articles(articles))