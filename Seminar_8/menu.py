import baza
import input_user
import dictionary
import print_data

def menu_bd():
    data = baza.read_bd()
    print('База запущена')
    sex = dictionary.sex_sl()
    while True:
        print('Нажмите 1 просмотр всех сотрудников', '\n', 'Нажмите 2 Добавить нового сотрудника', '\n', 'Нажмите 3 Удаление сотрудника','\n', 'Нажмите 4 Редактирование сотрудника','\n', 'Нажмите 5 Поиск сотрудника','\n', 'Нажмите 0 Выход')
        data_user = input_user.input_menu()
        if data_user == '1':
            for key in data:
                print_data.print_user(key)
        elif data_user == '2':
            fio = input('Введите ФИО:')
            s = input('Введите пол:')
            bd = input('Введите день рождения:')
            tel = input('Введите телефоны через пробел:')
            tel_sp = list(map(int, tel.split()))
            zp = int(input('Введите заработную плату:'))
            if s == 'Мужской':
                s = 0
            else:
                s = 1
            data[fio] = {'sex':s, 'birday':bd,'phone':tel_sp,'salary':zp}
            baza.save_bd(data)
        elif data_user == '3':
            dl = input('Введите ФИО: ')
            del data[dl]
            baza.save_bd(data)
        elif data_user == '4':
            fio = input('Введите ФИО сотрудника для редактирования: ')
            for key in data:
                if key == fio:
                    print_data.print_user(key)
                    break
            print('Введите что необходимо поменять:','\n', 'Нажмите 1 Изменить ФИО', '\n', 'Нажмите 2 Изменить пол','\n', 'Нажмите 3 Изменить телефон','\n', 'Нажмите 4 Изменить день рождения', '\n', 'Нажмите 5 Изменить заработную плату')
            red = input_user.input_menu()
            if red == '1':
                print('Прежнее ФИО: ', key)
                new = input('Введите новое ФИО: ')
                data[new] = data[key]
                del data[key]
            elif red == '2':
                print('Прежний пол: ', sex[data[key] ['sex']])
                new = input('Введите новый пол: ')
                if new == 'мужской':
                    data[key] ['sex'] = 0
                else:
                    data[key] ['sex'] = 1
            elif red == '3':
                print('Прежние телефоны: ', data[key] ['phone'])
                new = input('Введите новые телефоны: ')
                new_tel = list(map(int, new.split()))
                data[key] ['phone'] = new_tel
            elif red == '4':
                print('Прежняя дата рождения: ', data[key] ['birday'])
                new = input('Введите новую дату рождения: ')
                data[key] ['birday'] = new
            elif red == '5':
                print('Прежняя заработная плпта: ', data[key] ['salary'])
                new = input('Введите новую заработную плпту: ')
                data[key] ['salary'] = new
            baza.save_bd(data)
        elif data_user == '5':
            print('По каким параметрам найти:','\n', 'Нажмите 1 Поиск по ФИО', '\n', 'Нажмите 2 Поиск по телефону')
            data_user = input_user.input_menu()
            if data_user == '1':
                fio = input('Введите ФИО: ')
                for key in data:
                  if key == fio:
                    print_data.print_user(key)
            elif data_user == '2':
                tel = int(input('Введите номер телефона: '))

                for key in data:
                        for i in range(len(data[key]['phone'])):
                                if (data[key]['phone'])[i] == tel:
                                        print_data.print_user(key)

            
        elif data_user == '0':
            break