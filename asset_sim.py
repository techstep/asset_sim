import numpy as np

class GeomBrownianMotion:
    def __init__(self, s0, time, time_rate, sigma, mu):
        # s0 is the initial asset price
        self.s0 = s0
        # time is the amount of time covered
        self.time = time
        # time_rate is the number of periods in each unit of time
        # the product of time_rate and time is the number of steps
        # in the simulation
        self.time_rate = time_rate
        self.sigma = sigma
        self.mu = mu

def generate_returns(log_returns):
    """
    Given a list of log returns, give back a list of returns.
    """
    return np.exp(log_returns)

def generate_prices(params, log_returns):
    """
    Given a list of log returns, and an object of parameters, generate
    prices starting from initial value S0.
    """
    returns = generate_returns(log_returns)

    price_seq = params.s0

    for i in range(1, len(returns)):
        price_seq.append(price_seq[i-1]*returns[i-1])
    return np.array(price_seq)

