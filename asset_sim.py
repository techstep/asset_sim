import numpy as np


def wiener(N, T=1, mu=0, sig=1):
    """
    Generates a path of a Wiener process of size N, which is characterized
    by the following properties:

    1)  W0 = 0;
    2)  Wt is almost surely continuous;
    3)  Wt has independent incremenets;  Wt-Ws ~ N(0, t-s), or a normal
        distribution with mean 0 and variance (t-s)^2.
    """
    W = np.zeros(N, np.dtype(float))

    # each timestep is 1/N units,
    dt = (T/N)**(1/2)

    for i in range(1, N):
        W[i] = W[i-1] + np.random.normal(mu, sig)*dt

    return dict(enumerate(W))
