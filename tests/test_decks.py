def test_list_decks_shows_seeded_decks(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Math" in resp.data
    assert b"German" in resp.data


def test_create_deck(client):
    resp = client.post("/decks", data={"name": "History"}, follow_redirects=True)
    assert resp.status_code == 200
    assert b"History" in resp.data
