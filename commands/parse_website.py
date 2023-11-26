from commands.chek_traffik import mb,gb
from commands.send_info import send_message
from commands.sqlite_command import load_information_about_traffic_limit, information_about_limit_traffic, save_information_in_the_table_about_limit, update_informatin_in_the_table_Lust_info
from commands.sqlite_command import take_last_information_about_traffik, traffic_infomation, save_information_in_the_table, save_information_in_the_table_about_limit

import time
import json


balance_list = []
balance_value = []
total_balance = []


def check_numbers(page_number, number_ch, driver, chat_info, chat_id):
    try:
        '''Открыть страницу'''
        driver.get(page_number)
        time.sleep(4)
        '''Получить данные страницы в обход javascriot'''
        website_info = driver.page_source
        '''Найти и получить json файл, способ: поиск id элементов фигурной скобки(открытие и закрытие),
        получаем в этом промежуте данные и привеодим данные в json объект'''
        clear_first_element = website_info.find("{")
        clear_last_element = website_info.rfind("}")
        info_about_number = website_info[clear_first_element:clear_last_element + 1]
        json_info_number = json.loads(info_about_number)
        with open('traffic_info.json', 'w', encoding='utf8') as outfile:  # Открываем файл для записи
            json.dump(json_info_number, outfile, indent=4)
        """Ищем данные в json файле, количество оставшегося трафика по имени предоставляемых
        услуг, убежадемся что трафик считается в Гб, на этой основе проверяем оставшийся лимит трафика"""
        for info in json_info_number['data']['discounts']:
            if info['label'] == 'Интернет по России':
                '''Получаем значение текущего трафика'''
                traffic_value = info['value']
                traffic_unit = info['unit']
                '''Проверяем лимит трафика'''
                total_traffic_value = info['valueTotal']
                total_traffic_unit = info['unitTotal']
                balance_list.append(f"{number_ch} - {traffic_value} {traffic_unit}")
                balance_value.append(f"{number_ch}")
                balance_value.append(f"{traffic_value}")
                total_balance.append(f"{total_traffic_value}")
                total_balance.append(f"{total_traffic_unit}")
                '''Загружаем информацию о лимите траффика и если таблица не заполнена, записываем данные'''
                try:
                    load_information_about_traffic_limit(number_ch)
                except Exception as exit:
                    print(exit)
                    save_information_in_the_table_about_limit(number_ch, total_traffic_value, total_traffic_unit)
                '''Проверяем что последня информация о лимите траффика равна предыдущему'''
                if float(information_about_limit_traffic[0]) != total_traffic_value:
                    update_informatin_in_the_table_Lust_info(number_ch, total_traffic_value)
                else:
                    ''' Проверяем пустое ли значение в таблах'''
                    try:
                        take_last_information_about_traffik(number_ch)
                        print(traffic_infomation)
                    # Если значение пустое сохраняем данные как первое значение
                    except Exception as ex:
                        save_information_in_the_table(number_ch, 0)

                if traffic_unit == 'Гб.':
                    gb(traffic_value, chat_info, number_ch, traffic_unit)
                else:
                    mb(traffic_value, chat_info, number_ch, traffic_unit)

    except Exception as ex:
        print(ex)
        send_message(chat_id, "Структура не доступна или поменялась")