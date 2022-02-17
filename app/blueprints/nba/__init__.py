from flask import Blueprint

bp = Blueprint('nba', __name__, url_prefix='/nba')

from .import routes