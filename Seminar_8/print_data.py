import baza
import dictionary

def print_user(key):
    data = baza.read_bd()
    sex = dictionary.sex_sl()
    print(f'\n','Фио: ', key, '\n', 'Пол: ', sex[data[key]['sex']], '\n','День рождения:', data[key]['birday'], '\n', 'Телефон: ', data[key]['phone'], '\n', 'Заработная плата: ', data[key]['salary'], '\n')
