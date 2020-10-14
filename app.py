import time
import datetime
import pymysql
from flask_bootstrap import Bootstrap
from flask import Flask, render_template

from db import Runtime

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():

    items = Runtime.select()
    for item in items:
        item.is_add = item.run_time.hour > 18
    return render_template('hello.html', items=items)


if __name__ == '__main__':
    app.debug = True
    app.run()
