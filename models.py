from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.model):
    __tablename__= 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
  
    #relationship
    hero_powers = db.relationship('HeroPower', backref='hero', cascade="all, delete")