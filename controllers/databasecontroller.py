"""Manage insertions in database."""


from tinydb import Query
from models.database import Database as db
from models.encoder import encode_class_to_dict


def insert_player_in_db(player):
    """Add player object in database."""
    player = encode_class_to_dict(player)
    db.player_table.insert(player)


def update_player_rank_in_db(player, new_rank):
    """Update rank value of player in database."""
    player_in_db = db.player_table.get(
        (Query().last_name == player.last_name)
        & (Query().first_name == player.first_name)
        & (Query().birthday == player.birthday)
        & (Query().sexe == player.sexe)
        & (Query().rank == player.rank)
    )
    db.player_table.update({"rank": new_rank}, doc_ids=[player_in_db.doc_id])


def insert_tournament_in_db(tournament):
    """Add tournament object in database."""
    tournament = encode_class_to_dict(tournament)
    db.tournament_table.insert(tournament)


def update_tournament_in_db(tournament):
    """Update tournament in database."""
    tournament = encode_class_to_dict(tournament)
    tournament_in_db = db.tournament_table.get(
        (Query().name == tournament["name"])
        & (Query().location == tournament["location"])
        & (Query().date == tournament["date"])
        & (Query().time_controller == tournament["time_controller"])
        & (Query().description == tournament["description"])
    )
    db.tournament_table.update(tournament, doc_ids=[tournament_in_db.doc_id])
