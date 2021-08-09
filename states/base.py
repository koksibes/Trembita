from telebot import types

from config import bot


class BaseState:
    text: str = ''
    keyboard = None

    def __init__(self, chat_id):
        # self.text = text
        self.chat_id = chat_id
        keyboard = types.InlineKeyboardMarkup()
        self.keyboard = keyboard

    def display(self):
        bot.send_message(self.chat_id, self.text, reply_markup=self.keyboard)

    def process(self, message: types.Message):
        pass
