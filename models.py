from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.model):
    __tablename__= 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
  
    #relationship with hero power
    hero_powers = db.relationship('HeroPower', backref='hero', cascade="all, delete")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name,
            "hero_powers": [hero_power.to_dict() for hero_power in self.hero_powers]
        }
