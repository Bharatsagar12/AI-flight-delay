from flask import Flask, request, jsonify
from flask_cors import CORS
from decision_engine import get_compensation

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Flight Delay AI System Running 🚀"

@app.route('/check-delay', methods=['POST'])
def check_delay():
    data = request.json
    
    delay_hours = data.get("delay_hours")
    passenger_type = data.get("passenger_type", "economy")

    result = get_compensation(delay_hours, passenger_type)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)