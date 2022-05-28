import telebot , time
from telebot import types 
from requests import get
import random
tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #Конвертация даты в читабельный вид
aa=random.randint(1,3)
if aa==1:
    bb='Колобок повесился'
if aa==2:
    bb='Русалка села на шпагат'
if aa==3:
    bb='Рыба потонула'
zz=random.randint(1,3)
if zz==1:
    xx='1'
if zz==2:
    xx='2'
if zz==3:
    xx='3'
bt = open("token.txt","r")
tok =str( bt.readline())
bot = telebot.TeleBot('5316100798:AAFWBq6I9RVG9lVUIAsknYFpbXwgBRjvrw4')
n=0
n1=''
'''

'''
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, "Ballon на связи")
@bot.message_handler(commands=["wws"])
def wws(message):
    aa=random.randint(1,3)
    if aa==1:
        bb='Колобок повесился'
    if aa==2:
        bb='Русалка села на шпагат'
    if aa==3:
        bb='Рыба потонула'
    bot.send_message(message.from_user.id, bb)
@bot.message_handler(commands=["MyId"])
def MyId(message):
    bot.send_message(message.from_user.id, "Я щас скажу твой ad")
    bot.send_message(message.from_user.id, 'Id:'+str(message.from_user.id)+'!')  
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.from_user.id, "Вот что я умею")
    bot.send_message(message.from_user.id, "старт-""/start")
    bot.send_message(message.from_user.id, "Мой айди-""/MyId")
    bot.send_message(message.from_user.id, "Спой песню-""/sing")
    bot.send_message(message.from_user.id, "Спойлер-""/spoiler")
    bot.send_message(message.from_user.id, "Три шутки-""/wws")
    bot.send_message(message.from_user.id, "Камень,Ножницы,Бумага-""/new")
    bot.send_message(message.from_user.id, "Давай поговорим-""/talk")
@bot.message_handler(commands=["sing"])
def sing(message):
    bot.send_message(message.from_user.id, "Антошка Антошка пошли копать картошку")
    bot.send_message(message.from_user.id, "Антошка Антошка пошли копать картошку")
@bot.message_handler(commands=["new"])
def new(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Камень")
    btn2 = types.KeyboardButton("Ножницы")
    btn3 = types.KeyboardButton("Бумага")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id,"Выбери Камень, Ножницы, Бумага", reply_markup=markup)
@bot.message_handler(commands=["spoiler"])
def spoiler(message):
    bot.send_message(message.from_user.id, " Я буду лутчим телеграм ботов")
    bot.send_message(message.from_user.id, "Потому что меня писал -R")  
@bot.message_handler(commands=["talk"])
def talk(message):
    global n
    n=1
    bot.send_message(message.from_user.id, "Меня зовут ballon")
    bot.send_message(message.from_user.id, "а тебя как зовут")
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global n, n1
    if n==1:
        n1=message.text
        bot.send_message(message.from_user.id, "Будем знакомы, "+n1)
        n=0
    elif message.text == "Классно" or message.text == "Отлично"or message.text == "класно"or message.text == "Жесть"or message.text == "жесть"or message.text == "здорово"or message.text == "Здорово"or message.text == "класс" or message.text== "окей"or message.text == "Окей" or message.text == "отлично"or message.text == "Класс" or message.text == "Идеал" or message.text == "Идеально":
        bot.send_message(message.from_user.id,"Спасибо")
    elif message.text == "Как у тебя дела?" or message.text == "Как у тебя дела" or message.text == "как у тебя дела" or message.text == "Как дела" or message.text == "Как дела?" or message.text == "как дела?"or message.text == "А как дела?" or message.text == "А как дела" :
        bot.send_message(message.from_user.id,"Я бот, я не имею эмоций")
    elif message.text == "Привет" or message.text == "привет" or message.text == "Дарова" or message.text == "Здравствуй":
        bot.send_message(message.from_user.id,"Привет "+message.from_user.first_name+"!")
    elif message.text == "Как тебя зовут" or message.text == "Как тебя зовут?":
        bot.send_message(message.from_user.id,"Ballon!")
    elif message.text == "ага" or message.text == "Ага":
        bot.send_message(message.from_user.id,"Ага")
    elif(message.text == "Камень"):
        zz=random.randint(1,3)
        if zz==1:
            xx='Бумага'
            bot.send_message(message.from_user.id, xx)
            bot.send_message(message.from_user.id, 'Проиграл')
        if zz==2:
            xx='Ножницы'
            bot.send_message(message.from_user.id, xx)
            bot.send_message(message.from_user.id, 'Победа')
        if zz==3:
            xx='Камень'
            bot.send_message(message.from_user.id, xx)
            bot.send_message(message.from_user.id, 'Ничья')
    elif(message.text == "Ножницы"):
        zz=random.randint(1,3)
        if zz==1:
            xx='Бумага'
            bot.send_message(message.from_user.id, xx)
            bot.send_message(message.from_user.id, 'Победа')
        if zz==2:
            xx='Ножницы'
            bot.send_message(message.from_user.id, xx)
            bot.send_message(message.from_user.id, 'Ничья')
        if zz==3:
            xx='Камень'
            bot.send_message(message.from_user.id, xx)
            bot.send_message(message.from_user.id, 'Проиграл')
    elif(message.text == "Бумага"):
        zz=random.randint(1,3)
        if zz==1:
            xx='Бумага'
            bot.send_message(message.from_user.id, xx)
            bot.send_message(message.from_user.id, 'Ничья')
        if zz==2:
            xx='Ножницы'
            bot.send_message(message.from_user.id, xx)
            bot.send_message(message.from_user.id, 'Проиграл')
        if zz==3:
            xx='Камень'
            bot.send_message(message.from_user.id, xx)
            bot.send_message(message.from_user.id, 'Победа')
    else:
        bot.send_message(message.from_user.id, "Я пока не знаю этого. Напиши /help.")
        bot.send_message(message.from_user.id, "Но ваше слово занесенно.Скоро я смогу это сделать")
        zz=open('bot.txt','a')
        zz.write('\n')
        zz.write(tconv(message.date)) 
        zz.write(' : ')
        zz.write(str(message.from_user.id))
        zz.write(' , ')
        zz.write(message.from_user.last_name or 'Неизветно')
        zz.write(' , ')
        zz.write(message.from_user.first_name or 'Неизветно')
        zz.write(' : ')
        zz.write(message.text)
        zz.close()
bot.polling(none_stop=True, interval=0)

