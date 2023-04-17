#-*- coding: utf-8 -*-
import asyncio
import telebot
import time
import schedule
import threading
from telegram import Bot

TOKEN = '5942470985:AAEqun8lUp-pKLakwYXyutssMtAKB0rbjHo'
ID = '815519369'
RESULT = 'https://docs.google.com/spreadsheets/d/1mmnyQsgDmzaw9Ut6t6HlUDQKTueKu_jb5oU27lbQZCQ/edit?usp=sharing'
LESSON = 'https://meet.google.com/abn-qzcz-xno'
HOMEWORK = 'mlcourse.unn@gmail.com'
RES1 = 'https://disk.yandex.com/i/VR6kXsXjxf_ROA'
RES2 = 'https://disk.yandex.com/i/ucXmzGjj4s-K5g'
RES3 = 'https://disk.yandex.com/i/MiJNI7-k3lVHgQ'
RES4 = 'https://disk.yandex.com/i/LIveaauvaX2Hbw'
RES5 = 'https://stackoverflow.com/questions/33899369/ranking-order-per-group-in-pandas'
FEEDBACK1 = 'https://docs.google.com/forms/d/e/1FAIpQLSdICzIz6b_yRxYyV22CsphqGzvL50rRTW-QA2-HDAtsRPQHjA/viewform?usp=sf_link'
FEEDBACK2 = 'https://docs.google.com/forms/d/e/1FAIpQLSeZJU8WaNt92t3i84mLW8E-TiWXzfY4dFh5QGCEKhtfU2Kw3w/viewform?usp=sf_link'
FEEDBACK3 = 'https://forms.gle/Unk2egQDCrKL46o49'
FEEDBACK4 = 'https://forms.gle/xx1VN5kvjSKfQUNaA'
VIDEO1 = 'https://disk.yandex.ru/i/ALWjxOVWGLA1Fw'
VIDEO2 = 'https://drive.google.com/file/d/1-Il4v4Tv2xI03L4NvE_NPA7GwsDY3soH/view?usp=sharing'
VIDEO3 = 'https://drive.google.com/file/d/1bayWx7Lz1IA12ZYIEoAxELmrAw7XE3qt/view?usp=drivesdk'
VIDEO4 = 'https://drive.google.com/file/d/1AMPcrS9dsV1tJX_PfV42XxKFufl9xziw/view?usp=drivesdk'
VIDEO5 = 'https://drive.google.com/file/d/1EHwtlRoHdxNpet7IDgKgI_tPNpo-hdCZ/view?usp=sharing'
VIDEO6 = 'https://drive.google.com/file/d/1kNGX9SjwhGrI-WEZ0bH8k_tMW9o9FPOu/view?usp=drivesdk'
VIDEO7 = 'https://drive.google.com/file/d/1_YC-tXpCYwLpjAaV5CYyD2lwVFZYnPsf/view?usp=drivesdk'
VIDEO8 = 'https://drive.google.com/file/d/1nirFMel0Ngmv96u5DV-ReOZVF0OoZcWA/view?usp=drivesdk'
VIDEO9 = 'https://drive.google.com/file/d/119jMEdvQqyYuLfD9rwuT2WIaibmdWHu8/view?usp=sharing'
VIDEO10 = 'https://drive.google.com/file/d/1CI0-p7yck009JsVYv-sOUPO6srboIxjN/view?usp=sharing'
VIDEO11 = 'https://drive.google.com/file/d/1l1qBSGemQnKmiM98VEHYfmDNhKmv9G6Q/view?usp=drivesdk'
VIDEO12 = 'https://drive.google.com/file/d/12hbxi_3j8cCHxFb6GQo3H7R2xNR7ZCql/view?usp=sharing'
VIDEO13 = 'https://drive.google.com/file/d/1nsJa7yMg-Ibf4Zeqi4jyI1rLcHglNyUv/view?usp=drivesdk'
VIDEO14 = 'https://drive.google.com/file/d/1oPJ9k59SUwIC_U2yvdI86k_fKdsRbW9o/view?usp=sharing'
VIDEO15 = 'https://drive.google.com/file/d/1Dz4J7lUJ_IrtZyiOZeisoPstAXHkkmp7/view?usp=drivesdk'
VIDEO16 = 'https://drive.google.com/file/d/1VWrVlDwm07B42tc8NIuzsquloNi1Yfyu/view?usp=sharing'
VIDEO17 = 'https://drive.google.com/file/d/1CcC4zDMCic0-pKCayHVQQMY-zkjbZv-4/view?usp=sharing'
VIDEO18 = 'https://drive.google.com/file/d/1g3a1Uc0u4hSHhUx5RX5BPFFAvO2-9Zse/view?usp=drivesdk'

bot_1 = Bot(token=TOKEN)
bot_2 = telebot.TeleBot(TOKEN)

@bot_2.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = telebot.types.KeyboardButton('Result')
    button_2 = telebot.types.KeyboardButton('Homework')
    button_3 = telebot.types.KeyboardButton('Feedback')
    button_4 = telebot.types.KeyboardButton('Lesson')
    button_5 = telebot.types.KeyboardButton('Video')
    button_6 = telebot.types.KeyboardButton('Resources')
    markup.add(button_1, button_2, button_3, button_4, button_5, button_6)

    user_name = message.from_user.first_name
    bot_2.send_message(message.chat.id, f'Привет, {user_name}! Я телеграмм бот, помогающий сориентироваться вашей учебной группе в процессе обучения.\n\nИ так, давайте расскажу, что я умею:\n\nResult - это сводная ведомость, где отображается прогресс выполнения домашних заданий, и оценки за их выполнение;\n\nHomework - это адрес для отправки домашних заданий и тип оформления файлов с заданиями;\n\nFeedback - здесь указаны ссылки на формы обратной связи по пройденным занятиям. Убедительно просим вас принимать участие во всех опросах. Результаты опросов помогают преподавателю оценить степень восприятия информации, и как результат, скорректировать учебный процесс;\n\nLesson - это ссылка на подключение к онлайн занятиям;\n\nVideo - это ссылка на запись занятия за определенную дату;\n\nResources - это перечень материалов, которые могут быть вам полезны в процессе обучения;\n\nА также в дни обучения, незадолго до начала занятия, я буду присылать вам напоминание и ссылку на подключение.', reply_markup=markup)

@bot_2.message_handler(content_types=['text'])
def bot_2_message(message):
    if message.chat.type == 'private':
        if message.text == 'Result':
            user_name = message.from_user.first_name
            bot_2.send_message(message.chat.id, f'{user_name}, вот ваша ссылка на сводную ведомость:\n{RESULT}')
        elif message.text == 'Homework':
            user_name = message.from_user.first_name
            bot_2.send_message(message.chat.id, f'{user_name}, домашняюю работу необходимо отправлять по адресу:\n{HOMEWORK}\nНазвание файла с домашней работой должно иметь вид: <Фамилия>_<ИО>_тема.\nВ теме письма не забывайте указывать тему домашней работы.')
        elif message.text == 'Feedback':
            user_name = message.from_user.first_name
            bot_2.send_message(message.chat.id, f'{user_name}, вот список опросов по всем пройденным темам:\n\nML&DS. Lesson 3. Pandas in practice:\n{FEEDBACK1}\n\nML&DS. Lesson 5. Confident intervals:\n{FEEDBACK2}\n\nML&DS. Неделя 4. Стат. критерии, k-ближайших соседей, numpy:\n{FEEDBACK3}\n\nML&DS. Недели 6 и 7. МНК, град. спуск, классификация, переобучение:\n{FEEDBACK4}')
        elif message.text == 'Lesson':
            user_name = message.from_user.first_name
            bot_2.send_message(message.chat.id, f'{user_name}, вот ваша ссылка на онлайн занятие:\n{LESSON}')
        elif message.text == 'Video':
            user_name = message.from_user.first_name
            bot_2.send_message(message.chat.id, f'{user_name}, вот список всех доступных записей занятий:\n\n20.02.2023: {VIDEO1}\n\n27.02.2023: {VIDEO2}\n\n04.03.2023: {VIDEO3}\n\n06.03.2023: {VIDEO4}\n\n10.03.2023: {VIDEO5}\n\n13.03.2023: {VIDEO6}\n\n15.03.2023: {VIDEO7}\n\n17.03.2023: {VIDEO8}\n\n20.03.2023: {VIDEO9}\n\n27.03.2023: {VIDEO10}\n\n30.03.2023: {VIDEO11}\n\n31.03.2023: {VIDEO12}\n\n03.04.2023: {VIDEO13}\n\n05.04.2023: {VIDEO14}\n\n07.04.2023: {VIDEO15}\n\n10.04.2023: {VIDEO16}\n\n12.04.2023: {VIDEO17}\n\n14.04.2023: {VIDEO18}')
        elif message.text == 'Resources':
            user_name = message.from_user.first_name
            bot_2.send_message(message.chat.id, f'{user_name}, вот список интересных материалов, которые могут быть вам полезны в процессе обучения:\n\nШпаргалка по Pandas (часть 1): {RES1}\n\nШпаргалка по Pandas (часть 2): {RES2}\n\nШпаргалка по NumPy (часть 1): {RES3}\n\nШпаргалка по NumPy (часть 2): {RES4}\n\nРанжирование в Pandas: {RES5}')

letter = (f'До начала занятия осталось 10 минут. Вот ссылка {LESSON}')

async def reminder():
    await bot_1.send_message(chat_id=ID, text=letter)

def schedule_reminder():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    schedule.every().monday.at('17:19').do(lambda: loop.run_until_complete(reminder()))
    schedule.every().wednesday.at('17:50').do(lambda: loop.run_until_complete(reminder()))
    schedule.every().friday.at('17:50').do(lambda: loop.run_until_complete(reminder()))
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    thread = threading.Thread(target=schedule_reminder)
    thread.start()
    thread_2 = threading.Thread(target=bot_2.polling(none_stop=True))
    thread_2.start()