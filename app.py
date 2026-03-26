from flask import Flask, render_template, request
import numpy as np
from models import black_scholes_price, delta, gamma, vega, theta, vol_surface
from visualization import plot_vol_surface_html

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/price', methods=['POST'])
def price():
    S = float(request.form['S'])
    K = float(request.form['K'])
    r = float(request.form['r'])
    sigma = float(request.form['sigma'])
    T = float(request.form['T'])

    price_val = black_scholes_price(S, K, r, sigma, T)
    delta_val = delta(S, K, r, sigma, T)
    gamma_val = gamma(S, K, r, sigma, T)
    vega_val = vega(S, K, r, sigma, T)
    theta_val = theta(S, K, r, sigma, T)

    K_list = np.linspace(80, 120, 10)
    T_list = np.linspace(0.1, 2, 10)
    market_prices = np.array([[black_scholes_price(S, k, r, sigma, t) for t in T_list] for k in K_list])
    surface = vol_surface(S, r, market_prices, K_list, T_list)
    html_graph = plot_vol_surface_html(K_list, T_list, surface)

    return render_template("result.html",
                           price=round(price_val, 4),
                           delta=round(delta_val, 4),
                           gamma=round(gamma_val, 4),
                           vega=round(vega_val, 4),
                           theta=round(theta_val, 4),
                           vol_surface_graph=html_graph)

if __name__ == '__main__':
    app.run(debug=True)
