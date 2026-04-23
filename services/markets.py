# Singapore Time: 2026-04-23 09:07
# Market API Blueprint
# 逻辑说明：
# - 提供一个 /api/markets endpoint
# - 返回模拟市场数据
# - Blueprint 必须叫 markets_bp（和 app.py 对应）

from flask import Blueprint, jsonify

# 创建 Blueprint（名字必须一致）
markets_bp = Blueprint('markets', __name__, url_prefix='/api')

# 路由：获取市场数据
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
