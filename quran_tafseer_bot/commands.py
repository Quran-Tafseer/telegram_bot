from pytafseer import QuranTafseer
from models import UserPreference, database
from decorators import send_action
import peewee
from messages import render_message
from telegram.chataction import ChatAction


@send_action(ChatAction.TYPING)
def start(bot, update):
    """The start command for the bot. Ths command will
    introduce the bot actions to the user.

    :param bot: bot instance
    :param update: update/chat instance
    """
    message = render_message('start.html')
    bot.send_message(chat_id=update.message.chat_id, text=message)


@send_action(ChatAction.TYPING)
def book_list(bot, update):
    """Gets the list of availabe books command.

    :param bot: bot instance
    :param update: update/chat instance
    """
    books = QuranTafseer.get_tafseer_books()
    message = render_message('book_list.html', books=books)
    bot.send_message(chat_id=update.message.chat_id, text=message,
                     parse_mode='HTML')


@send_action(ChatAction.TYPING)
def set_book(bot, update, args):
    """Sets the active Tafseer book for the user.
    This book will be used by other commands

    :param bot: bot instance
    :param update: update/chat instance
    :param args: List of arguments. [book id]
    """
    try:
        book_id = args[0]
    except IndexError:
        # User didn't assign a book ID
        message = render_message('setbook_invalid.html')
        bot.send_message(chat_id=update.message.chat_id, text=message)
        return None

    from_user = update.message.from_user
    user = UserPreference
    try:
        user = UserPreference.create(user_id=from_user['id'],
                                     first_name=from_user['first_name'],
                                     last_name=from_user['last_name'],
                                     username=from_user['username'],
                                     book_id=int(book_id)
                                     )
    except peewee.IntegrityError:
        user = UserPreference.get(UserPreference.user_id == from_user['id'])
        user.first_name = from_user['first_name']
        user.last_name = from_user['last_name']
        user.username = from_user['username']
        user.book_id = int(book_id)
        user.save()
    # TODO: Send the name of the book in the message instead of the ID only
    message = render_message('set_book.html', book_id=book_id)
    bot.send_message(chat_id=update.message.chat_id, text=message)


@send_action(ChatAction.TYPING)
def tafseer(bot, update, args):
    """Gets the Tafseer fot the verse in a chapter.

    :param bot: bot instance
    :param update: update/chat instance
    :param args: List of arguments. [chapter number, verse number]
    """
    try:
        chapter_number = args[0]
        verse_number = args[1]
    except IndexError:
        # User sent invalid arguments
        bot.send_message(chat_id=update.message.chat_id,
                         text=render_message('tafseer_invalid.html'))
        return None
    user = UserPreference.get(
        UserPreference.user_id == update.message.from_user['id'])
    tafseer_book = QuranTafseer(book_id=user.book_id)
    tafseer_text = tafseer_book.get_verse_tafseer(
        chapter_number=chapter_number,
        verse_number=verse_number)
    message = render_message('tafseer.html', tafseer=tafseer_text['text'])
    bot.send_message(chat_id=update.message.chat_id, text=message)
