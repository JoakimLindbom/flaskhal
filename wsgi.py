from flask import Flask
from flask_hal import HAL, document

import time

start_time = None
app = Flask(__name__)
HAL(app)  # Initialise HAL


@app.route('/hello')
@app.route('/')
def hello():
    return document.Document(data={
        'message': 'Hello World'
    })

@app.route("/probe")
def probe():
    return document.Document(data={
        'message': 'I\'m alive',
        'since': '{}'.format(start_time)
    })

if __name__ == "__main__":
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    app.run()
