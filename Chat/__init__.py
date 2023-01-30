from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO()
socketio.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")


@socketio.on("message")
def handle_message(message):
    print(message)
    send(message, broadcast=True)


def some_function():
    socketio.emit('some event', {'data': "algo raro"})


if __name__ == '__main__':
    socketio.run(app)
