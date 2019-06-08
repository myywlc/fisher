"""
  Created by lin at 2019-06-08
"""

from flask import Flask, make_response

app = Flask(__name__)

app.config.from_object('config')


@app.route('/hello')
def hello():
    return '<div style="color: red">lin</div>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=app.config['DEBUG'])
