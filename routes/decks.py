from flask import Blueprint, redirect, render_template, request, url_for

import models

bp = Blueprint("decks", __name__)


@bp.route("/")
def list_decks():
    decks = models.get_decks()
    return render_template("decks_list.html", decks=decks)


@bp.route("/decks", methods=["POST"])
def create_deck():
    name = request.form["name"]
    models.create_deck(name)
    return redirect(url_for("decks.list_decks"))


@bp.route("/decks/<int:deck_id>")
def deck_detail(deck_id):
    deck = models.get_deck(deck_id)
    cards = models.get_cards(deck_id)
    return render_template("deck_detail.html", deck=deck, cards=cards)
