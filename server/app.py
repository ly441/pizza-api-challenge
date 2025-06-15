from flask import Flask, jsonify
from flask_migrate import Migrate
from server.db.config import Config
from server.db.database import db, init_app  
from server.controllers import (
    restaurants_bp, 
    pizzas_bp, 
    restaurant_pizzas_bp
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    
    init_app(app)
    
    
    migrate = Migrate(app, db)
    
    # Register blueprints
    app.register_blueprint(restaurants_bp, url_prefix='/restaurants')
    app.register_blueprint(pizzas_bp, url_prefix='/pizzas')
    app.register_blueprint(restaurant_pizzas_bp, url_prefix='/restaurant_pizzas')
    
    @app.route('/test_db')
    def test_db():
        try:
            db.session.execute('SELECT 1')
            return jsonify({"message": "Database connection successful!"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/')
    def index():
        return jsonify({"message": "Pizza Restaurant API"})
    
    return app

app = create_app()
if __name__ == '__main__':
    app.run(port=5555, debug=app.config['DEBUG'])
