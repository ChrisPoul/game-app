from .views import bp
from flask import Flask, render_template
from .sockets import socketio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

app.register_blueprint(bp)

socketio.init_app(app)
