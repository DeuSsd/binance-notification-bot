import os
from pathlib import Path
from models import *



def create_tables():
    with database:
        database.create_tables([Config])
        
        
if __name__ == '__main__':
    if not os.path.isfile(Path(SQLITE_DB_PATH)):
        print("created DB")
        create_tables()
    else:
        print("DB exist")
        