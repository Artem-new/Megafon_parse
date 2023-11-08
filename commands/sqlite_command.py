import sqlite3


traffic_infomation = []

class Base:


    def connection_base(self, command):
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute(command)


    def creata_table(self):
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute("""
                                      CREATE TABLE IF MOT EXISTS Traffic_information(
                                          id integer PIMARY KEY,
                                          number text NOT NULL,
                                          traffic integer NOT NULL,
                                          format text NOT NULL
                                      );
                                      CREATE TABLE IF MOT EXISTS Last_info(
                                          id integer PIMARY KEY,
                                          last_traffic integer NOT NULL,
                                          format text NOT NULL
                                      );
                                      CREATE TABLE IF NOT EXISTS Traffic_limit(
                                          id integer PIMARY KEY,
                                          limit integer NOT NULL,
                                          format text NOT NULL
                               """)
        coursor_connection.close()


    def take_information(self):
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute("""
                                      SELECT last_traffic FROM Last_info 
                                    """)
        last_information_traffic = coursor_connection.fetchone()
        for one_info in last_information_traffic:
            traffic_infomation.append(one_info)
        coursor_connection.close()


    def save_information_in_the_table(self, numb, traffics, lust_traffic):
        connection = sqlite3.connect('Megafon')
        coursor_connection = connection.cursor()
        coursor_connection.execute("""
                                   
                                   """)
