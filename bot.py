import telebot
import requests
import random
from config import token
from programmer import pro_skill

import os
print(os.listdir('images'))

bot = telebot.TeleBot(token)
can = '/skill - покажет какой ты программист, /mems - покажет мем, /duck - покажет утку, /dog - покажет собаку.'
@bot.message_handler(commands=['skill'])
def send_bye(message):
    skillz = pro_skill(1)
    bot.reply_to(message, f"Ты программист на {skillz}")

@bot.message_handler(commands=['start'])
def send_bye(message):
    bot.reply_to(message, F'Вот что я могу: {can}')

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open('images/mem1.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['mems'])
def send_random_mem(message):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']      
@bot.message_handler(commands=['duck'])
def duck(message):
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

def get_dog_image_url(): 
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']  
@bot.message_handler(commands=['dog'])
def anime(message):
    image_url = get_dog_image_url()
    bot.reply_to(message, image_url) 

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    reply_to(message, message.text)

@bot.message_handler(commands=['start'])
def send_bye(message):
    bot.reply_to(message, F'Вот что я могу: {can}')

bot.infinity_polling()