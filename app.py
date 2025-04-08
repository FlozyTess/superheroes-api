from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///superheroes.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.json.compact = False

    
    db.init_app(app)
    
  
    migrate = Migrate(app, db)

    # Home route
    @app.route('/')
    def home():
        return "Hello, This is a Superheroes API"

    # Routes for heroes
    @app.route("/heroes", methods=["GET"])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([hero.to_dict() for hero in heroes]), 200

    @app.route("/heroes/<int:id>", methods=["GET"])
    def get_hero(id):
        hero = Hero.query.get(id)
        if hero:
            return jsonify(hero.to_dict()), 200
        return jsonify({"error": "Hero not found"}), 404

    # Routes for powers
    @app.route("/powers", methods=["GET"])
    def get_powers():
        powers = Power.query.all()
        return jsonify([power.to_dict() for power in powers]), 200

    @app.route("/powers/<int:id>", methods=["GET"])
    def get_power(id):
        power = Power.query.get(id)
        if power:
            return jsonify(power.to_dict()), 200
        return jsonify({"error": "Power not found"}), 404

    # Update power route
    @app.route("/powers/<int:id>", methods=["PATCH"])
    def update_power(id):
        power = Power.query.get(id)
        if not power:
            return jsonify({"error": "Power not found"}), 404
        
        data = request.get_json()
        description = data.get("description")
        
        if not description or len(description) < 20:
            return jsonify({"errors": ["Description must be at least 20 characters long"]}), 400
        
        power.description = description
        db.session.commit()
        return jsonify(power.to_dict()), 200

    # HeroPower route (creates associations between heroes and powers)
    @app.route("/hero_powers", methods=["POST"])
    def create_hero_power():
        data = request.get_json()
        strength = data.get("strength")
        hero_id = data.get("hero_id")
        power_id = data.get("power_id")

        if strength not in ["Strong", "Weak", "Average"]:
            return jsonify({"errors": ["Strength must be 'Strong', 'Weak', or 'Average'"]}), 400

        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)
        
        if not hero or not power:
            return jsonify({"errors": ["Invalid hero or power ID"]}), 400
        
        hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
        db.session.add(hero_power)
        db.session.commit()
        
        return jsonify(hero_power.to_dict()), 201

    return app

if __name__ == "__main__":
    app = create_app()  
    app.run(debug=True)
