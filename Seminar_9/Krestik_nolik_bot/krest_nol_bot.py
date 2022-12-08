import telebot
from random import randint

API_TOKEN='1150291434:AAHRRnZjBJcRiSGD4yBE7DWrdHFLaOZfcLY'

bot = telebot.TeleBot(API_TOKEN)



board = []



@bot.message_handler(commands=['start'])
def start_message(message):
    global board
    board = list(range(1,10))
    for i in range(3):
        bot.send_message(message.chat.id, (f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |'))

@bot.message_handler(commands=['hod'])
def hod_message(message):
    prov = 0
    win = 0
    chet = 0
    global board
    


    while True:
            player_answer = message.text.split()[1:]
            prov = 0
            if player_answer[0].isdigit() == True:
                pl = int(player_answer[0])
        
                if pl >= 1 and pl <= 9:
                    if(str(board[pl-1]) not in "XO"):
                        board[pl-1] = 'X'
                        chet = chet + 1
                        break
                    else:
                        bot.send_message(message.chat.id,"Эта клетка уже занята! Введите команду заново")
                        prov = 1
                        break
                else:
                    bot.send_message(message.chat.id,"Некорректный ввод. Введите число от 1 до 9. Введите команду заново")
                    prov = 1
                    break
            else:
                bot.send_message(message.chat.id,"Некорректный ввод. Введите число от 1 до 9. Введите команду заново")
                prov = 1
                break
     
    if chet == 9:
        bot.send_message(message.chat.id,"Игра закончена")
        return   


    for i in range(3):
        bot.send_message(message.chat.id, (f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |'))

    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          bot.send_message(message.chat.id,"Игра закончилась, победил игрок")
          win = 1


    if win == 1:
        return
    if prov == 0:
        while True:
            answer = int(randint(1, 9))
            if(str(board[answer-1]) not in "XO"):
                board[answer-1] = 'O'
                bot.send_message(message.chat.id,"ИИ сделал ход")
                chet = chet + 1
                break
    
    if chet == 9:
        bot.send_message(message.chat.id,"Игра закончена")
        return   

    
    if prov == 0:
        for i in range(3):
            bot.send_message(message.chat.id, (f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |'))



    
    for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          bot.send_message(message.chat.id,"Игра закончилась, победил ИИ")
          



bot.polling()