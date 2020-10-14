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
    list = Runtime.select().where(Runtime.run_date == fn.CURRENT_DATE()).get()
    if list:
        Runtime.update(counter=Stat.counter + 1).where(Stat.url == request.url)
        print('有')
    else:
        print("wu")
    # for i in list:
    #     print(i)
    print(list)
    # all = Runtime.select()
    # for item in all:
    #     item.is_add = item.run_time > datetime.time(hour=17, minute=30)
    #     print(item.is_add)
    # print(all)
