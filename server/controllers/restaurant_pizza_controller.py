from flask import Blueprint, jsonify, request
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from server.db import db

restaurants_bp = Blueprint('restaurants', __name__)

@restaurants_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants])

@restaurants_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    pizzas = [{
        'id': rp.pizza.id,
        'name': rp.pizza.name,
        'ingredients': rp.pizza.ingredients,
        'price': rp.price
    } for rp in restaurant.pizzas]
    
    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': pizzas
    })
@restaurants_bp.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    new_restaurant = Restaurant(
        name=data['name'],
        address=data['address']
    )
    db.session.add(new_restaurant)
    db.session.commit()
    return jsonify({'id': new_restaurant.id}), 200
@restaurants_bp.route('/restaurants', methods=['PUT'])
def update_restaurant():
    data = request.get_json()
    restaurant = Restaurant.query.get(data['id'])
    
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    restaurant.name = data['name']
    restaurant.address = data['address']
    
    db.session.commit()
    return jsonify({'id': restaurant.id}), 200

@restaurants_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204