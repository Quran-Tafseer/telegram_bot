from settings import BOT_TOKEN
from telegram.ext import Updater, CommandHandler
import logging
from models import UserPreference, database
import peewee
from commands import (start,  book_list, set_book, tafseer)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

# Map command with functions
start_handler = CommandHandler('start', start)
book_list_handler = CommandHandler('books', book_list)
set_book_handler = CommandHandler('setbook', set_book, pass_args=True)
tafseer_handler = CommandHandler('tafseer', tafseer, pass_args=True)


# Add the mapping
dispatcher.add_handler(start_handler)
dispatcher.add_handler(book_list_handler)
dispatcher.add_handler(set_book_handler)
dispatcher.add_handler(tafseer_handler)

if __name__=="__main__":
    database.connect()
    # database.create_tables([UserPreference])
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
