def test_add_card_to_deck(client):
    resp = client.post(
        "/decks/1/cards",
        data={
            "question": "10 / 2 = ?",
            "option_a": "5",
            "option_b": "2",
            "option_c": "20",
            "correct_index": "0",
        },
        follow_redirects=True,
    )
    assert resp.status_code == 200
    assert b"10 / 2 = ?" in resp.data
