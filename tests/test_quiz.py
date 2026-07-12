def test_start_quiz_returns_cards(client):
    resp = client.get("/decks/1/quiz", headers={"Accept": "application/json"})
    assert resp.status_code == 200
    assert len(resp.json["cards"]) > 0


def test_answer_correct(client):
    resp = client.post("/decks/1/quiz/answer", data={"card_id": "1", "chosen_index": "1"})
    assert resp.status_code == 200
    assert resp.json["correct"] is True


def test_answer_wrong(client):
    resp = client.post("/decks/1/quiz/answer", data={"card_id": "1", "chosen_index": "0"})
    assert resp.status_code == 200
    assert resp.json["correct"] is False


def test_quiz_only_uses_selected_deck(client):
    resp = client.get("/decks/1/quiz", headers={"Accept": "application/json"})
    card_ids = {c["deck_id"] for c in resp.json["cards"]}
    assert card_ids == {1}
