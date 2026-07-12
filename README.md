# StudyDeck

Small Flask flashcard/quiz app. Decks contain multiple-choice cards; data lives in a local `data.json` (auto-seeded on first run).

## Install uv

macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify:

```bash
uv --version
```

## Run the app

```bash
uv run studydeck
```

Open http://127.0.0.1:7891 — decks seed automatically on first request.

## Run tests

```bash
uv run pytest -q
```

## Fallback: no uv (plain Python + pip)

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m flask --app app run
python -m pytest -q
```

## Get access to Junie

1. Go to junie.jetbrains.com
2. Follow the installation steps
3. Login to your JetBrains account (or create one)
4. After installation, type `/promo` and enter `JUNIECAMP` -> $35 credits

Hint: use cheaper models (like Google Gemini Flash 3) to stretch your credits further.

## Workshop tasks

Fresh copy of this repo, prompting only — no manual edits. Get Junie to plan before it touches code.

**Task 1: Add a difficulty property for each question, sort by difficulty during a quiz.**
Cards need a difficulty (easy/medium/hard); the quiz should order questions by difficulty instead of insertion order.

**Task 2: Add a submit button and a results page with points and mistakes (don't show before submit).**
Instead of per-question instant feedback, the quiz should collect all answers, only reveal correct/wrong once the whole quiz is submitted, and show a results page with score + which questions were missed.
