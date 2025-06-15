from server.app import create_app
from server.db.database import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    # Create all tables
    db.create_all()
    print("Tables created successfully!")
    
    # Verify tables
    print("Existing tables:")
    for table in db.metadata.tables:
        print(f"- {table}")