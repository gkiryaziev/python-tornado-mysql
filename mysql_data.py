import mysql.connector
from mysql.connector import cursor
import json


class MySQLData:
    pass

    conn = None

    def connect_to_db(self, host, uid, pwd, db):
        self.conn = mysql.connector.connect(host=host, user=uid, password=pwd, database=db)

    def disconnect_from_db(self):
        self.conn.close()

    #=====================================
    # получаем всех жильцов
    #=====================================
    def get_all_data(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)

        query_result = [dict(line) for line in [zip([column[0] for column in cursor.description], row) for row in
                                                cursor.fetchall()]]
        cursor.close()
        return query_result

    #=====================================
    # получаем жильца по номеру телефона
    #=====================================
    def get_data_by_phone(self, phone):
        cursor = self.conn.cursor()
        cursor.execute("select * from maindb where phone = '" + str(phone) + "'")

        query_result = [dict(line) for line in [zip([column[0] for column in cursor.description], row) for row in
                                                cursor.fetchall()]]
        cursor.close()
        return json.dumps(query_result, ensure_ascii=False)