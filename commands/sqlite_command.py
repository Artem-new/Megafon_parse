import sqlite3


traffic_infomation = []


def creata_table():
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


def take_information():
    connection = sqlite3.connect('Megafon')
    coursor_connection = connection.cursor()
    coursor_connection.execute("""
                                  SELECT last_reaffic FROM Last_info 
                                """)
    traffic_infomation.append(coursor_connection.fetchall())
