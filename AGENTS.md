# Agent instructions

- Run `uv run pytest -q` before considering any change done.
- Use `uv run studydeck` to run the app locally (port 7891); `uv run pytest -q` for tests.
- Keep the flat module layout (`app.py`, `models.py`, `storage.py`, `routes/`, `templates/`, `static/`) — don't restructure into a `src/` package.
- Data is a JSON file (`data.json`, auto-seeded from `seed_data.py`), not a database. Don't introduce SQLAlchemy/SQLite unless explicitly asked.
- `routes/quiz.py`, `routes/decks.py`, `routes/cards.py` are Flask blueprints registered in `routes/__init__.py` — new endpoints belong in the matching file, not a new top-level module.
