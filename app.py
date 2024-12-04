# app.py

from app_init import create_app

# Create an instance of the Flask app
app = create_app()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
