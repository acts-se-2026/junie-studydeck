from .decks import bp as decks_bp
from .cards import bp as cards_bp
from .quiz import bp as quiz_bp


def register_routes(app):
    app.register_blueprint(decks_bp)
    app.register_blueprint(cards_bp)
    app.register_blueprint(quiz_bp)
