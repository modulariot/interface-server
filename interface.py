import json
from flask import Flask

API_VERSION = '0.0.1'

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

class DeviceType(object):
    'An enum of device types.'
    Switch, Radio, Select, Knob = range(4)

class Device(object):
    'A IOT device.'
    def __init__(self, id_number, device_type, state):
        self.id_number = id_number
        self.device_type = device_type
        self._state = state
    def id(self):
        'The unique ID number of the device.'
        return self.id_number
    def type(self):
        'The type of device.'
        return self.device_type
    def state(self):
        'The current state of the device.'
        return self._state
    def update(self, new_state):
        'Update the state of the device.'
        self._state = new_state

def serialize_device(device):
    'Convert a device object into JSON.'
    return json.dumps({
        'id' : device.id(),
        'type' : device.type(),
        'state' : device.state()
    })

def deserialize_device(text):
    'Convert JSON into a device object.'
    table = json.loads(text)
    return Device(table['id'],
                  table['type'],
                  table['state'])

DEVICES = [
    Device(0, DeviceType.Switch, 0),
    Device(1, DeviceType.Switch, 1),
]

@app.route('/api/<version>/devices', methods = ['GET'])
def list_devices(version):
    'Return a JSON list of all device objects.'
    return json.dumps([json.loads(serialize_device(device))
                       for device in DEVICES])

@app.route('/api/<version>/devices/<int:id_number>', methods = ['GET'])
def get_device(version, id_number):
    'Return the device with the given ID number.'
    for device in DEVICES:
        if device.id() == id_number:
            return serialize_device(device)
    return json.dumps({
        'error' : 'id',
        'message' : 'There was no device with the given ID.',
    })

@app.route('/api/<version>/devices/<int:id_number>', methods = ['POST'])
def update_device(version, id_number):
    'Update the state of the device with the given ID number.'
    for device in DEVICES:
        if device.id() == id_number:
            if device.state() == DeviceType.Switch:
                if new_state in ('ON', 'OFF'):
                    device.update(new_state == 'ON')
                    return '' #needs to return OKAY
                else:
                    return json.dumps({
                        'error' : 'state',
                        'message' : 'Switches must be \'ON\' or \'OFF\', but state was \'%s\'.' % (new_state,),
                    })
            elif device.state() == DeviceType.Radio:
                pass
            elif device.state() == DeviceType.Select:
                pass
            elif device.state() == DeviceType.Knob:

if __name__ == '__main__':
    app.run()
