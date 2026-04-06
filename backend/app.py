import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from database import init_db
from routes.finance import finance_bp
from routes.stocks import stocks_bp
from routes.news import news_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(finance_bp)
app.register_blueprint(stocks_bp)
app.register_blueprint(news_bp)

init_db()

@app.route('/')
def home():
    return "Finance Tracker API is running!"

if __name__ == '__main__':
    app.run(debug=False)