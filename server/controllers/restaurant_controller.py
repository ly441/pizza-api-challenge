from flask import Blueprint, jsonify, request
from server.models.restaurant import Restaurant  
from server.models.restaurant_pizza import RestaurantPizza 
from server.db.database import db  

restaurants_bp = Blueprint('restaurants', __name__)



restaurant_pizzas_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizzas_bp.route('/restaurant_pizzas', methods=['GET'])
def get_restaurant_pizzas():
    rps = RestaurantPizza.query.all()
    return jsonify([{
        'id': rp.id,
        'price': rp.price,
        'pizza_id': rp.pizza_id,
        'restaurant_id': rp.restaurant_id
    } for rp in rps])

@restaurant_pizzas_bp.route('/restaurant_pizzas/<int:id>', methods=['GET'])
def get_restaurant_pizza(id):
    rp = RestaurantPizza.query.get_or_404(id)
    return jsonify({
        'id': rp.id,
        'price': rp.price,
        'pizza_id': rp.pizza_id,
        'restaurant_id': rp.restaurant_id
    })

@restaurant_pizzas_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    required = ['price', 'pizza_id', 'restaurant_id']
    if not all(field in data for field in required):
        return jsonify({'errors': ['Missing required fields']}), 400
    restaurant = Restaurant.query.get(data['restaurant_id'])
    pizza = Pizza.query.get(data['pizza_id'])
    if not restaurant or not pizza:
        return jsonify({'errors': ['Restaurant or Pizza not found']}), 404
    try:
        rp = RestaurantPizza(
            price=data['price'],
            restaurant_id=data['restaurant_id'],
            pizza_id=data['pizza_id']
        )
        db.session.add(rp)
        db.session.commit()
        return jsonify({
            'id': rp.id,
            'price': rp.price,
            'pizza_id': rp.pizza_id,
            'restaurant_id': rp.restaurant_id
        }), 201
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400

@restaurant_pizzas_bp.route('/restaurant_pizzas/<int:id>', methods=['PUT'])
def update_restaurant_pizza(id):
    rp = RestaurantPizza.query.get_or_404(id)
    data = request.get_json()
    if not data:
        abort(400, description="No input data provided")
    rp.price = data.get('price', rp.price)
    rp.pizza_id = data.get('pizza_id', rp.pizza_id)
    rp.restaurant_id = data.get('restaurant_id', rp.restaurant_id)
    db.session.commit()
    return jsonify({
        'id': rp.id,
        'price': rp.price,
        'pizza_id': rp.pizza_id,
        'restaurant_id': rp.restaurant_id
    })

@restaurant_pizzas_bp.route('/restaurant_pizzas/<int:id>', methods=['DELETE'])
def delete_restaurant_pizza(id):
    rp = RestaurantPizza.query.get_or_404(id)
    db.session.delete(rp)
    db.session.commit()
    return jsonify({'message': 'RestaurantPizza deleted'})
    