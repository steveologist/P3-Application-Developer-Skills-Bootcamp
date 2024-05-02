"""Define database."""


import os
from tinydb import TinyDB


class Database:

    mydir = os.getcwd()
    db = TinyDB(mydir + r"/data/db.json")
    player_table = db.table("player_table")
    tournament_table = db.table("tournament_table")

    def __init__(self):
        pass
