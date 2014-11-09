import mysql.connector
import mysql.connector.pooling
from mysql.connector import cursor
import json


class MySQLData:
    # =====================================
    # получаем соединение
    # =====================================
    @staticmethod
    def connect_to_db(host, uid, pwd, db):
        db_config = {"host": host, "user": uid, "password": pwd, "database": db, "connection_timeout": 60}
        conn_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="db_pool", pool_size=20, **db_config)
        return conn_pool

    # =====================================
    # закрываем соединение
    # =====================================
    # def disconnect_from_db(self):
    # self.conn.close()

    # =====================================
    # получаем всех жильцов
    # =====================================
    @staticmethod
    def get_all_data(conn):
        db_cursor = conn.cursor()
        db_cursor.execute("select * from maindb")

        query_result = [dict(line) for line in [zip([column[0] for column in db_cursor.description], row) for row in
                                                db_cursor.fetchall()]]
        db_cursor.close()
        return json.dumps(query_result, ensure_ascii=False)

    # =====================================
    # получаем жильца по номеру телефона
    # =====================================
    @staticmethod
    def get_data_by_phone(conn, phone):
        db_cursor = conn.cursor()
        db_cursor.execute("select * from maindb where phone = '" + str(phone) + "'")

        query_result = [dict(line) for line in [zip([column[0] for column in db_cursor.description], row) for row in
                                                db_cursor.fetchall()]]
        db_cursor.close()
        return json.dumps(query_result, ensure_ascii=False)

    @staticmethod
    def insert_data(conn):
        db_cursor = conn.cursor()
        db_cursor.execute("insert into test(name, phone, who) values('John Doe', '123-456-789', 'Python')")
        db_cursor.close()
        return ""
