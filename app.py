from flask import Flask, request, render_template, jsonify
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
import numpy as np

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ua')
def ua():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/asset_sim/api/v1.0/random/', defaults={'draws': 10})
@app.route('/asset_sim/api/v1.0/random/<int:draws>', methods=["GET"])
def random_nums(draws):
    """
    Generates an arbitrary number of IID draws from the standard normal
    distibution and returns them as a JSON object.
    """
    return jsonify(dict(enumerate(np.random.standard_normal(draws))))


@app.route('/asset_sim/api/v1.0/wiener', defaults={'sample': 100})
@app.route('/asset_sim/api/v1.0/wiener/<int:sample>', methods=["GET"])
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

    return(jsonify(dict(enumerate(W))))

if __name__ == '__main__':
    manager.run()
