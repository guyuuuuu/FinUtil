import numpy as np

def EuroCall(S: float, K: float, T: float, sigma: float, r: float, N:int, y: float = 0, t: float = 0) -> float:
    '''
    S: Currunt Stock Price
    K: Strike Price
    T: Maturity Day, measured in years
    sigma: Volatility, measured in precentage/100
    r: risk-free rate, measured in precentage/100
    N: Number of Simulation
    y: Dividend Yield Rate (Continues), default to be zero
    t: Current Time, default to be zero

    Example:
    EuroCall(80, 50, 1, 0.2, 0.05, 1000000)
    Option Pricing for a call mature in 1 year with no dividend yield,
    strike price 50, currunt price 80, volatility at 20% and risk-free rate at 5%
    '''
    normals = np.random.randn(N)
    S_T = (S * np.exp((r - y - (sigma ** 2) / 2) * (T - t) + sigma * (T ** 0.5) * normals)) - K
    S_T = np.exp(-r * (T - t)) * np.where(S_T < 0, 0, S_T)
    c = np.mean(S_T)
    return c

def BinaryCall(Q: float, S: float, K: float, T: float, sigma: float, r: float, N:int, y: float = 0, t: float = 0) -> float:
    '''
    Q: Payoff of the call
    S: Currunt Stock Price
    K: Strike Price
    T: Maturity Day, measured in years
    sigma: Volatility, measured in precentage/100
    r: risk-free rate, measured in precentage/100
    N: Number of Simulation
    y: Dividend Yield Rate (Continues), default to be zero
    t: Current Time, default to be zero

    Example:
    BinaryCall(1, 80, 50, 1, 0.2, 0.05, 1000000)
    Binary Call with payoff 1, mature in 1 year with no dividend yield,
    strike price 50, currunt price 80, volatility at 20% and risk-free rate at 5%
    '''
    normals = np.random.randn(N)
    S_T = (S * np.exp((r - y - (sigma ** 2) / 2) * (T - t) + sigma * (T ** 0.5) * normals)) - K
    S_T = np.exp(-r * (T - t)) * np.where(S_T < 0, 0, Q)
    c = np.mean(S_T)
    return c