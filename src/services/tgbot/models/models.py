
from peewee import *

SQLITE_DB_PATH = 'database/test.db'

database = SqliteDatabase(SQLITE_DB_PATH)


class BaseModel(Model):
    class Meta:
        database = database


class Config(BaseModel):
    id = PrimaryKeyField(unique=True)
    chat_id = IntegerField()
    status = BooleanField(default=True)
    delay = IntegerField(default=30)
    selected_counter = IntegerField(default=0)

    class Meta:
        db_table = "config"
        order_by = 'id'
