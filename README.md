# Asset Simulation Project 
Attempt at developing an asset price simulator/API in Python

I want to learn to create APIs for data, that I can use to display said data on a website.

Nothing here is to simulate real stock or asset pricing activity, except perhaps in the broadest statistical sense.

Currently, the API does the following:
* Generates IID draws from a standard normal distribution
* Generates samples of a Wiener process (i.e. standard Brownian motion)

What it doesn't do:
* Generates sample paths for geometric Brownian motion
* Stream the data to the client

# Installation

First, create a virtualenv:

```bash
virtualenv --python=python3.4 ~/asset_sim_env
```

Then, start the virtualenv:

```bash
source ~/asset_sim_env/bin/activate
```

Then, install the Python modules:

```bash
cd asset_sim/reqs
pip install -r requirements.txt
```

