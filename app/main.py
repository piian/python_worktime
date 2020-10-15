import time

import pymysql


def log_time():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "rootroot", "worktime")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    cursor.execute("select * from runtime where run_date = current_date()")
    result = cursor.fetchone()

    if result is not None:
        sql = "update runtime set run_time=current_time() where id = %d" % result[0]
    else:
        sql = "insert into runtime (`run_date`, `run_time`) values (current_date(), current_time())"

    cursor.execute(sql)
    db.commit()
    db.close()


if __name__ == '__main__':
    log_time()
