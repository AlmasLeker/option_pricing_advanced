# models.py

# Black-Scholes model for option pricing

def black_scholes(S, K, T, r, sigma):
    import numpy as np
    from scipy.stats import norm
    
    # Calculate d1 and d2
    d1 = (np.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Calculate call and put prices
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    return call_price, put_price


# Greeks calculations

def calculate_greeks(S, K, T, r, sigma):
    import numpy as np
    from scipy.stats import norm
    
    call_price, put_price = black_scholes(S, K, T, r, sigma)
    d1 = (np.log(S / K) + (r + (sigma ** 2) / 2) * T) / (sigma * np.sqrt(T))
    
    # Delta
    delta_call = norm.cdf(d1)
    delta_put = norm.cdf(d1) - 1
    
    # Gamma
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    
    # Theta
    theta_call = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d1))
    theta_put = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d1))
    
    # Vega
    vega = S * norm.pdf(d1) * np.sqrt(T)
    
    return (delta_call, delta_put, gamma, theta_call, theta_put, vega)