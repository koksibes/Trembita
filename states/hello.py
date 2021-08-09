from telebot import types

from states.action import ActionState
from states.base import BaseState


class HelloState(BaseState):
    text = "Приветсвуем вас"

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.keyboard.add(types.InlineKeyboardButton(text='Акция', callback_data='nextstate:ActionState'))
        self.keyboard.add(types.InlineKeyboardButton(text='Ваш Тариф', callback_data='nextstate:TarifState'))
        self.keyboard.add(types.InlineKeyboardButton(text='Курс', callback_data='nextstate:CursState'))

    def process(self, message: types.Message):
        if hasattr(message, 'data'):
            if message.data == 'nextstate:ActionState':
                return ActionState(self.chat_id)
        return self
