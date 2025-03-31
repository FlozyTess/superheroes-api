from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db, Hero,Power,HeroPower

app = Flask(__name__) #initialize app

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Superhero API"

if __name__ == '__main__':
    app.run(debug=True)
