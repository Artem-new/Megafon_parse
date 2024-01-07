import sqlite3
from datetime import date


traffic_infomation = []
save_information_in_the_table_about_limit = []
information_about_limit_traffic = []
time = date.today()


def connection_base(command):
    connection = sqlite3.connect('Megafon.db')
    coursor_connection = connection.cursor()
    coursor_connection.execute(command)


def creata_table():
    connection = sqlite3.connect('Megafon.db')
    coursor_connection = connection.cursor()
    coursor_connection.execute("""
                                  CREATE TABLE IF NOT EXISTS Traffic_information(
                                      date text NOT NULL,
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


def save_information_in_the_table(numb, traffics, format):
    '''Сохранение информации в базу'''
    connection = sqlite3.connect('Megafon.db')
    coursor_connection = connection.cursor()
    '''Вставить в таблицу инофрмацию об использованом трафиком между предыдущими сессиями'''
    coursor_connection.execute("INSERT INTO Traffic_information (date, number, traffic, format) VALUES (?,?,?,?)", (time, numb, traffics, format))
    connection.commit()


def take_last_information_about_traffik(numb):
    connection = sqlite3.connect('Megafon.db')
    coursor_connection = connection.cursor()
    coursor_connection.execute(f"SELECT last_traffic FROM Last_info WHERE number=?", (numb,))
    last_information_traffic = coursor_connection.fetchone()
    for last_trafic_info in last_information_traffic:
        traffic_infomation.append(last_trafic_info)

    connection.commit()


def update_information_in_the_table(numb, traffic, format):
    try:
        take_last_information_about_traffik(numb, format)
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute(f'DELETE FROM Traffic_information WHERE date=?', (time,))
        connection.commit()
        save_information_in_the_table(numb, traffic_infomation+traffic, format)
        connection.commit()
    except Exception:
        save_information_in_the_table(numb, traffic, format)


def save_information_in_the_table_about_limit(numb, limit, format):
    '''Вставить инофрмацию олимите трафика'''
    connection = sqlite3.connect('Megafon.db')
    coursor_connection = connection.cursor()
    coursor_connection.execute("INSERT INTO Traffic_limit (number, limits, format) VALUES (?,?,?)", (numb, limit, format))
    connection.commit()


def update_informattion_in_the_table_about_limit(numb, limit, format):
    try:
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute(f'DELETE FROM Traffic_limit WHERE number=?', (numb,))
        connection.commit()
        coursor_connection.execute(f"UPDATE Traffic_limit SET WHERE number=?",
                                   (numb, limit, format))
        connection.commit()
    except Exception:
        save_information_in_the_table_about_limit(numb, limit, format)


def save_information_about_last_info(numb, last_traffic, format):
    connection = sqlite3.connect('Megafon.db')
    coursor_connection = connection.cursor()
    coursor_connection.execute("INSERT INTO Last_info (number, last_traffic, format) VALUES (?,?,?)", (numb, last_traffic, format))
    connection.commit()


def update_informatin_in_the_table_Lust_info(numb, lust_traffic):
    try:
        connection = sqlite3.connect('Megafon.db')
        coursor_connection = connection.cursor()
        coursor_connection.execute(f'DELETE FROM Last_info WHERE number=?', (numb,))
        connection.commit()
        coursor_connection.execute(f"UPDATE Last_info SET WHERE number=?",
                              (lust_traffic, numb))
        connection.commit()
    except Exception:
        save_information_about_last_info(numb, lust_traffic, numb)


def load_and_save_information_about_traffic_limit(numb, limit_traffic, format):
    '''Получить инофрмацию о лимите траффика'''
    connection = sqlite3.connect('Megafon.db')
    coursor_connection = connection.cursor()
    coursor_connection.execute(f"SELECT limits FROM Traffic_limit WHERE number=?", (numb,))
    '''Получение'''
    last_information_traffic = coursor_connection.fetchone()
    for last_trafic_info in last_information_traffic:
        information_about_limit_traffic.append(last_trafic_info)
    if last_trafic_info != limit_traffic:
        update_informattion_in_the_table_about_limit(numb, limit_traffic, format)
        information_about_limit_traffic.clear()
        information_about_limit_traffic.append(limit_traffic)
    else:
        connection.commit()
