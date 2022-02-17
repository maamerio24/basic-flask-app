from flask import Blueprint
from .import bp as nba

@nba.route('/')
def lakers():
    return "My favorite NBA team is the Los Angeles Lakers."
