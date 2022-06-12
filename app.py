from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)  # Creating a SocketIO instance for the flask app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat')
def chat():
    username = request.args.get('username')  # used to fetch the data from the REST request
    room_id = request.args.get('room_id')

    if username and room_id:
        return render_template('chat.html', username=username, room_id=room_id)
    else:
        return redirect(url_for('home'))  # we can directly use redirect('/'), but url_for is more organised

@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info(f"{data['username']} has joined the room {data['room']}")

if __name__ == '__main__':
    socketio.run(app,debug=True)
