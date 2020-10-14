import datetime

from peewee import *


class Runtime(Model):
    run_date = DateField()
    run_time = TimeField()

    class Meta:
        setting = {'host': 'localhost', 'user': 'root', 'password': 'rootroot', 'database': 'worktime'}
        database = MySQLDatabase(**setting)
        # database = SqliteDatabase('my_app.db')
    # def set_database(self):
    #     self._meta.database = SqliteDatabase('new_app.db')


if __name__ == '__main__':
    all = Runtime.select()
    for item in all:
        item.is_add = item.run_time > datetime.time(hour=17, minute=30)
        print(item.is_add)
    print(all)
