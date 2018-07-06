import sqlite3


class DBUsers:
    db_name = "db_users.db"
    table_name = "users"

    def __init__(self):
        self.conn = sqlite3.connect(self.db_name)
        cursor = self.conn.cursor()
        cursor.execute('create table if not exists ' + self.table_name + ' (user text unique);')
        cursor.close()
        self.conn.commit()
        pass

    def add(self, name):
        cursor = self.conn.cursor()
        try:
            cursor.execute('insert into users values ("{}")'.format(name))
        except sqlite3.Error as error:
            pass
        cursor.close()
        self.conn.commit()
        pass

    def get_users(self):
        cursor = self.conn.cursor()
        cursor.execute('select * from ' + self.table_name)
        lst = cursor.fetchall()
        cursor.close()
        print(lst)
        return lst

    def remove(self, name):
        cursor = self.conn.cursor()
        cursor.execute('delete from table ' + self.table_name + ' where user = {}'.format(name))
        cursor.close()
        pass


if __name__ == "__main__":
    db = DBUsers()
    db.get_users()
