from flask import Blueprint, jsonify, request
from models import db, Hero, Power, HeroPower

main = Blueprint('main', __name__)

@main.route('/superheroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes]), 200

@main.route('/superheroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict()), 200

@main.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers]), 200

@main.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200

@main.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.json
    if "description" in data and len(data["description"]) < 20:
        return jsonify({"errors": ["Description must be at least 20 characters"]}), 400

    power.description = data["description"]
    db.session.commit()
    return jsonify(power.to_dict()), 200

@main.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    if data["strength"] not in ["Strong", "Weak", "Average"]:
        return jsonify({"errors": ["Invalid strength value"]}), 400

    hero_power = HeroPower(hero_id=data["hero_id"], power_id=data["power_id"], strength=data["strength"])
    db.session.add(hero_power)
    db.session.commit()
    
    return jsonify(hero_power.to_dict()), 201

