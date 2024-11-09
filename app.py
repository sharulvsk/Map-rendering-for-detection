from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('test_map.html')

def update_location():
    while True:
        lat = -34.397 + (random.random() - 0.5) * 0.01
        lng = 150.644 + (random.random() - 0.5) * 0.01
        socketio.emit('location_update', {'lat': lat, 'lng': lng})
        time.sleep(5)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    threading.Thread(target=update_location).start()
    socketio.run(app, debug=True)
