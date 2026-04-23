# 🕒 Singapore Time: 2026-04-22 11:32
# =========================================
# Health check endpoint
# =========================================

from flask import Blueprint

# 定义 Blueprint（必须有！）
health_bp = Blueprint('health', __name__)

# 路由
@health_bp.route('/health')
def health():
    return {"status": "OK"}, 200
