from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO
import redis
import eventlet


eventlet.monkey_patch()
app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')
redis_cache = redis.Redis(host='redis', port='6379', db=0)

@app.route('/prices', methods=['GET'])
def get_prices():
    keys = redis_cache.keys('ticket:*')
    prices = {key.decode('utf-8'): redis_cache.get(key).decode('utf-8') for key in keys}
    return jsonify(prices)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/realtime')
def realtime():
    prices = get_prices()
    return render_template('realtime.html')

@socketio.on('update')
def handle_update(data):
    print('Actualización recibida', data)
    socketio.emit('update', data, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5001, allow_unsafe_werkzeug=True)