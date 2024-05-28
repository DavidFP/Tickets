from flask import Flask, jsonify, render_template
import redis

app = Flask(__name__)

redis_cache = redis.Redis(host='redis', port='6379', db=0)

@app.route('/prices', methods=['GET'])
def get_prices():
    keys = redis_cache.keys('ticket:*')
    prices = {key.decode('utf-8'): redis_cache.get(key).decode('utf-8') for key in keys}
    return jsonify(prices)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)