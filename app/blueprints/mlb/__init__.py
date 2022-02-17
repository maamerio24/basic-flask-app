from flask import Blueprint

bp = Blueprint('mlb', __name__, url_prefix='/mlb')

from .import routes


