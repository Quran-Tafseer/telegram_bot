import peewee

# Define the database
database = peewee.SqliteDatabase("users_preferences.db", pragmas={'journal_mode': 'wal', 'cache_size': -1024 * 64})


class BaseModel(peewee.Model):
    class Meta:
        database = database


class UserPreference(BaseModel):
    user_id = peewee.IntegerField(primary_key=True)
    book_id = peewee.IntegerField(null=True)
    username = peewee.CharField(max_length=100)
    first_name = peewee.CharField(max_length=100, null=True)
    last_name = peewee.CharField(max_length=100, null=True)
    language_code = peewee.CharField(max_length=5, null=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
