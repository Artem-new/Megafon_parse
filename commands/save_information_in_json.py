import json
from datetime import date
from information.numerlist import numbers


def save_to_json(information):
    import os.path
    if os.path.exists(r'traffic_info.json'):
        with open('traffic_info.json', encoding='utf8') as file:
            data = json.load(file)
            for key in data:
                if key[-1:] != date.today():
                    data.append(information)
                    with open('traffic_info.json', 'a', encoding='utf8') as outfile:  # Открываем файл для записи
                        json.dump(information, outfile, indent=4)
                        outfile.write('\n')
                else:
                    data[1][f'{numbers[0]}'] = float(data[1][f'{numbers[0]}']) + float(information[1][f'{numbers[0]}'])
                    with open('traffic_info.json', 'w', encoding='utf8') as outfile:  # Открываем файл для записи
                        json.dump(data, outfile, indent=4)


    else:
        with open('traffic_info.json', 'w', encoding='utf8') as outfile:  # Открываем файл для записи
            json.dump(information, outfile, indent=4)
# ensure_ascii=False,
