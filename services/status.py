# 🕒 Singapore Time: 2026-04-22 11:34
# =========================================
# Status endpoint
# =========================================

from flask import Blueprint
import os

# 定义 Blueprint（必须有）
status_bp = Blueprint('status', __name__, url_prefix='/api')

# 路由
@status_bp.route('/status')
def status():
    return {
        "name": "mirofish-backend",
        "version": "1.0.0",
        "environment": os.getenv("ENV", "production")
    }, 200
