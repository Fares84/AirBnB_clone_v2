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


@app.route('/hbnb_filters', strict_slashes=False)
def DisplayFilters():
    """ state and cities by state

    Returns:
        html: fetches html page
    """
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
