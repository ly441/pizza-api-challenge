from flask import Flask, jsonify
from flask_migrate import Migrate
from server.db.config import Config
from server.db.database import db, init_app  
from server.models.restaurant import Restaurant

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database with the app
    init_app(app)  # Use the init_app function from database.py
    
    # Initialize migrations
    migrate = Migrate(app, db)
    
    # Register blueprints
    from controllers import (
        restaurants_bp, 
        pizzas_bp, 
        restaurant_pizzas_bp
    )
    
    app.register_blueprint(restaurants_bp, url_prefix='/restaurants')
    app.register_blueprint(pizzas_bp, url_prefix='/pizzas')
    app.register_blueprint(restaurant_pizzas_bp, url_prefix='/restaurant_pizzas')
    
    # Test route
    @app.route('/')
    def index():
        return jsonify({"message": "Pizza Restaurant API"})
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=app.config['DEBUG'])
    