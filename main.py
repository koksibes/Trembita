# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from config import bot


# Press the green button in the gutter to run the script.
# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):  # Название функции не играет никакой роли
#     bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['start'])
def begin_conversation(message):
    from states.hello import HelloState
    s = HelloState(message.chat.id)
    s.display()
    user_states[message.chat.id] = s


@bot.callback_query_handler(func=lambda d: True)
def callback_handler(message):
    s = user_states[message.from_user.id]
    s2 = s.process(message)
    s2.display()
    user_states[message.from_user.id] = s2


user_states = {}
if __name__ == '__main__':
    bot.infinity_polling()
