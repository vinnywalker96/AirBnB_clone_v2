#!/usr/bin/python3
"""Starts a Flask web App

The application listens on 0.0.0.0, port 5000.
Routes:
        the list of all State objects present in DBStorage sorted by name
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Return Number: n"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', state=sorted_states)

@app.teardown_appcontext
def close_session():
    """Close database connection"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
