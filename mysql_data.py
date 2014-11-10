import mysql.connector
import mysql.connector.pooling
from mysql.connector import cursor
import json


class MySQLData:
    # =====================================
    # подключаемся к БД
    # =====================================
    def __init__(self, host, uid, pwd, db):
        db_config = {"host": host, "user": uid, "password": pwd, "database": db}
        self.conn = mysql.connector.connect(pool_name="db_pool", pool_size=5, **db_config)

    # =====================================
    # конструктор запросов
    # =====================================
    def query_constructor(self, key, value):
        if key == "all":
            query = "select * from maindb order by id"
        if key == "phone":
            query = "select * from maindb where phone like '%" + str(value) + "%' order by id"
        return query

    # =====================================
    # получаем json строку из курсора MySQL
    # =====================================
    def cursor_to_json(self, _cursor):
        _result = [dict(line) for line in [zip([column[0] for column in _cursor.description], row) for row in _cursor.fetchall()]]
        return json.dumps(_result, ensure_ascii=False)

    # =====================================
    # получаем данные по запросу
    # =====================================
    def get_data_by_query(self, key, value):
        db_cursor = self.conn.cursor()
        db_cursor.execute(self.query_constructor(key, value))
        json_result = self.cursor_to_json(db_cursor)
        db_cursor.close()
        return json_result

    # =====================================
    # закрываем соединение
    # =====================================
    # def disconnect_from_db(self):
    # self.conn.close()

    # @staticmethod
    # def insert_data(conn):
    #     db_cursor = conn.cursor()
    #     db_cursor.execute("insert into test(name, phone, who) values('John Doe', '123-456-789', 'Python')")
    #     db_cursor.close()
    #     return ""
