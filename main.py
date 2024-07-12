import os
import uuid
import time

import telebot
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
from telebot import types


bot = telebot.TeleBot("7044485074:AAEB2yJ8756S2fyM2Z82IzMvYUXL1ABPUE4")
user_state = {}


def main_keyboard():
    main = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(text='Белая Форма', callback_data='dinamo_w')
    button2 = types.InlineKeyboardButton(text='Синяя Форма', callback_data='dinamo_blue')
    button3 = types.InlineKeyboardButton(text='Зеленая Форма', callback_data='dinamo_g')
    button4 = types.InlineKeyboardButton(text='Черная Форма', callback_data='dinamo_black')

    main.add(button1, button2)
    main.add(button3, button4)

    return main


def channel():
    ch = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton(text='SMIponaroshku', url='https://t.me/SMIponaroshku', callback_data='channel')

    ch.add(button1)

    return ch


def dinamo(path, font_path, image_name, your_name, your_number, text_color):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_name = 90
    font_number = 400

    x_name = (image.width) // 2
    y_name = 250

    x_number = (image.width) // 2
    y_number = 525

    font1 = ImageFont.truetype(font_path, font_name)
    font2 = ImageFont.truetype(font_path, font_number)

    draw.text((x_name, y_name), your_name, font=font1, fill=text_color, anchor='mm')
    draw.text((x_number, y_number), str(your_number), font=font2, fill=text_color, anchor='mm')

    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(image_name, new_img)


def dinamo_g(path, font_path, image_name, your_name, your_number, text_color):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_name = 350
    font_number = 1600

    x_name = (image.width) // 2
    y_name = 1000

    x_number = (image.width) // 2
    y_number = 2200

    font1 = ImageFont.truetype(font_path, font_name)
    font2 = ImageFont.truetype(font_path, font_number)

    draw.text((x_name, y_name), your_name, font=font1, fill=text_color, anchor='mm')
    draw.text((x_number, y_number), str(your_number), font=font2, fill=text_color, anchor='mm')

    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(image_name, new_img)


@bot.message_handler(commands=['start'])
def start_bot(message):
    user = bot.get_chat_member(-1001960632253, message.from_user.id)
    if user and user.status in ['creator', 'administrator', 'member']:
        bot.send_message(message.chat.id, "Бот успешно запущен", reply_markup=main_keyboard())
    else:
        bot.send_message(message.chat.id, "Для использования функционала подпишитесь на канал!!!", reply_markup=channel())


@bot.callback_query_handler(func=lambda call: True)
def dinamo_club_handlers(call):
    if call.data == 'dinamo_w':
        bot.send_message(call.message.chat.id, "Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(call.message, name_asking_for_white, call.data)
    elif call.data == 'dinamo_blue':
        bot.send_message(call.message.chat.id, "Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(call.message, name_asking_for_white, call.data)
    elif call.data == 'dinamo_g':
        bot.send_message(call.message.chat.id, "Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(call.message, name_asking_for_white, call.data)
    elif call.data == 'dinamo_black':
        bot.send_message(call.message.chat.id, "Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(call.message, name_asking_for_white, call.data)


def name_asking_for_white(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_white, club)


def name_asking_for_blue(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_blue, club)


def name_asking_for_green(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_green, club)


def name_asking_for_black(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_black, club)


def result(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'dinamo.ttf'
        if club == 'dinamo_w':
            text_color = (1, 83, 183)
        else:
            text_color = (255, 255, 255)

        if club == 'dinamo_g':
            dinamo_g(path, font_path, image_name, your_name, your_number, text_color)
        else:
            dinamo(path, font_path, image_name, your_name, your_number, text_color)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result)

running = True

while running:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Exception occurred: {e}")
        time.sleep(1)

