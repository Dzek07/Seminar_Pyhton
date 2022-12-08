import telebot
import log
import calculations

API_TOKEN='1150291434:AAHRRnZjBJcRiSGD4yBE7DWrdHFLaOZfcLY'

bot = telebot.TeleBot(API_TOKEN)




@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, (f'Привет {message.from_user.first_name}'))
    bot.send_message(message.chat.id, 'Поддерживаемые команды: calc, log, help, compl')
    data = message.text
    log.addlog(data)
          
@bot.message_handler(commands=['log'])
def log_message(message):
    
    bot.send_message(message.chat.id, log.read_log())
    data = message.text
    log.addlog(data)

@bot.message_handler(commands=['help'])
def help_message(message):
    
    bot.send_message(message.chat.id, '/calc - Калькулятор')
    bot.send_message(message.chat.id, '/compl - калькулятор для комплесных чисел')
    bot.send_message(message.chat.id, '/log - посмотреть log')
    bot.send_message(message.chat.id, '/help - справка')
    data = message.text
    log.addlog(data)

@bot.message_handler(commands=['compl'])
def compl_message(message):
    expression = message.text.split()[1:]
    expression_text = str(expression[0])
    bot.send_message(message.chat.id, calculations.calc_compl(expression_text))
    log.addlog(message.text)

@bot.message_handler(commands=['calc'])
def calc_message(message):
    expression = message.text.split()[1:]
    expression_text = str(expression[0])
    bot.send_message(message.chat.id, calculations.calc(expression_text))
    log.addlog(message.text)
    

bot.polling()
