from telebot import types

from states.base import BaseState


class ActionState(BaseState):
    text = "Акции"

    def __init__(self, chat_id=None):
        super().__init__(chat_id)

    def process(self, message: types.Message):
        pass
