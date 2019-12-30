from quran_tafseer_bot.models import UserPreference
from quran_tafseer_bot.database import create_database, database

TABLES = [UserPreference]

if __name__ == '__main__':
    create_database(database, TABLES)
