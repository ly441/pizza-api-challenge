from flask import Blueprint, jsonify, request, abort
from server.models.pizza import Pizza, db

pizzas_bp = Blueprint('pizzas', __name__)

@pizzas_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'ingredients': p.ingredients
    } for p in pizzas])

@pizzas_bp.route('/pizzas/<int:id>', methods=['GET'])
def get_pizza(id):
    pizza = Pizza.query.get_or_404(id)
    return jsonify({
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    })

@pizzas_bp.route('/pizzas', methods=['POST'])
def create_pizza():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('ingredients'):
        abort(400, description="Missing required fields")
    new_pizza = Pizza(
        name=data['name'],
        ingredients=data['ingredients']
    )
    db.session.add(new_pizza)
    db.session.commit()
    return jsonify({'id': new_pizza.id}), 201

@pizzas_bp.route('/pizzas/<int:id>', methods=['PUT'])
def update_pizza(id):
    pizza = Pizza.query.get_or_404(id)
    data = request.get_json()
    if not data:
        abort(400, description="No input data provided")
    pizza.name = data.get('name', pizza.name)
    pizza.ingredients = data.get('ingredients', pizza.ingredients)
    db.session.commit()
    return jsonify({
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    })

@pizzas_bp.route('/pizzas/<int:id>', methods=['DELETE'])
def delete_pizza(id):
    pizza = Pizza.query.get_or_404(id)
    db.session.delete(pizza)
    db.session.commit()
    return jsonify({'message': 'Pizza deleted'})
