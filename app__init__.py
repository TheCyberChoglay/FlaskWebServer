# app_init.py

from flask import Flask

def create_app():
    """
    Factory function to create and configure the Flask app.
    """
    app = Flask(__name__)
    
    # Import and register routes
    from app_routes import main
    app.register_blueprint(main)

    return app
