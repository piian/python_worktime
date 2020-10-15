import datetime

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from db import Runtime

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def hello_world():
    items = Runtime.select()
    for item in items:
        # 如果5.30下班，标记一下
        item.is_add = item.run_time > datetime.time(hour=17, minute=45)
    return render_template('hello.html', items=items)


if __name__ == '__main__':
    app.debug = True
    app.run()
