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


@app.route('/asset_sim/api/v1.0/random', methods=["GET"])
def random_nums():
    """
    Generates 200 draws from the standard normal and returns them
    as a JSON object.
    """
    return jsonify(dict(enumerate(np.random.standard_normal(200))))


if __name__ == '__main__':
    manager.run()
