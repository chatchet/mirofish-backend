from flask import Blueprint, jsonify

signals_bp = Blueprint('signals', __name__, url_prefix='/api')

@signals_bp.route('/signals')
def get_signals():
    return jsonify({
        "signal": "bullish",
        "confidence": 0.75,
        "timestamp": "2026-04-23T08:36:00+08:00",
        "conditions": ["volume_spike", "rsi_recovery"]
    }), 200
