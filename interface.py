from flask import Flask

API_VERSION = '0.0.1'

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

class Device(object):
    'A IOT device.'
    def __init__(self, id_number, device_type, state):
        self.id_number = id_number
        self.device_type = device_type
        self.state = state
    def id(self):
        'The unique ID number of the device.'
        return self.id_number
    def type(self):
        'The type of device.'
        return self.device_type
    def state(self):
        'The current state of the device.'
        return state
    def update(self, new_state):
        'Update the state of the device.'
        self.state = new_state

if __name__ == '__main__':
    app.run()
