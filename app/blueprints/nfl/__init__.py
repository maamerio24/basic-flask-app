from flask import Blueprint

bp = Blueprint('nfl', __name__, url_prefix='/nfl')

from .import routes 