from flask import Blueprint
from .import bp as nfl


@nfl.route('/')
def raiders():
    return "My favorite NFL team is the Las Vegas Raiders."
