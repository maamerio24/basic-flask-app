from flask import Blueprint
from .import bp as main

@main.route('/')
def main():
    return "Hello! Welcome to my favorite teams. Type in /nba, /nfl, or /mlb to the end of the url to reveal what teams they are!"
