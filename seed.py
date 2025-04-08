import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from superheroes_api import create_app, db
from superheroes_api.models import Hero, Power, HeroPower

app = create_app()

with app.app_context():
    db.create_all()

# Create hero
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Carol Danvers", super_name="Captain Marvel")
    
# Create powers    
    power1 = Power(name="Flight", description="Gives the wielder the ability to fly at supersonic speeds")
    power2 = Power(name="Super Strength", description="Gives the wielder super-human strength")

# Assign powers to heroes
    hero_power1 = HeroPower(hero=hero1, power=power1, strength="Strong")
    hero_power2 = HeroPower(hero=hero2, power=power2, strength="Average")


    db.session.add_all([hero1, hero2, power1, power2, hero_power1, hero_power2])
    db.session.commit()

    print("Data seeded successfully.")