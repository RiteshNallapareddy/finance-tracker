from flask import Flask
from database import init_db
from routes.finance import finance_bp

app = Flask(__name__)

app.register_blueprint(finance_bp)

init_db()

@app.route('/')
def home():
    return "Finance Tracker API is running!"

if __name__ == '__main__':
    app.run(debug=True)
