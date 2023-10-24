import json
from datetime import date
from information.numerlist import numbers
from commands.parse_website import check_numbers, balance_list, balance_value


collect_info = []


def save_to_json(information):
    import os.path
    if os.path.exists(r'traffic_info.json'):
        with open('traffic_info.json', encoding='utf8') as file:
            data = json.load(file)
            for key in data:
                if key[-1:] != date.today():
                    difference_balance1 = key[f'{balance_list[0]}'] - information[f'{balance_list[0]}']
                    difference_balance2 = key[f'{balance_list[2]}'] - information[f'{balance_list[2]}']
                    difference_balance3 = key[f'{balance_list[4]}'] - information[f'{balance_list[4]}']
                    difference_balance4 = key[f'{balance_list[6]}'] - information[f'{balance_list[6]}']
                    if difference_balance1 > 0:
                        key[f'{balance_list[0]}'] = difference_balance1
                    else:
                        key[f'{balance_list[0]}'] = difference_balance1 + float(50) - information[f'{balance_list[0]}']
                    if difference_balance2 > 0:
                        key[f'{balance_list[2]}'] = difference_balance2
                    else:
                        key[f'{balance_list[2]}'] = difference_balance2 + float(50) - information[f'{balance_list[2]}']
                    if difference_balance3 > 0:
                        key[f'{balance_list[4]}'] = difference_balance3
                    else:
                        key[f'{balance_list[4]}'] = difference_balance1 + float(50) - information[f'{balance_list[4]}']
                    if difference_balance4 > 0:
                        key[f'{balance_list[6]}'] = difference_balance4
                    else:
                        key[f'{balance_list[6]}'] = difference_balance1 + float(50) - information[f'{balance_list[6]}']

                    with open('traffic_info.json', 'a', encoding='utf8') as outfile:  # Открываем файл для записи
                        json.dump(collect_info, outfile, indent=4)
                        outfile.write('\n')
                else:
                    data[1]['date'] = float(data[1][f'{numbers[0]}']) + float(information[1][f'{numbers[0]}'])
                    with open('traffic_info.json', 'w', encoding='utf8') as outfile:  # Открываем файл для записи
                        json.dump(data, outfile, indent=4)


    else:
        with open('traffic_info.json', 'w', encoding='utf8') as outfile:  # Открываем файл для записи
            information_parce = {"date": f"{str(date.today())}",
                                 f'{balance_value[0]}': float(0),
                                 f'{balance_value[2]}': float(0),
                                 f'{balance_value[4]}': float(0),
                                 f'{balance_value[6]}': float(0),
                                 1: float(balance_value[1]),
                                 2: float(balance_value[2]),
                                 3: float(balance_value[3]),
                                 4: float(balance_value[4])
                                 }
            json.dump(information_parce, outfile, indent=4)
# ensure_ascii=False,
