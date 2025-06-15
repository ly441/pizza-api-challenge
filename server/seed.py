from server.app import create_app
from server.db.database import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    # Clear existing data
    db.reflect()
    db.drop_all()
    db.create_all()

    # Create restaurants
    restaurants = [
        Restaurant(name="New York Pizza", address="123 Broadway, NY"),
        Restaurant(name="Chicago Deep Dish", address="456 Windy St, IL"),
        Restaurant(name="California Pizza", address="789 Sunny Blvd, CA")
    ]
    
    # Create pizzas
    pizzas = [
        Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil"),
        Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni"),
        Pizza(name="Vegetarian", ingredients="Tomato, Mozzarella, Vegetables")
    ]
    
    db.session.add_all(restaurants + pizzas)
    db.session.commit()
    
    # Create associations
    restaurant_pizzas = [
        RestaurantPizza(restaurant_id=restaurants[0].id, pizza_id=pizzas[0].id, price=12),
        RestaurantPizza(restaurant_id=restaurants[0].id, pizza_id=pizzas[1].id, price=15),
        RestaurantPizza(restaurant_id=restaurants[1].id, pizza_id=pizzas[2].id, price=18),
        RestaurantPizza(restaurant_id=restaurants[2].id, pizza_id=pizzas[0].id, price=14),
        RestaurantPizza(restaurant_id=restaurants[2].id, pizza_id=pizzas[2].id, price=16)
    ]
    
    db.session.add_all(restaurant_pizzas)
    db.session.commit()
    print("Database seeded successfully!")
    