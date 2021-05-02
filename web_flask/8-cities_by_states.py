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


@app.route('/cities_by_states', strict_slashes=False)
def DisplayCitiesByStates():
    """ statelist method

    Returns:
        html: fetches html page
    """
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
