"""Display database informations."""


from models.database import Database as db


def display_player_in_db():
    """Print last name, first name and rank of each players in database."""
    for player in db.player_table:
        print(
            player.doc_id,
            player["last_name"],
            player["first_name"],
            player["rank"],
        )


def display_tournament_in_db():
    """Print doc id, name, location and date of each tournaments in database.""" # noqa
    for tournament in db.tournament_table:
        print(
            tournament.doc_id,
            ".",
            tournament["name"],
            "à",
            tournament["location"],
            "le",
            tournament["date"],
        )
