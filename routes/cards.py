from flask import Blueprint, redirect, request, url_for

import models

bp = Blueprint("cards", __name__)


@bp.route("/decks/<int:deck_id>/cards", methods=["POST"])
def add_card(deck_id):
    question = request.form["question"]
    options = [
        request.form["option_a"],
        request.form["option_b"],
        request.form["option_c"],
    ]
    correct_index = int(request.form["correct_index"])
    models.create_card(deck_id, question, options, correct_index)
    return redirect(url_for("decks.deck_detail", deck_id=deck_id))
