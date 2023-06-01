from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'got_a_secret_can_you_keep_it'

from app import routes

if __name__ == '__main__':
    app.run()






