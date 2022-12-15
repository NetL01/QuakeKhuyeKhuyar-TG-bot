import schedule
from datetime import datetime
import time
import telebot
from yaweather import Russia, YaWeather
import random
import multiprocessing
import threading
import pickle
import os
import json


a = ['123', '321']
# Main token to start
bot = telebot.TeleBot('5849840132:AAEHFN1i-u6ZiglFRYL4jcwvL-1_R9DuKdM')
# bot.send_message(-1001803296788, text=f"{datetime.now()} bot started")

target_dist = 'saved_dictionary.pkl'
if os.path.getsize(target_dist) > 0:
    with open('saved_dictionary.pkl', 'rb') as f:
        loaded_dict = pickle.load(f)
        todo_list = loaded_dict
        print('132')
else:
    todo_list = {}

try:
    @bot.message_handler(commands=['check'])
    def check(message):
        bot.reply_to(message, text=f'Bot status: working, {message.from_user.username}!')

    @bot.message_handler(commands=['pogoda'])
    def pogoda(message):
        y = YaWeather(api_key='2256552c-c694-4849-9715-95763b707bae')
        res = y.forecast(Russia.SaintPetersburg)
        dict_condition = {"clear": "ясно", "overcast": "пасмурно", "rain": "дождь", "cloudy": "облачно"}
        if res.fact.condition in dict_condition:
            bot.send_message(message.chat.id, text=f'На деле: {res.fact.temp} °C, ощущается: {res.fact.feels_like} °C\n'
                                                   f'На небе: {dict_condition[res.fact.condition]}\n'
                                                   f'Скорость ветра: {res.fact.wind_speed}\nГроза: {res.fact.is_thunder}\n')
        else:
            bot.send_message(message.chat.id, text=f'На деле: {res.fact.temp} °C, ощущается: {res.fact.feels_like} °C\n'
                                                   f'На небе: {res.fact.condition}\n'
                                                   f'Скорость ветра: {res.fact.wind_speed}\nГроза: {res.fact.is_thunder}\n')


    # TODO LIST TASKBOARD

    @bot.message_handler(commands=['todo'], content_types=['text'])
    def TODOlist(message):
        try:
            command = message.text.split(' ')
            if command[-1] == 'list':
                if not todo_list:
                    bot.send_message(-1001803296788, text=f"TODO list was empty!")
                # print priority
                else:
                    bot.send_message(-1001803296788, text=f"PRIORITY:")
                    for key, value in todo_list.items():
                        if value == 1:
                            bot.send_message(-1001803296788, text=f"{key.upper()}")
                    bot.send_message(-1001803296788, text=f"Пока похер:")
                    for key, value in todo_list.items():
                        if value == 0:
                            bot.send_message(-1001803296788, text=f"{key}")
            else:
                if command[-2] == "addpr":
                    todo_list[command[-1]] = 1
                    print(todo_list)
                    print('saved.')
                    bot.send_message(-1001803296788, text=f"saved.")
                if command[-2] == "delpr":
                    if command[-1] in todo_list:
                        del todo_list[command[-1]]
                        print("deleted.")
                        bot.send_message(-1001803296788, text=f"deleted.")
                    else:
                        bot.send_message(-1001803296788, text=f"TODO id not found")

                if command[-2] == "add":
                    print(todo_list)
                    todo_list[command[-1]] = 0
                    print('saved.')
                    bot.send_message(-1001803296788, text=f"saved.")
                if command[-2] == "del":
                    if command[-1] in todo_list:
                        del todo_list[command[-1]]
                        print('deleted.')
                        bot.send_message(-1001803296788, text=f"deleted.")
                    else:
                        bot.send_message(-1001803296788, text=f"TODO id not found")
        except:
            bot.send_message(-1001803296788, text=f"TODO is working, try it!\n"
                                                  f"Check list = /todo list\n Add Priority elem = /todo addpr(delpr) <name> \n"
                                                  f"Add basic elem = /todo add(del) <name> ")



    def GoCode():
        variants = ['Время ботать?!', 'Ботать ботать боооотаааать!!', 'Я сделал алгосы, а ТЫ?', 'Щас бы тяночку...',
                    'Я хочу детей от сатисфекшена...']
        var = random.randint(0, 4)
        bot.send_message(-1001803296788, text=f'{variants[var]}')

    @bot.message_handler(commands=['stop'])
    def exit(message):


        with open(target_dist, 'wb') as f:
            print('Prepare to save before closed bot')
            pickle.dump(todo_list, f)
            # print(os.path.getsize(target_dist))
        crashlist = [1, 2, 3]
        for i in range(len(crashlist) + 10):
            a = crashlist[i]



    with multiprocessing.Pool(2) as pool:
        schedule.every(1).hour.do(GoCode)
        print('work')

    bot.polling(none_stop=True, interval=0)



except:
    print('crashed')
    # bot.send_message(-1001803296788, text=f"{datetime.now()} bot was stopped!")

if __name__ == '__main__':
    thr = threading.Thread(target=GoCode(), args=(), kwargs={})
    thr.start()  # Will run "foo"


    #thr.is_alive()  # Will return whether foo is running currently

    #thr.join()  # Will wait till "foo" is done