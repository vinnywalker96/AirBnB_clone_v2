from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """Retrieves state in db"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda  state: state.name)
    return render_template("7-states_list.html", states=sorted_states);
 

@app.teardown_appcontext
def close_session(exception=None):
    """Closes database session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
