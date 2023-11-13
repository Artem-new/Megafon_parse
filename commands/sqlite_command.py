import sqlite3


traffic_infomation = []
information_about_limit_traffic = []

class Base:

    def connection_base(self, command):
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute(command)


    def creata_table(self):
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute("""
                                      CREATE TABLE IF NOT EXISTS Traffic_information(
                                          number text NOT NULL,
                                          traffic text NOT NULL,
                                          format text NOT NULL
                                          )
                                    """)
        coursor_connection.execute("""
                                    CREATE TABLE IF NOT EXISTS Last_info(
                                          number text NOT NULL,
                                          last_traffic text NOT NULL,
                                          format text NOT NULL
                                          )
                                    """)
        coursor_connection.execute("""
                                    CREATE TABLE IF NOT EXISTS Traffic_limit(
                                          number text NOT NULL,
                                          limits text NOT NULL,
                                          format text NOT NULL
                                          )
                                    """)
        coursor_connection.close()


    def take_information(self, numb):
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute(f"SELECT last_traffic FROM Last_info WHERE number=?", (numb))
        last_information_traffic = coursor_connection.fetchone()
        for last_trafic_info in last_information_traffic:
            traffic_infomation.append(last_trafic_info)
        coursor_connection.close()


    def save_information_in_the_table(self, numb, traffics):
        '''Сохранение информации в базу'''
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        '''Вставить в таблицу инофрмацию об использованом трафиком между предыдущими сессиями'''
        coursor_connection.execute("INSERT INTO Traffic_information (number, traffic, format) VALUES (?,?,?)",(numb, traffics, 'Гб.'))
        coursor_connection.close()

    def save_information_in_the_table_about_limit(self, numb, limit):
        '''Вставить инофрмацию олимите трафика'''
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute("INSERT INTO Traffic_limit (number, limit, format) VALUES (?,?,?)", (numb, limit, format))
        # coursor_connection.execute("INSERT INTO Last_info (number, last_traffic, format) VALUES (?,?,?)",(numb, lust_traffic, 'Гб.'))
        # coursor_connection.execute("INSERT INTO Traffic_limit (number, limits, format) VALUES (?,?,?)",(numb, limit, 'Гб.'))
        coursor_connection.close()

    def load_information_about_limit(self, numb):
        '''Получить инофрмацию о лимите траффика'''
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute(f"SELECT last_traffic FROM Last_info WHERE number=?", (numb))
        last_information_traffic = coursor_connection.fetchone()
        for last_trafic_info in last_information_traffic:
            information_about_limit_traffic.append(last_trafic_info)
        coursor_connection.close()


    def update_informatin_in_the_table_Lust_info(self, numb, lust_traffic):
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute(f'DELETE FROM Last_info WHERE number={numb}', ('newuser',))
        coursor_connection.execute(f"UPDATE Last_info SET last_traffic=? WHERE number=?",
                                   (lust_traffic, numb))
        connection.commit()
        connection.close()

