# Asset Simulation Project 
Attempt at developing an asset price simulator/API in Python

I want to learn to create APIs for data, that I can use to display said data on a website.

Nothing here is to simulate real stock or asset pricing activity, except perhaps in the broadest statistical sense.

Currently, the API does the following:
* Generates IID draws from a standard normal distribution
* Generates samples of a Wiener process (i.e. standard Brownian motion)
* Generates sample paths for geometric Brownian motion

What it doesn't do:
* Streams the data to the client
* Allow for all parameters to be manipulated in the API

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

To use it:

```bash
python app.py runserver
```

By default, the APIs can be reached at [http://localhost:5000/] (http://localhost:5000/).

The following URLs work:
* [/asset_sim/api/v1.0/random] (/asset_sim/api/v1.0/random) for random number generation, with 10 draws by default;
* [/asset_sim/api/v1.0/wiener] (/asset_sim/api/v1.0/wiener) for Wiener process/standard Brownian, 100 draws by default;
* [/asset_sim/api/v1.0/gbm] (/asset_sim/api/v1.0/gbm) for geometric Brownian motion, 100 draws and an initial value of 100 by default.

