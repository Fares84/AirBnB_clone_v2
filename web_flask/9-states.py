#!/usr/bin/python3
""" script that starts a Flask web application
on port 5000 and displays Hello HBNB """
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ closing Session """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def StatesById(id):
    """ cities by state method

    returns:
        html: fetches html page
    """
    states = storage.all("State")
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', state=state, mode='id')
    else:
        return render_template('9-states.html', states=states, mode='not')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
