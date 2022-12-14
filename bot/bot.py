import os
import signal

import msg
from dotenv import load_dotenv
from file_check import check_file
from parsing import open_file_and_parsing
from table_check import check_table_and_insert_data
from telegram import ReplyKeyboardRemove
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()

TOKEN = os.getenv('TOKEN')
TEMP_DIR = '/tempfiles/'

updater = Updater(token=TOKEN)


def my_file(update, context):
    """
    Проверка расширения файла.
    Получение имени и указание пути для загрузки.
    Провека состояние таблицы и валидация.
    """
    chat = update.effective_chat
    doc = context.bot.get_file(update.message.document)
    file_path = check_file(doc=doc)
    if file_path:
        doc.download(custom_path=file_path)
        report = check_table_and_insert_data(file_path=file_path)
        if isinstance(report, str):
            context.bot.send_message(
                chat_id=chat.id,
                text=report
            )
        elif isinstance(report, dict):  # timeout limit?
            context.bot.send_message(
                chat_id=chat.id,
                text=msg.msg_upload(report['table'])
            )
            try:
                result, pars_time = open_file_and_parsing(file=file_path)
                context.bot.send_message(
                    chat_id=chat.id,
                    text=f'{result}{msg.msg_time_pars()}{pars_time}c.')
            except Exception as er:
                context.bot.send_message(
                    chat_id=chat.id,
                    text=f'{msg.msg_tolong_pars()} {er}')
    else:
        context.bot.send_message(
            chat_id=chat.id,
            text=msg.msg_file_check_error()
            )


def wake_up(update, context):
    """
    Активация Бота и приветствие команда /start.
    """
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text=msg.msg_hi(name=name))


def bot_break(update, context):
    """
    Остановка бота из чата комманда /stop.
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
