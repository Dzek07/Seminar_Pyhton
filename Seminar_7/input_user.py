import logging

def input_data():
    user_input = input('Введите вырожение: ')
    logging.addlog(user_input)
    return user_input

def menu_input():
    data = input('Введите команду: ')
    logging.addlog(data)
    return data

