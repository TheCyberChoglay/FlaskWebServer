# app_routes.py

from flask import Blueprint, render_template

# Create a Blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def home():
    """
    Route for the home page.
    """
    return render_template('index.html')
