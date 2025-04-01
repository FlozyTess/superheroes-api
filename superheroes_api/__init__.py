from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from superheroes_api.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    from .models import Hero, Power, HeroPower 
    
    #routes registration
    from .routes import main
    app.register_blueprint(main)
    
    return app