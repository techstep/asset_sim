from flask import Flask, request, render_template, jsonify
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
import numpy as np
import asset_sim

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
    return jsonify(asset_sim.wiener(sample))

if __name__ == '__main__':
    manager.run()
