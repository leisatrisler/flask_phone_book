from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
# app.config["SECRET_KEY"] = "got_a_secret_can_you_keep_it"
app.config.from_object(Config)

# if __name__ == "__main__":
#     app.run()

db = SQLAlchemy(app)

migrate = Migrate(app, db)

login = LoginManager(app)

login.login_view = "login"

login.login_message_category = "warning"

from app import routes, models
