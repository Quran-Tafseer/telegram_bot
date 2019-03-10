from settings import BOT_TOKEN, TEMAPLTE_PATH
from telegram.ext import Updater, CommandHandler
from pytafseer import QuranTafseer
import logging
from jinja2 import Environment, FileSystemLoader, select_autoescape
from models import UserPreference, database
import peewee

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher


# Loading Jinja2 environment
env = Environment(
    loader=FileSystemLoader(TEMAPLTE_PATH),
    autoescape=select_autoescape(['html', 'xml'])
)


def start(bot, update):
    template = env.get_template('start.html')
    message = template.render()
    bot.send_message(chat_id=update.message.chat_id, text=message)

def book_list(bot, update):
    books = QuranTafseer.get_tafseer_books()
    template = env.get_template('book_list.html')
    message = template.render(books=books)
    bot.send_message(chat_id=update.message.chat_id, text=message)

def set_book(bot, update):
    book_id = update.message.text.split('/setbook')[1].strip()
    from_user = update.message.from_user
    try:
        user = UserPreference.create(user_id=from_user['id'],
        first_name=from_user['first_name'],
        last_name=from_user['last_name'],
        username=from_user['username'],
        book_id=int(book_id)
        )
    except peewee.IntegrityError:
        user = UserPreference.get(UserPreference.user_id == from_user['id'])
        user.first_name=from_user['first_name']
        user.last_name=from_user['last_name']
        user.username=from_user['username']
        user.book_id=int(book_id)
    finally:
        user.save()
    template = env.get_template('set_book.html')
    message = template.render(book_id=book_id)
    bot.send_message(chat_id=update.message.chat_id, text=message)

def tafseer(bot, update):
    user= UserPreference.get(UserPreference.user_id == update.message.from_user['id'])
    chapter_number, verse_number = update.message.text.split('/tafseer')[1].strip().split()
    tafseer_book = QuranTafseer(book_id=user.book_id)
    tafseer_text = tafseer_book.get_verse_tafseer(chapter_number=chapter_number,
    verse_number=verse_number)
    template = env.get_template('tafseer.html')
    message = template.render(tafseer=tafseer_text['text'])
    bot.send_message(chat_id=update.message.chat_id, text=message)

# Map command with functions
start_handler = CommandHandler('start', start)
book_list_handler = CommandHandler('books', book_list)
set_book_handler = CommandHandler('setbook', set_book)
tafseer_handler = CommandHandler('tafseer', tafseer)

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
