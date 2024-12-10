# app.py

from app__init__ import create_app

# Create an instance of the Flask app
app = create_app()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
