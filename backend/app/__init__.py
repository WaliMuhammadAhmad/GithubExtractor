from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS

        # Register routes
    from .routes import main_routes
    app.register_blueprint(main_routes)

    # Load configuration with error handling
    try:
        app.config.from_pyfile('config.py')
    except FileNotFoundError:
        print("Configuration file not found.")
    except Exception as e:
        print(f"An error occurred while loading the configuration file: {e}")

    return app