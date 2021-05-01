#!/usr/bin/python3
""" script that starts a Flask web application
on port 5000 and displays Hello HBNB """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def HelloHBNB():
    """ HelloHBNB method

    Returns:
        str: returns Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ HBNB method

    Returns:
        str: returns 'HBNB'
    """
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
