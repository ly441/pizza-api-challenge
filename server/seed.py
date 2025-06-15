from app import create_app
from models import db, Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Seed restaurants
    restaurants = [
        Restaurant(name="Pizza Palace", address="123 Main St"),
        Restaurant(name="Italian Corner", address="456 Oak Ave"),
        Restaurant(name="Slice Heaven", address="789 Pine Rd")
    ]
    db.session.add_all(restaurants)
    
    # Seed pizzas
    pizzas = [
        Pizza(name="Margherita", ingredients="Tomato sauce, Mozzarella, Basil"),
        Pizza(name="Pepperoni", ingredients="Tomato sauce, Mozzarella, Pepperoni"),
        Pizza(name="Vegetarian", ingredients="Tomato sauce, Mozzarella, Vegetables")
    ]
    db.session.add_all(pizzas)
    
    db.session.commit()
    
    # Seed restaurant_pizzas
    restaurant_pizzas = [
        RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
        RestaurantPizza(price=12, restaurant_id=1, pizza_id=2),
        RestaurantPizza(price=9, restaurant_id=2, pizza_id=1),
        RestaurantPizza(price=11, restaurant_id=3, pizza_id=3)
    ]
    db.session.add_all(restaurant_pizzas)
    db.session.commit()
    
    print("Database seeded successfully!")