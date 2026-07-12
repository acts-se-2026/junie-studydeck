import os

import storage

SEED = {
    "decks": [
        {"id": 1, "name": "Math"},
        {"id": 2, "name": "German"},
    ],
    "cards": [
        {"id": 1, "deck_id": 1, "question": "Which is larger: e^π or π^e?", "options": ["π^e", "e^π", "They're equal"], "correct_index": 1},
        {"id": 2, "deck_id": 1, "question": "What does 0.999... (repeating forever) equal?", "options": ["Slightly less than 1", "Exactly 1", "It's undefined"], "correct_index": 1},
        {"id": 3, "deck_id": 1, "question": "A bat and ball cost $1.10 together. The bat costs $1 more than the ball. How much is the ball?", "options": ["$0.10", "$0.05", "$1.00"], "correct_index": 1},
        {"id": 4, "deck_id": 2, "question": "How do you say 'homework' in German?", "options": ["Hausaufgabe", "Handtuch", "Haustier"], "correct_index": 0},
        {"id": 5, "deck_id": 2, "question": "What does 'Freund' mean in English?", "options": ["Enemy", "Friend", "Teacher"], "correct_index": 1},
        {"id": 6, "deck_id": 2, "question": "Which German word means 'weekend'?", "options": ["Wochenende", "Wochentag", "Woche"], "correct_index": 0},
    ],
}


def ensure_seeded(path):
    if os.path.exists(path):
        return
    storage.save(SEED, path)
