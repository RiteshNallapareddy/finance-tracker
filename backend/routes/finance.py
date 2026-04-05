from flask import Blueprint
from flask import jsonify
from flask import request
from database import get_db_connection

# Create the Blueprint object
finance_bp = Blueprint('finance', __name__)

# Then use finance_ap instead of app
@finance_bp.route('/transactions', methods=['GET'])
def get_transactions():
    connection = get_db_connection()
    transactions = connection.execute("SELECT * FROM transactions").fetchall()
    connection.close()

    return jsonify([dict(row) for row in transactions])


@finance_bp.route('/transactions', methods=['POST'])
def post_transactions():
    data = request.get_json()
    amount = data['amount']
    category = data['category']
    type = data['type']
    date = data['date']
    description = data['description']
    
    connection = get_db_connection()
    connection.execute("""
    INSERT INTO transactions (amount, category, type, date, description)
    VALUES (?, ?, ?, ?, ?)""", (amount, category, type, date, description))
    connection.commit()
    connection.close()

    return jsonify({'message': 'Transaction added!'}), 201