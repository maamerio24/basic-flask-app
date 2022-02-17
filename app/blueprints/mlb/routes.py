from flask import Blueprint
from .import bp as mlb

@mlb.route('/')
def dodgers():
    return "My favorite MLB team is the Los Angeles Dodgers."