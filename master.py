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
import time

target_dist = 'saved_dictionary.pkl'
if os.path.getsize(target_dist) > 0:
    with open('saved_dictionary.pkl', 'rb') as f:
        loaded_dict = pickle.load(f)
        todo_list = loaded_dict
        print('saved_dictionary loaded')
else:
    todo_list = {}

target_permission = 'permission_list.pkl'
if os.path.getsize(target_permission) > 0:
    with open('permission_list.pkl', 'rb') as f:
        loaded_dict = pickle.load(f)
        permission_list = loaded_dict
        print('permission_list loaded')
else:
    permission_list = {"happy_coder": "happy_coder"}

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
schedule.run_pending()
print(permission_list)
def check_permission(id):
    return id in permission_list

# Main token to start
bot = telebot.TeleBot('5849840132:AAEHFN1i-u6ZiglFRYL4jcwvL-1_R9DuKdM')
# bot.send_message(-1001803296788, text=f"{datetime.now()} bot started")
# bot.send_message(-1001803296788, text=f" ")

try:
    @bot.message_handler(commands=['check', 'status'])
    def check(message):
        if not check_permission(message.from_user.username):
            bot.reply_to(message, text=f'Bot status: working, {message.from_user.username}!')
        else:
            bot.reply_to(message, text='Permission deny.')

    @bot.message_handler(commands=['pogoda'])
    def pogoda(message):
        if not check_permission(message.from_user.username):
            loh_list = ['happy_coder', 'BangoSteve']
            if message.from_user.username not in loh_list:
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
            else:
                bot.reply_to(message, text=f"Для тебя всегда плохая")
        else:
            bot.reply_to(message, text=f"Permission deny")


    # TODO LIST TASKBOARD

    @bot.message_handler(commands=['stats'])
    def stats(message):
        command = message.text.split(' ')
        if message.from_user.username == "netl01":
            print(command)
            if command[1] == 'check':
                bot.reply_to(message, text=f'Preparing to summarize scores from spreadsheets\n'
                             f'Status:')
                time.sleep(random.randint(1, 5))
                bot.reply_to(message, text=f'Done.')
                #bot.edit_message_text(message.chat.id, message_id=bot.message_id,
                #                      text=f'Preparing to summarize scores from spreadsheets\n'
                #                           f'Status: done')
                time.sleep(1)
                print('ok')
                bot.send_message(message.chat.id, text=f'From "Разуваев Никита" :\n'
                                 f'Практика ДМ 2022/.../Рейтинг : 37.32\n'
                                 f'АиСД рейтинг 202.../семестр 1 : 61.05')
        else:
            bot.reply_to(message, text=f"Permission deny.")

    @bot.message_handler(commands=['todo'], content_types=['text'])
    def TODOlist(message):
        try:
            if not check_permission(message.from_user.username):
                command = message.text.split(' ')
                if command[1] == 'list':
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
                    if command[1] == "addpr":
                        todo_list[command[2]] = 1
                        print(todo_list)
                        print('saved.')
                        bot.send_message(-1001803296788, text=f"saved.")
                    if command[1] == "delpr":
                        if command[2] in todo_list:
                            del todo_list[command[2]]
                            print("deleted.")
                            bot.send_message(-1001803296788, text=f"deleted.")
                        else:
                            bot.send_message(-1001803296788, text=f"TODO id not found")

                    if command[1] == "add":

                        todo_list[command[2]] = 0
                        print(todo_list)
                        print('saved.')
                        bot.send_message(-1001803296788, text=f"saved.")
                    if command[1] == "del":
                        if command[2] in todo_list:
                            del todo_list[command[2:]]
                            print('deleted.')
                            bot.send_message(-1001803296788, text=f"deleted.")
                        else:
                            bot.send_message(-1001803296788, text=f"TODO id not found")
            else:
                bot.reply_to(message, text=f"Permission deny.")
        except:
            bot.send_message(-1001803296788, text=f"TODO is working, try it!\n"
                                                  f"Check list = /todo list\n Add Priority elem = /todo addpr(delpr) <name> \n"
                                                  f"Add basic elem = /todo add(del) <name> ")


    # @bot.message_handler(commands='permission')
    # def permission(message):
    # perm_message = message.text.split(' ')
    # if message.from_user.username == 'netl01':
    # if perm_message[1] == 'list':
    # for key, value in permission_list.items():
    # bot.send_message(message.chat.id, text=f"{key}")
    # if perm_message[1] == 'add':
    # permission_list[perm_message[2]] = 0
    # bot.reply_to(message.chat.id, text=f"saved.")
    # if perm_message[1] == 'del':
    # if perm_message[2] in permission_list:
    # del permission_list[perm_message[2]]
    # bot.reply_to(message.chat.id, text=f"deleted.")
    # else:
    # bot.reply_to(message.chat.id, text=f"not found")
    # else:
    # bot.reply_to(message, text=f"Permission deny")

    def GoCode():
        variants = ['Время ботать?!', 'Ботать ботать боооотаааать!!', 'Я сделал алгосы, а ТЫ?', 'Щас бы тяночку...',
                    'Я хочу детей от сатисфекшена...']
        var = random.randint(0, 4)
        bot.send_message(-1001803296788, text=f'{variants[var]}')

    @bot.message_handler(commands=['stop'])
    def exit(message):
        if message.from_user.username == "netl01":
            # saved todo list
            with open(target_dist, 'wb') as f:
                pickle.dump(todo_list, f)
                print('todo saved')
                # print(os.path.getsize(target_dist))
            # saved permission list
            with open(target_permission, 'wb') as f:
                pickle.dump(permission_list, f)
                print('permission list saved')
                # print(os.path.getsize(target_dist))
            bot.reply_to(message, text=f"Bot stopped.")
            crashlist = [1, 2, 3]
            for i in range(len(crashlist) + 10):
                a = crashlist[i]
        else:
            bot.reply_to(message, text=f'Permission deny.')


    schedule.every(1).minute.do(GoCode)
    #with multiprocessing.Pool(2) as pool:
    #    print('work')

    bot.polling(none_stop=True, interval=0)



except:
    print('crashed')
    # bot.send_message(-1001803296788, text=f"{datetime.now()} bot was stopped!")



    #thr.is_alive()  # Will return whether foo is running currently

    #thr.join()  # Will wait till "foo" is done