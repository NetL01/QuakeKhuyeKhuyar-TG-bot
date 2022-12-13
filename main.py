import datetime as datetime
import telebot
import sys
import os
import importlib
from datetime import datetime
import json
import telebot
import requests as req
from geopy import geocoders
from os import environ
from yaweather import Russia, YaWeather


y = YaWeather(api_key='2256552c-c694-4849-9715-95763b707bae')
res = y.forecast(Russia.SaintPetersburg)



# Main token to start
bot = telebot.TeleBot('5849840132:AAEHFN1i-u6ZiglFRYL4jcwvL-1_R9DuKdM')
url = "https://api.weather.yandex.ru/v2/informers?lat=59.957729&lon=30.309568"
headers = {"X-Yandex-API-Key": "2256552c-c694-4849-9715-95763b707bae"}




def exit():
    sys.exit(0)
# Connect all others libs in directory
try:
    def get_py_files(src):
        cwd = os.getcwd() # Current Working directory
        py_files = []
        for root, dirs, files in os.walk(src):
            for file in files:
                if file.endswith(".py"):
                    py_files.append(os.path.join(cwd, root, file))
        return py_files


    def dynamic_import(module_name, py_path):
        module_spec = importlib.util.spec_from_file_location(module_name, py_path)
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        return module


    def dynamic_import_from_src(src, star_import = False):
        my_py_files = get_py_files(src)
        for py_file in my_py_files:
            module_name = os.path.split(py_file)[-1].strip(".py")
            imported_module = dynamic_import(module_name, py_file)
            if star_import:
                for obj in dir(imported_module):
                    globals()[obj] = imported_module.__dict__[obj]
            else:
                globals()[module_name] = imported_module
        return

    dynamic_import_from_src("first", star_import=False)
except:
	print("some errors")

bot.send_message(-1001803296788, text=f"{datetime.now()} bot started")

try:
    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, text=f'Hello,	{message.from_user.username}!')

    @bot.message_handler(commands=['пидор_дня'.upper().lower()])
    def who_pidor(message):
        import random

        # Пункт 1: примите ислам

        dict = {"Никита Перфоратор": 0, "Никита Сатисфекшн": 0, "Дмитрий Кузнайн Шпала Липецк": 0,
                "Семен банго стив гей": 0, " Кирилл шнурок коврик волосатая мохнатка хеппикодер": 0}


        for key, value in dict.items():
            dict[key] = random.randint(0, 100)
        sorted(dict.items(), key=lambda item: (item[1], item[0]))
        k = 0
        pidors = []
        cocorols = []
        good_boys = []

        sorted_dict = {}
        sorted_keys = sorted(dict, key=dict.get, reverse=True)  # [1, 3, 2]

        for w in sorted_keys:
            sorted_dict[w] = dict[w]

        for key, value in sorted_dict.items():
            if k == 0:
                to_pin = bot.send_message(message.chat.id, f'Пидор дня: {key}').message_id
                bot.pin_chat_message(chat_id=message.chat.id, message_id=to_pin)
            k += 1




    @bot.message_handler(commands=['close_session'])
    def end_session(message):
        bot.send_message(-1001803296788, text='session was closed :(')
        exit()


    @bot.message_handler(commands=['get_weather', 'weather', 'pogoda'])
    def get_weather(message):
        bot.send_message(message.chat.id, text=f'На деле: {res.fact.temp} °C, но блять словно все {res.fact.feels_like} °C')
        dict_condition = {"clear": "ясно", "overcast": "пасмурно", "rain": "дождь", "cloudy": "облачно"}
        bot.send_message(message.chat.id, text=f'На небе: {dict_condition[res.fact.condition]}')



    bot.polling(none_stop=True, interval=0)
except:
    print('pizdec')

if __name__ == '__main__':
    pass