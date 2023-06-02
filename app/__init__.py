from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'got_a_secret_can_you_keep_it'
app.config.from_object(Config)

if __name__ == '__main__':
    app.run()

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

migrate = Migrate(app, db)


from app import routes, models






