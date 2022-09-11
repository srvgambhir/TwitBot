from os import environ
from flask import Flask
import clock

app = Flask(__name__)
app.run(host= '0.0.0.0', port=environ.get('PORT'))

clock.sched.start()
