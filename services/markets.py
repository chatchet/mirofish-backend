from flask import Blueprint, jsonify

markets_bp = Blueprint('markets', __name__, url_prefix='/api')

@markets_bp.route('/markets')
def get_markets():
    return jsonify({
        "BTC-USD": {
            "price": 63421.50,
            "change_24h": 2.34,
            "indicators": {
                "rsi": 62.4
            }
        }
    }), 200
