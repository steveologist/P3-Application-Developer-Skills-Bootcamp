"""Define a reporting."""


from models.database import Database as db
from models.encoder import encode_json_to_dict
from controllers import errorcontroller
from views import reportingview
from views import errorview
from views import databaseview


def display_reporting():
    """Manage reporting functionality."""
    while True:
        try:
            choice = reportingview.choice_report_to_display()

            if choice == 1:
                while True:
                    try:
                        choice = reportingview.wich_order()
                        if choice == 1:
                            players_list = (
                                sort_players_list_by_alphabetical_order(
                                    db.player_table
                                )
                            )
                            reportingview.display_players_report(players_list)
                            break
                        elif choice == 2:
                            players_list = sort_players_list_by_rank_order(
                                db.player_table
                            )
                            reportingview.display_players_report(players_list)
                            break
                        elif choice == 3:
                            break
                        else:
                            errorview.display_wrong_choice_message()
                    except ValueError:
                        errorview.display_not_an_integer_message()

            elif choice == 2:
                while True:
                    try:
                        tournament_number = choose_a_tournament()
                        tournament_player_list = db.tournament_table.get(
                            doc_id=tournament_number
                        )["players_list"]
                        choice = reportingview.wich_order()
                        if choice == 1:
                            players_list = (
                                sort_players_list_by_alphabetical_order(
                                    tournament_player_list
                                )
                            )
                            reportingview.display_players_report(players_list)
                            break
                        if choice == 2:
                            players_list = sort_players_list_by_rank_order(
                                tournament_player_list
                            )
                            reportingview.display_players_report(players_list)
                            break
                        elif choice == 3:
                            break
                        else:
                            errorview.display_wrong_choice_message()
                    except ValueError:
                        errorview.display_not_an_integer_message()

            elif choice == 3:
                tournaments_list = format_tournaments_to_display()
                reportingview.display_all_tournament_report(tournaments_list)

            elif choice == 4:
                while True:
                    try:
                        tournament_number = choose_a_tournament()
                        tournament_rounds_list = db.tournament_table.get(
                            doc_id=tournament_number
                        )["rounds_list"]
                        for round in tournament_rounds_list:
                            del round["match_list"]
                        reportingview.display_all_rounds_tournament_report(
                            tournament_rounds_list
                        )
                        break
                    except ValueError:
                        errorview.display_not_an_integer_message()

            elif choice == 5:
                while True:
                    try:
                        tournament_number = choose_a_tournament()
                        tournament_rounds_list = db.tournament_table.get(
                            doc_id=tournament_number
                        )["rounds_list"]
                        match_list = []
                        for round in tournament_rounds_list:
                            match_list.append(round["match_list"])
                        reportingview.display_all_matchs_tournament_report(
                            match_list
                        )
                        break
                    except ValueError:
                        errorview.display_not_an_integer_message()

            elif choice == 6:
                break

            else:
                errorview.display_wrong_choice_message()

        except ValueError:
            errorview.display_not_an_integer_message()


def sort_players_list_by_alphabetical_order(self):
    """Take player table database in argument and return sorted list by alphabetical order.""" # noqa
    players_list = []
    for player in self:
        player = encode_json_to_dict(player)
        players_list.append(player)
    players_list.sort(key=lambda player: player.get("last_name"))

    return players_list


def sort_players_list_by_rank_order(self):
    """Take player table database in argument and return sorted list by rank order.""" # noqa
    players_list = []
    for player in self:
        player = encode_json_to_dict(player)
        players_list.append(player)
    players_list.sort(key=lambda player: player.get("rank"))

    return players_list


def format_tournaments_to_display():
    """Format and return each tournament in database in a list."""
    tournaments_list = []
    for tournament in db.tournament_table:
        tournament = encode_json_to_dict(tournament)
        del tournament["rounds_list"]
        del tournament["players_list"]
        tournaments_list.append(tournament)

    return tournaments_list


def choose_a_tournament():
    """Manage selection of a tournament."""
    while True:
        try:
            databaseview.display_tournament_in_db()
            tournament_number = reportingview.select_tournament_number()
            if (
                tournament_number > len(db.tournament_table)
                or tournament_number <= 0
            ):
                raise errorcontroller.OutOfRangeException
            return tournament_number

        except errorcontroller.OutOfRangeException:
            errorview.display_not_in_selection_range()
