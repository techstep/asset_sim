import numpy as np


def wiener(N, T=1, mu=0, sig=1):
    """
    Generates a path of a Wiener process of size N, with drift mu and diffusion
    sig. With the default values of mu and sigma, we have *the* Wiener process
    of size N, which is characterized by the following properties:

    1)  W0 = 0;
    2)  Wt is almost surely continuous;
    3)  Wt has independent incremenets;  Wt-Ws ~ N(0, t-s), or a normal
        distribution with mean 0 and variance (t-s)^2. (When t-s=1, this
        is the same as a draw from a standard normal.)
    """
    W = np.zeros(N, np.dtype(float))

    # each timestep is 1/N units, scaled accordingly
    dt = (T/N)**(1/2)

    for i in range(1, N):
        W[i] = W[i-1] + np.random.normal(mu, sig)*dt

    return dict(enumerate(W))


def geom_bm(N, T=1, mu=0, sig=1, S0=0):
    """
    Simulates a geometric Brownian Motion of size N, which comes from the
    solution of the SDE:
        dS_t = \mu S_t dt + \sigma S_t dW_t

    which is:

        S_t = S_0 exp((\mu-\sigma^2/2)t + \sigma W_t)

    which is log-normally distributed.
    """
    dt = (T/N)**(1/2)
    t = np.linspace(0, T, N)
    W = np.cumsum(np.random.normal(size=N))*dt

    X = (mu-(sig**2)/2)*t + sig*W
    S = S0*np.exp(X)

    return dict(enumerate(S))
