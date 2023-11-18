import requests
import telebot

class App:
    def __init__(self, url, id):
        self.data = {
            "key": "9662e2fc21114e2061e4b06ccbd3746d",
            "action": "add",
            "link": url,
            "quantity": "1000",
            "service": id
        }
# @Crazzy_8 & @BRoK8
    def add_order(self):
        res = requests.post("https://fastsmo.com/api/v2", data=self.data).text

token = "6756691141:AAH6V5Hg2j1HchKzY32J6H5sgubQtaqXA-c"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("مشاهدات تيك توك")
    item2 = telebot.types.KeyboardButton("مشاهدات تويتر فيديو")
    item3 = telebot.types.KeyboardButton("مشاهدات تويتر تغريدة")
    item4 = telebot.types.KeyboardButton("مشاهدات تلجرام")
    markup.row(item1, item2)
    markup.row(item3, item4)
    bot.send_message(message.chat.id, "اختر الخدمة:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_service_choice(message):
    url = bot.send_message(message.chat.id, "أدخل الرابط:")
    bot.register_next_step_handler(url, process_service_choice, message.text)


def process_service_choice(url_message, service_choice):
    url = url_message.text
    app = None
    if service_choice == "مشاهدات تيك توك":
        app = App(url, "3381")
    elif service_choice == "مشاهدات تويتر فيديو":
        app = App(url, "3382")
    elif service_choice == "مشاهدات تويتر تغريدة":
        app = App(url, "3383")
    elif service_choice == "مشاهدات تلجرام":
        app = App(url, "3392")

    if app:
        app.add_order()
        bot.send_message(url_message.chat.id, "تم استلام طلبك، يرجى الانتظار...")
# @Crazzy_8 & @BRoK8
bot.infinity_polling()
