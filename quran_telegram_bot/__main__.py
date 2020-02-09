from quran_telegram_bot.__init__ import updater
from quran_telegram_bot.models import database

database.connect()
updater.start_polling()
# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
# Close database before stopping the bot
database.close()
