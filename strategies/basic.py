# 🕒 Singapore Time: 2026-04-23 09:12
# =========================================
# Strategy API Blueprint
# =========================================
# 功能说明：
# 提供策略接口 /api/strategy
# 用于测试 backend 是否正常工作
#
# 逻辑来源：
# Flask Blueprint 标准结构
# 每个模块必须导出 *_bp 才能被 app.py import
#
# 参数说明：
# url_prefix='/api' → 统一 API 前缀
#
# 修改方法：
# 未来可以在这里加入真实 trading strategy

from flask import Blueprint, jsonify

# Blueprint 名字必须和 app.py 对应
strategy_bp = Blueprint('strategy', __name__, url_prefix='/api')

@strategy_bp.route('/strategy')
def get_strategy():
    return jsonify({
        "strategy": "basic",
        "signal": "neutral",
        "confidence": 0.5
    }), 200
