import os

from flask import Flask

import seed_data
from routes import register_routes


def create_app(data_file=None):
    app = Flask(__name__)
    app.config["DATA_FILE"] = data_file or os.path.join(os.path.dirname(__file__), "data.json")
    seed_data.ensure_seeded(app.config["DATA_FILE"])
    register_routes(app)
    return app


def main():
    create_app().run(debug=True, port=7891)


if __name__ == "__main__":
    main()
