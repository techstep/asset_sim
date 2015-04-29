import numpy as np


def wiener(sample):
    """
    Generates a wiener process of size sample, which is defined by the
    following characteristics:

    1)  W0 = 0;
    2)  Wt is almost surely continuous;
    3)  Wt has independent incremenets;  Wt-Ws ~ N(0, t-s), or a normal
        distribution with mean 0 and variance (t-s)^2.
    """
    W = np.zeros(sample, np.dtype(float))

    mu, sig = 0, 1

    dt = (1/sample)**(1/2)

    for i in range(1, sample):
        W[i] = W[i-1] + np.random.normal(mu, sig)*dt

    return dict(enumerate(W))


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
