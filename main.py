import telebot
from random import randint

from config import token

bot = telebot.TeleBot(token)
gtn_started = 0
num = 0

class Computer:
    processor = ""
    video_card = ""
    ram = ""
    motherboard = ""
    display = ""
    os = ""

    def on(self):
        return 'on'

    def off(self):
        return 'off'

    def info(self):
        return f'''Processor: {self.processor}
        Video card: {self.video_card}
        RAM: {self.ram}
        Motherboard:{self.motherboard}
        Display:{self.display}
        OS:{self.os}'''

PC = Computer()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
    
@bot.message_handler(commands=['guess_the_number'])
def guess_the_number(message):
    global gtn_started, num
    bot.send_message(message.chat.id,'Угадай число от 1 до 100.')
    gtn_started = 1
    num = randint(0,100)

@bot.message_handler(commands=['newPC'])
def guess_the_number(message):
    PC = Computer()
    bot.send_message(message.chat.id,'Обнуление произошло успешно!')

@bot.message_handler(commands=['help'])
def guess_the_number(message):
    bot.send_message(message.chat.id,'''Команды:
                                        /guess_the_number - игра "Угадай число"
                                        /newPC - обнуление класса
                                        /PC - изменение класса''')

@bot.message_handler(commands=['PC'])
def guess_the_number(message):
    arg = telebot.util.extract_arguments(message.text)
    arg_s = arg.split(' ')
    print(arg_s)
    if len(arg_s) >= 1:
        PC.processor = arg_s[0]
    elif len(arg_s) >= 2:
        PC.ram = arg_s[1]
    elif len(arg_s) >= 3:
        PC.video_card = arg_s[2]
    elif len(arg_s) >= 4:
        PC.display = arg_s[3]
    elif len(arg_s) >= 5:
        PC.os = arg_s[4]
    elif len(arg_s) >= 6:
        PC.motherboard = arg_s[5]
    elif len(arg_s) >= 7 and arg_s[6] == 'True':
        bot.send_message(message.chat.id,PC.info()) 
    elif len(arg_s) >= 8 and arg_s[7] == 'True':
        bot.send_message(message.chat.id,PC.off()) 
    elif len(arg_s) >= 9 and arg_s[8] == 'True':
        bot.send_message(message.chat.id,PC.on()) 

    bot.send_message(message.chat.id,'Изменение произошло успешно!')
    


@bot.message_handler(content_types=['text'])
def echo_message(message):
    global gtn_started,num
    if gtn_started == 1:
        if message.text.lower() == 'да':
            guess_the_number(message)

        elif message.text.lower() == 'нет':
            gtn_started = 0
            bot.send_message(message.chat.id,'Возвращайтесь в следующий раз!')
        else:
            try:
                number = int(message.text)
            except:
                bot.send_message(message.chat.id,"Простите, но это не число. Введите число от 1 до 100")
            if number > 100:
                bot.send_message(message.chat.id,"Простите, но это число больше 100. Введите число от 1 до 100")

            elif number < 1:
                bot.send_message(message.chat.id,"Простите, но это число меньше 1. Введите число от 1 до 100")    
            else: 
                if number > num:
                    bot.send_message(message.chat.id,"Меньше")

                elif number < num:
                    bot.send_message(message.chat.id,"Больше")
                
                else:
                    bot.send_message(message.chat.id,"Вы угадали число! Сыгрем еще раз?")

    else: bot.reply_to(message, message.text)

bot.infinity_polling()