from commands.chek_traffik import mb,gb
from commands.send_info import send_message
import time
import json

balance_list = []
balance_value = []


def check_numbers(page_number, number_ch, driver, chat_info, chat_id):
    try:
        '''Pages'''
        driver.get(page_number)
        time.sleep(4)
        '''Find info on page'''
        website_info = driver.page_source
        '''Find and take json file'''
        clear_first_element = website_info.find("{")
        clear_last_element = website_info.rfind("}")
        info_about_number = website_info[clear_first_element:clear_last_element + 1]
        json_info_number = json.loads(info_about_number)

        for info in json_info_number['data']['discounts']:
            if info['label'] == 'Интернет по России':
                traffic_value = info['value']
                traffic_unit = info['unit']
                balance_list.append(f"{number_ch} - {traffic_value} {traffic_unit}\n")
                balance_value.append(f"{number_ch}")
                balance_value.append(f"{traffic_value}")
                if traffic_unit == 'Гб.':
                    gb(traffic_value, chat_info, number_ch, traffic_unit)
                else:
                    mb(traffic_value, chat_info, number_ch, traffic_unit)

    except Exception as ex:
        print(ex)
        send_message(chat_id, "Структура не доступна или поменялась")