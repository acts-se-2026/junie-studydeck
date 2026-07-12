import pytest

import storage
from app import create_app
from seed_data import SEED


@pytest.fixture
def data_file(tmp_path):
    path = tmp_path / "data.json"
    storage.save(SEED, str(path))
    return str(path)


@pytest.fixture
def app(data_file):
    app = create_app(data_file=data_file)
    app.config.update(TESTING=True)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_decks():
    return {"math_id": 1, "german_id": 2}
