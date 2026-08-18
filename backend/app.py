from flask import Flask, request, jsonify
from flask_cors import CORS
from decision_engine import get_compensation

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Flight Delay AI System Running 🚀"

@app.route("/check-delay", methods=["POST"])
def check_delay():
    data = request.get_json()

    delay = data["delay_hours"]
    ptype = data["passenger_type"]

    result = get_compensation(delay, ptype)

    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)