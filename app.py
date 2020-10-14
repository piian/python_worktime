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
    db = pymysql.connect("localhost", "root", "rootroot", "worktime")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from runtime")
    results = cursor.fetchall()
    items = []
    print(results)

    for row in results:
        item = {
            'id': row[0],
            'run_date': row[1],
            'run_time': row[2],
            # 比较时间,是否大于17:30
            'is_add': row[2] > datetime.timedelta(hours=17, minutes=30)
        }
        items.append(item)
    #     打印结果
        # print("fname=%s,lname=%s" % (fname, lname))
    # 提交到数据库执行
    # 关闭数据库连接
    db.close()
    print(items)
    return render_template('hello.html', items=items)
    # return 'Hello, World!'


if __name__ == '__main__':
    app.debug = True
    app.run()
