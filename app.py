# 🕒 Singapore Time: 2026-04-22 11:26
# =========================================
# 这是主入口 Flask App
# 作用：注册所有 API 路由（Blueprint）
# =========================================

from flask import Flask

# 导入各个模块（Blueprint）
from services.health import health_bp
from services.status import status_bp
from services.markets import markets_bp
from services.signals import signals_bp
from strategies.basic import strategy_bp

# 初始化 Flask
app = Flask(__name__)

# =========================================
# 注册所有模块（非常关键！）
# =========================================
app.register_blueprint(health_bp)
app.register_blueprint(status_bp)
app.register_blueprint(markets_bp)
app.register_blueprint(signals_bp)
app.register_blueprint(strategy_bp)

# =========================================
# 默认首页（测试用）
# =========================================
@app.route("/")
def home():
    return "MiroFish Backend Running 🚀"

# =========================================
# 启动服务
# =========================================
if __name__ == "__main__":
    # 说明：
    # host=0.0.0.0 → 允许外部访问（Zeabur必须）
    # port=5000 → 必须和Zeabur端口一致
    app.run(host="0.0.0.0", port=5000)
