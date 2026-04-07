from flask import Blueprint, jsonify, request
from database import get_db_connection
import yfinance as yf

# Get current price
def get_stock_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        price = ticker.info['currentPrice']
        return round(float(price), 2)
    except:
        return None

# Create the Blueprint object
stocks_bp = Blueprint('stocks', __name__)

# Then use stock_bp instead of app
@stocks_bp.route('/portfolio', methods=['GET'])
def get_portfolio():
    connection = get_db_connection()
    portfolio = connection.execute("SELECT * FROM portfolio").fetchall()
    connection.close()
    result = []

    for stock in portfolio:
        stock_dict = dict(stock)
        current_price = get_stock_price(stock_dict['symbol'])
        if current_price is None:
            stock_dict['current_price'] = None
            stock_dict['profit_loss'] = None
        else:
            profit_loss = round((current_price - stock_dict['purchase_price']) * stock_dict['shares'], 2)
            stock_dict['current_price'] = current_price
            stock_dict['profit_loss'] = profit_loss

        result.append(stock_dict)
    return jsonify(result)

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
    
    price = get_stock_price(symbol)
    if price is None:
        return jsonify({'error' : 'Invalid symbol or API limit reached'}), 404
    return jsonify({'symbol': symbol, 'price': price})

@stocks_bp.route('/portfolio/<int:id>', methods=['DELETE'])
def delete_stock(id):
    connection = get_db_connection()
    connection.execute("DELETE FROM portfolio WHERE id = ?", (id,))
    connection.commit()
    connection.close()

    return jsonify({'message': 'Stock deleted!'}), 200
