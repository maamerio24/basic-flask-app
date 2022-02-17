from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.blueprints.main import bp as main
    from app.blueprints.mlb import bp as mlb
    from app.blueprints.nfl import bp as nfl
    from app.blueprints.nba import bp as nba

    app.register_blueprint(main)
    app.register_blueprint(mlb)
    app.register_blueprint(nba)
    app.register_blueprint(nfl)

    return app
