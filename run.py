'''
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
'''
#!flask/bin/python
from app import app

app.run(host="127.0.0.1", port=5002, debug=True)
'''
leszczyna:
app.run(host="0.0.0.0", port=5002, debug=True)
standardowe:
app.run(debug=True)
'''