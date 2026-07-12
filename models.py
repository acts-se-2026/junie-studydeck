from flask import current_app

import storage


def _load():
    return storage.load(current_app.config["DATA_FILE"])


def _save(data):
    storage.save(data, current_app.config["DATA_FILE"])


def _next_id(items):
    return max((item["id"] for item in items), default=0) + 1


def get_decks():
    return _load()["decks"]


def get_deck(deck_id):
    return next((d for d in get_decks() if d["id"] == deck_id), None)


def create_deck(name):
    data = _load()
    deck = {"id": _next_id(data["decks"]), "name": name}
    data["decks"].append(deck)
    _save(data)
    return deck


def get_cards(deck_id=None):
    cards = _load()["cards"]
    if deck_id is None:
        return cards
    return [c for c in cards if c["deck_id"] == deck_id]


def get_card(card_id):
    return next((c for c in _load()["cards"] if c["id"] == card_id), None)


def create_card(deck_id, question, options, correct_index):
    data = _load()
    card = {
        "id": _next_id(data["cards"]),
        "deck_id": deck_id,
        "question": question,
        "options": options,
        "correct_index": correct_index,
    }
    data["cards"].append(card)
    _save(data)
    return card
