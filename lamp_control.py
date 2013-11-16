import time
from itertools import cycle
from flask import Flask, render_template
from robot_brain.gpio_pin import GPIOPin

app = Flask(__name__)
on_pin = GPIOPin(18)
off_pin = GPIOPin(23)
state_cycle = cycle(['on', 'off'])

@app.route("/")
@app.route("/<state>")
def update_lamp(state=None):
    if state == 'on':
        on_pin.set(1)
        time.sleep(.2)
        on_pin.set(0)
    if state == 'off':
        off_pin.set(1)
        time.sleep(.2)
        off_pin.set(0)
    if state == 'toggle':
        state = next(state_cycle)
        update_lamp(state)
    template_data = {
        'title' : state,
    }
    return render_template('main.html', **template_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
