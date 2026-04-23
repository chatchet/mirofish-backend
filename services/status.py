from flask import Blueprint
import os

status_bp = Blueprint('status', __name__, url_prefix='/api')

@status_bp.route('/status')
def status():
    return {
        "name": "mirofish-backend",
        "version": "1.0.0",
        "environment": os.getenv("ENV", "production")
    }, 200
