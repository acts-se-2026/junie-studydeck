from flask import Blueprint, jsonify, render_template, request

import models

bp = Blueprint("quiz", __name__)


@bp.route("/decks/<int:deck_id>/quiz")
def start_quiz(deck_id):
    deck = models.get_deck(deck_id)
    cards = models.get_cards(deck_id)

    if request.headers.get("Accept") == "application/json":
        return jsonify({"cards": cards})
    return render_template("quiz.html", deck=deck, cards=cards)


@bp.route("/decks/<int:deck_id>/quiz/answer", methods=["POST"])
def answer(deck_id):
    card_id = int(request.form["card_id"])
    chosen_index = int(request.form["chosen_index"])
    card = models.get_card(card_id)
    correct = card["correct_index"] == chosen_index
    return jsonify({"correct": correct, "correct_index": card["correct_index"]})
