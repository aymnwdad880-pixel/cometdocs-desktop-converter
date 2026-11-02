# build 3a478aaaa5
# (auto) 48b8fb
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
