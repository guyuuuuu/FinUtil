import numpy as np
from scipy.stats import norm

def EuroCall(S: float, K: float, T: float, sigma: float, r: float, y: float = 0, t: float = 0) -> float:
    '''
    S: Currunt Stock Price
    K: Strike Price
    T: Maturity Day, measured in years
    sigma: Volatility, measured in precentage/100
    r: risk-free rate, measured in precentage/100
    y: Dividend Yield Rate (Continues), default to be zero
    t: Current Time, default to be zero

    Example:
    EuroCall(80, 50, 1, 0.2, 0.05)
    Option Pricing for a call mature in 1 year with no dividend yield,
    strike price 50, currunt price 80, volatility at 20% and risk-free rate at 5%
    '''    
    d1 = (np.log(S / K) + (r - y + ((sigma ** 2) / 2) * (T- t))) / (sigma * ((T - t) ** 0.5))
    d2 = d1 - (sigma * ((T - t) ** 0.5))
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    c = S * np.exp(-y) * Nd1 - K * np.exp(-r * (T - t)) * Nd2
    return c

def BinaryCall(Q: float, S: float, K: float, T: float, sigma: float, r: float, y: float = 0, t: float = 0) -> float:
    '''
    S: Currunt Stock Price
    K: Strike Price
    T: Maturity Day, measured in years
    sigma: Volatility, measured in precentage/100
    r: risk-free rate, measured in precentage/100
    y: Dividend Yield Rate (Continues), default to be zero
    t: Current Time, default to be zero

    Example:
    BinaryCall(1, 80, 50, 1, 0.2, 0.05)
    Binary call with payoff 1, mature in 1 year with no dividend yield,
    strike price 50, currunt price 80, volatility at 20% and risk-free rate at 5%
    '''    
    d2 = (np.log(S / K) + (r - y - ((sigma ** 2) / 2) * (T- t))) / (sigma * ((T - t) ** 0.5))
    Nd2 = norm.cdf(d2)
    c = Q * np.exp(-r * (T - t)) * Nd2
    return c