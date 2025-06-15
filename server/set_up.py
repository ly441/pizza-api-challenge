from app import create_app
from database import db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    # Create all tables
    db.create_all()
    print("Tables created successfully!")
    
    # Verify tables
    print("Existing tables:")
    for table in db.metadata.tables:
        print(f"- {table}")