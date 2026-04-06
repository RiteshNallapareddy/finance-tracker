from flask import Flask
from flask_cors import CORS
from database import init_db
from routes.finance import finance_bp
from routes.stocks import stocks_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(finance_bp)
app.register_blueprint(stocks_bp)

init_db()

@app.route('/')
def home():
    return "Finance Tracker API is running!"

if __name__ == '__main__':
    app.run(debug=True)

