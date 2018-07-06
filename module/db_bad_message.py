import sqlite3


class DBBadMessages:
    db_name = "db_bad_messages.db"
    table = "messages"

    def __init__(self):
        self.conn = sqlite3.connect(self.db_name)
        sql = "create table if not exists " + self.table + "(word text unique);"
        self.exec_sql(sql)
        self.conn.commit()

    def add(self, message):
        sql = "insert into " + self.table + " values ({})".format(message)
        try:
            self.exec_sql(sql)
        except sqlite3.Error as error:
            pass
        self.conn.commit()
        pass

    def is_word_bad(self, message):
        cursor = self.get_cursor()
        sql = "select * from " + self.table + " where word = " + message
        cursor.execute(sql)
        """cursor.fetchall()"""
        pass

    def remove(self, message):
        pass

    def get_cursor(self):
        return self.conn.cursor()

    def exec_sql(self, sql):
        cursor = self.get_cursor()
        cursor.execute(sql)
        cursor.close()
