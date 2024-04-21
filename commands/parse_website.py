from commands.chek_traffik import mb,gb
from commands.send_info import send_message
from commands.sqlite_command import save_information_in_the_table_about_limit, update_informatin_in_the_table_Lust_info, update_informattion_in_the_table_about_limit
from commands.sqlite_command import take_last_information_about_traffik, traffic_infomation, save_information_in_the_table
from commands.sqlite_command import lust_traffic_infomation, take_information_abut_lust_info, save_information_about_last_info
import time
import json


balance_list = []
balance_value = []
total_balance = []


def check_numbers(page_number, number_ch, driver, chat_info, chat_id):
    try:
        '''Открыть страницу'''
        driver.get(page_number)
        time.sleep(6)
        '''Получить данные страницы в обход javascriot'''
        website_info = driver.page_source
        '''Найти и получить json файл, способ: поиск id элементов фигурной скобки(открытие и закрытие),
        получаем в этом промежуте данные и привеодим данные в json объект'''
        try:
            clear_first_element = website_info.find("{")
            clear_last_element = website_info.rfind("}")
            info_about_number = website_info[clear_first_element:clear_last_element + 1]
        except Exception as ex:
            print(ex)
        json_info_number = json.loads(info_about_number)
        with open('traffic_info.json', 'w', encoding='utf-8') as outfile:  # Открываем файл для записи
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
                ''' Проверяем пустое ли значение в таблицах'''
                try:
                    """Проверим лимит трафика"""
                    take_last_information_about_traffik(number_ch)
                    if float(traffic_infomation[0]) != float(total_traffic_value):
                        update_informattion_in_the_table_about_limit(number_ch, total_traffic_value, traffic_unit)
                        take_information_abut_lust_info(number_ch)
                        update_informatin_in_the_table_Lust_info(number_ch, traffic_value, traffic_unit)
                        take_information_abut_lust_info(number_ch)
                        used_traffic_new = float(total_traffic_value) - float(lust_traffic_infomation[0])
                        save_information_in_the_table(number_ch, used_traffic_new, traffic_unit)
                    else:
                        take_information_abut_lust_info(number_ch)
                        """
                        Записываем условие сохранения испоьльзованного траффика если предудущее значение меньше текщего, то
                        вычитаем лимит из текущего значения трафика 
                        """
                        if float(lust_traffic_infomation[0]) >= float(traffic_value):
                            used_traffic_last = float(traffic_value)-float(lust_traffic_infomation[0])
                            save_information_in_the_table(number_ch, used_traffic_last, traffic_unit)
                            update_informatin_in_the_table_Lust_info(number_ch, traffic_value, traffic_unit)
                        else:
                            used_traffic_new = float(total_traffic_value) - float(lust_traffic_infomation[0])
                            save_information_in_the_table(number_ch, used_traffic_new, traffic_unit)
                            update_informatin_in_the_table_Lust_info(number_ch, traffic_value, traffic_unit)

                except Exception:
                    """Если значение пустое сохраняем данные как первое значение"""
                    save_information_in_the_table(number_ch, float(0), traffic_unit)
                    save_information_in_the_table_about_limit(number_ch, float(total_balance[0]),total_balance[1])
                    save_information_about_last_info(number_ch, float(balance_value[1]), traffic_unit)

                if traffic_unit == 'Гб.':
                    gb(traffic_value, chat_info, number_ch, traffic_unit)
                else:
                    mb(traffic_value, chat_info, number_ch, traffic_unit)
        balance_list.clear()
        balance_value.clear()
        total_balance.clear()
        traffic_infomation.clear()
        lust_traffic_infomation.clear()

    except Exception as ex:
        print(ex)
        balance_list.clear()
        balance_value.clear()
        total_balance.clear()
        traffic_infomation.clear()
        lust_traffic_infomation.clear()
        send_message(chat_id, "Структура не доступна или поменялась")

