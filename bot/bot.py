import os
import signal
import sqlite3
from file_check import temp_file_path
import pandas as pd
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import msg
# from telegram import ReplyKeyboardMarkup

load_dotenv()

TOKEN = os.getenv('TOKEN')
USER_ID = os.getenv('USER_ID')
TEMP_DIR = '/tempfiles/'

updater = Updater(token=TOKEN)


def my_file(update, context):
    con = sqlite3.connect('db.sqlite')
    chat = update.effective_chat
    doc = context.bot.get_file(update.message.document)
    file_path = temp_file_path(doc=doc)
    if file_path:
        doc.download(custom_path=file_path)
        try:
            rows = ['name', 'url', 'xpath']
            # xls, xlsx, xlsm, xlsb, odf, ods and odt
            d = pd.read_excel(file_path, header=None, names=rows)

            # d.to_sql(name='krakoz', con=con, if_exists='append', index=False)
            con.close()
            context.bot.send_message(
                chat_id=chat.id,
                text=msg.msg_upload(data=d)
            )
        except Exception as e:
            context.bot.send_message(
                chat_id=chat.id,
                text=msg.msg_file_error(er=e)
            )
    else:
        context.bot.send_message(
            chat_id=chat.id,
            text='Файл не прошел проверку!'
            )


def wake_up(update, context):
    """
    Активация Бота и приветствие команда /start
    """
    chat = update.effective_chat
    name = update.message.chat.first_name
    # button = ReplyKeyboardMarkup([['Line_2']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text=msg.msg_hi(name=name))
    # reply_markup=button)


def bot_break(update, context):
    """
    Остановка бота из чата комманда /stop
    """
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text=msg.msg_stop())
    os.kill(os.getpid(), signal.SIGINT)


if __name__ == '__main__':
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('stop', bot_break))
    updater.dispatcher.add_handler(MessageHandler(Filters.document, my_file))

    updater.start_polling()
    updater.idle()
