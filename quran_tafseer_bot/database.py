from typing import List

import peewee


# Define the database
database = peewee.SqliteDatabase("users_preferences.db",
                                 pragmas={'journal_mode': 'wal',
                                          'cache_size': -1024 * 64})


def create_database(database_instance: peewee.Database,
                    tables: List[peewee.Table]):
    """
    Create empty database with tables based
    :param database_instance: Peewee Database instance
    :param tables: List of tables to be created
    """
    with database_instance:
        database_instance.create_tables(tables)