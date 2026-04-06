from flask import Blueprint, jsonify, request
from database import get_db_connection
from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_KEY=os.getenv('ALPHA_VANTAGE_KEY')

# Create the Blueprint object
stocks_bp = Blueprint('stocks', __name__)

# Then use stock_bp instead of app
@stocks_bp.route('/portfolio', methods=['GET'])
def get_portfolio():
    connection = get_db_connection()
    portfolio = connection.execute("SELECT * FROM portfolio").fetchall()
    connection.close()

    return jsonify([dict(row) for row in portfolio])

@stocks_bp.route('/portfolio', methods=['POST'])
def post_portfolio():
    data = request.get_json()
    stock_name = data['stock_name']
    symbol = data['symbol']
    shares = data['shares']
    purchase_price = data['purchase_price']
    purchase_date = data['purchase_date']

    connection = get_db_connection()
    connection.execute("""
    INSERT INTO portfolio (stock_name, symbol, shares, purchase_price, purchase_date)
    VALUES (?, ?, ?, ?, ?)""", (stock_name, symbol, shares, purchase_price, purchase_date))
    connection.commit()
    connection.close()

    return jsonify({"message" : 'Porfolio updated!'}), 201

@stocks_bp.route('/portfolio/price', methods=['GET'])
def get_price():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error' : 'Symbol is required'}) , 400
    
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    if 'Global Quote' not in data  or '05. price' not in data['Global Quote']:
        return jsonify({'error' : 'Invalid symbol or API limit reached'}), 404
    
    price = data['Global Quote']['05. price']

    return jsonify({'symbol': symbol, 'price': price})

