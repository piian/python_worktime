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
