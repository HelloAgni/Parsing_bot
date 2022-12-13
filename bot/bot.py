import os
import signal
import sqlite3
from table_check import check_table
from file_check import check_file
import pandas as pd
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import msg
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

load_dotenv()

TOKEN = os.getenv('TOKEN')
# USER_ID = os.getenv('USER_ID')
TEMP_DIR = '/tempfiles/'

updater = Updater(token=TOKEN)


def my_file(update, context):    
    chat = update.effective_chat
    doc = context.bot.get_file(update.message.document)
    file_path = check_file(doc=doc)
    if file_path:
        """
        Проверяем состояние таблицы
        """
        doc.download(custom_path=file_path)
        report = check_table(file_path=file_path)
        if report:
            context.bot.send_message(
                chat_id=chat.id,
                text=report
            )
        else:
            try:
                con = sqlite3.connect('db.sqlite')
                rows = ['name', 'url', 'xpath']
                d = pd.read_excel(file_path, header=None, names=rows)
                table = d.to_string(
                    index=False, max_colwidth=15, justify='center')
                d.to_sql(
                    name='krakoz', con=con, if_exists='append', index=False)
                con.close()
                context.bot.send_message(
                    chat_id=chat.id,
                    text=msg.msg_upload(data=table)
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
    remove_button = ReplyKeyboardRemove()
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text=msg.msg_stop(),
                             reply_markup=remove_button)
    os.kill(os.getpid(), signal.SIGINT)


if __name__ == '__main__':
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('stop', bot_break))
    updater.dispatcher.add_handler(MessageHandler(Filters.document, my_file))

    updater.start_polling()
    updater.idle()
