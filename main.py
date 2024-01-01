#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def index():
    #return 'Hello World , This is my first Application'
#if __name__ == '__main__':
      #app.run(host='0.0.0.0', port=8080)

import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world!! I hope you liked it"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
