# Flask app for Option Pricing Calculator

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/option_price', methods=['POST'])
def calculate_option_price():
    # Example input:  {'type': 'call', 'strike': 100, 'spot': 105, 'volatility': 0.2, 'time_to_maturity': 1}
    data = request.json
    # Implement option pricing logic here (Black-Scholes or others)
    price = 0  # Placeholder for actual price calculation
    return jsonify({'price': price})

if __name__ == '__main__':
    app.run(debug=True)