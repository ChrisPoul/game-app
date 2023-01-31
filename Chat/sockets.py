from flask_socketio import SocketIO, send, emit

socketio = SocketIO()


@socketio.on("message")
def handle_message(message):
    print(message)
    send(message, broadcast=True)
