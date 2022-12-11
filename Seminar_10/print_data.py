import baza
import dictionary

def print_user(key):
    data = baza.read_bd()
    sex = dictionary.sex_sl()
    data_txt = 'ФИО: ' + str(key) + '\n' + 'Пол: ' + sex[data[key]['sex']] + '\n' + 'День рождения: ' + str(data[key]['birday']) + '\n' + 'Телефон: ' + str(data[key]['phone']) + '\n' + 'Заработная плата: ' + str(data[key]['salary'])
    return(data_txt)
    