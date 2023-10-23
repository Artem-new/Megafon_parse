from commands.send_info import send_message

def gb(traffic_value, chat_id, number_ch, unit):
    traffic_value_number = float(traffic_value)
    if traffic_value_number >= 2:
        print('OK')
    else:
        sending_text = f"Недостаточно или на исходе пакеты на номере: {number_ch}\n"f"Остаток по пакетам {traffic_value_number} {unit}"
        send_message(chat_id, sending_text)



def mb(traffic_value, chat_id, number_ch, unit):
        traffic_value_number = float(traffic_value)
        if traffic_value_number >= 2000:
            print('OK')
        else:
            sending_text = f"Недостаточно или на исходе пакеты на номере: {number_ch}\n"f"Остаток по пакетам {traffic_value_number} {unit}"
            send_message(chat_id, sending_text)
