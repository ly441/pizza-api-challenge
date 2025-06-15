from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy instance
db = SQLAlchemy()

# Optional: Add helper functions
def init_app(app):
    """Initialize the database with the Flask app"""
    db.init_app(app)
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()