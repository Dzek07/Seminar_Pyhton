import input_user
import print_data
import calculations
import logging


def menuit():
    print('Поддерживаемые команды: calc, log, exit, help, compl')
    while True:
        
        data = input_user.menu_input()
        if data == 'calc':
            user_input = input_user.input_data()
            res = calculations.calc(user_input)
            print_data.printer(res)
        elif data == 'compl':
            user_input = input_user.input_data()
            res = calculations.calc_compl(user_input)
            print_data.printer(res)
        elif data == 'log':
            logging.read_log()
        elif data == 'exit':
            print('Приходите еще')
            break
        elif data == 'help':
            print('calc - Калькулятор')
            print('compl - калькулятор для комплесных чисел')
            print('log - посмотреть log')
            print('help - справка')
            print('exit - выход из программы')
        else:
            print('Нераспознаная команда')
            print('Наберите help')
