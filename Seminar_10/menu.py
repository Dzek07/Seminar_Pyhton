import telebot
import baza
import dictionary
import print_data

API_TOKEN='1150291434:AAHRRnZjBJcRiSGD4yBE7DWrdHFLaOZfcLY'

bot = telebot.TeleBot(API_TOKEN)

data = {}
sex = dictionary.sex_sl()

@bot.message_handler(commands=['start'])
def start_message(message):
    global data
    global sex
    data = baza.read_bd()
    bot.send_message(message.chat.id,"База запущена!")
    bot.send_message(message.chat.id,"/print просмотр всех сотрудников")
    bot.send_message(message.chat.id,"/find_fio Поиск сотрудника по ФИО")
    bot.send_message(message.chat.id,"/find_tel Поиск сотрудника по телефону")
    bot.send_message(message.chat.id,"/add Добавить нового сотрудника")
    bot.send_message(message.chat.id,"/del  Удалить сотрудника")
    bot.send_message(message.chat.id,"/edit_fio  Изменение ФИО")
    bot.send_message(message.chat.id,"/edit_sex  Изменить пол")
    bot.send_message(message.chat.id,"/edit_tel  Изменить телефон")
    bot.send_message(message.chat.id,"/edit_bird  Изменить дату рождения")
    bot.send_message(message.chat.id,"/edit_salary  Изменить Заработную плату")
    
@bot.message_handler(commands=['print'])
def print_message(message):
    global data
    global sex
    for key in data:
        bot.send_message(message.chat.id, print_data.print_user(key))
            
@bot.message_handler(commands=['find_fio'])
def findfio_message(message):
    global data
    global sex
    count = 0
    fio = (message.text.split()[1:])
    fio_txt = ' '.join(fio)
    for key in data:
        if fio_txt in key:
            bot.send_message(message.chat.id, print_data.print_user(key))
            count = 1
    if count == 0:
        bot.send_message(message.chat.id, 'Совпадений не найдено. Прверьте правельность введенных данных')

@bot.message_handler(commands=['find_tel'])
def findtel_message(message):
    global data
    global sex
    count = 0
    tel = message.text.split()[1:]
    tel = int(tel[0])
    for key in data:
        for i in range(len(data[key]['phone'])):
                if (data[key]['phone'])[i] == tel:
                        bot.send_message(message.chat.id, print_data.print_user(key))
                        count = 1
    if count == 0:
        bot.send_message(message.chat.id, 'Совпадений не найдено. Прверьте правельность введенных данных')

@bot.message_handler(commands=['add'])
def add_message(message):
    global data
    global sex
    str_user = message.text.split()[1:]
    fio = str(str_user[0]) + ' ' + str(str_user[1]) + ' ' + str(str_user[2])
    del str_user[0:3]
    if str(str_user[0]) == 'Мужской':
        mf = 0
    else: mf = 1
    str_user.pop(0)
    bird = str(str_user[0])
    str_user.pop(0)
    zp = int(str_user[-1])
    str_user.pop(-1)
    tel = list(map(int, str_user))
    data[fio] = {'sex':mf, 'birday':bird,'phone':tel,'salary':zp}
    baza.save_bd(data)
    bot.send_message(message.chat.id, 'Новый сотрудник добавлен')

@bot.message_handler(commands=['del'])
def del_message(message):
    global data
    global sex
    fio = (message.text.split()[1:])
    fio_txt = ' '.join(fio)
    del data[fio_txt]
    baza.save_bd(data)
    bot.send_message(message.chat.id, 'Пользователь удален')

@bot.message_handler(commands=['edit_fio'])
def editfio_message(message):
    global data
    global sex
    text = (message.text.split()[1:])
    fio = str(text[0]) + ' ' + str(text[1]) + ' ' + str(text[2])
    del text[0:3]
    new_fio = str(text[0]) + ' ' + str(text[1]) + ' ' + str(text[2])
    for key in data:
        if key == fio:
            bot.send_message(message.chat.id, 'Сотрудник найден')
            bot.send_message(message.chat.id, print_data.print_user(key))
            break
    data[new_fio] = data[key]
    del data[key]
    baza.save_bd(data)
    bot.send_message(message.chat.id, 'Пользователь изменен')
    bot.send_message(message.chat.id, print_data.print_user(new_fio))

@bot.message_handler(commands=['edit_sex'])
def editsex_message(message):
    global data
    global sex
    text = (message.text.split()[1:])
    fio = str(text[0]) + ' ' + str(text[1]) + ' ' + str(text[2])
    del text[0:3]
    new_sex = str(text[0])
    for key in data:
        if key == fio:
            bot.send_message(message.chat.id, 'Сотрудник найден')
            bot.send_message(message.chat.id, print_data.print_user(key))
            break
    if new_sex == 'мужской':
        data[key] ['sex'] = 0
    else:
        data[key] ['sex'] = 1
    baza.save_bd(data)
    bot.send_message(message.chat.id, 'Пользователь изменен')
    bot.send_message(message.chat.id, print_data.print_user(key))

@bot.message_handler(commands=['edit_tel'])
def edittel_message(message):
    global data
    global sex
    text = (message.text.split()[1:])
    fio = str(text[0]) + ' ' + str(text[1]) + ' ' + str(text[2])
    del text[0:3]
    new_tel = list(map(int, text))
    for key in data:
        if key == fio:
            bot.send_message(message.chat.id, 'Сотрудник найден')
            bot.send_message(message.chat.id, print_data.print_user(key))
            break
    data[key] ['phone'] = new_tel
    baza.save_bd(data)
    bot.send_message(message.chat.id, 'Пользователь изменен')
    bot.send_message(message.chat.id, print_data.print_user(key))

@bot.message_handler(commands=['edit_bird'])
def editbird_message(message):
    global data
    global sex
    text = (message.text.split()[1:])
    fio = str(text[0]) + ' ' + str(text[1]) + ' ' + str(text[2])
    del text[0:3]
    new_bird = str(text[0])
    for key in data:
        if key == fio:
            bot.send_message(message.chat.id, 'Сотрудник найден')
            bot.send_message(message.chat.id, print_data.print_user(key))
            break
    data[key] ['birday'] = new_bird
    baza.save_bd(data)
    bot.send_message(message.chat.id, 'Пользователь изменен')
    bot.send_message(message.chat.id, print_data.print_user(key))    

@bot.message_handler(commands=['edit_salary'])
def editsalary_message(message):
    global data
    global sex
    text = (message.text.split()[1:])
    fio = str(text[0]) + ' ' + str(text[1]) + ' ' + str(text[2])
    del text[0:3]
    new_sl = int(text[0])
    for key in data:
        if key == fio:
            bot.send_message(message.chat.id, 'Сотрудник найден')
            bot.send_message(message.chat.id, print_data.print_user(key))
            break
    data[key] ['salary'] = new_sl
    baza.save_bd(data)
    bot.send_message(message.chat.id, 'Пользователь изменен')
    bot.send_message(message.chat.id, print_data.print_user(key))  

bot.polling()

