from quran_telegram_bot.database import create_database, database
from quran_telegram_bot.models import UserPreference

TABLES = [UserPreference]

if __name__ == '__main__':
    """
    Util module to run before running the application to create the database.
    """
    create_database(database, TABLES)
