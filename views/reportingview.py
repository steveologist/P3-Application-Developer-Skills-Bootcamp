"""Display reporting messages."""


from models.encoder import encode_json_to_str
from views import userinput


def display_players_report(player_list):
    """Display each player of players list."""
    for player in player_list:
        print(encode_json_to_str(player))


def display_all_tournament_report(tournament_list):
    """Display each tournament of tournaments list."""
    for tournament in tournament_list:
        print(encode_json_to_str(tournament))


def display_all_rounds_tournament_report(tournament_rounds_list):
    """Display each round of rounds list."""
    for round in tournament_rounds_list:
        print(encode_json_to_str(round))


def display_all_matchs_tournament_report(tournament_matchs_list):
    """Display each match of matchs list."""
    for match in tournament_matchs_list:
        print(encode_json_to_str(match))


def choice_report_to_display():
    """Display report menu and return number input."""
    print(
        """Which report would you like to display?
1. List of all players,
2. List of all players in a tournament,
3. List of all tournaments,
4. List of all rounds in a tournament,
5. List of all matches in a tournament,
6. Back."""
    )

    return userinput.input_a_number()


def wich_order():
    """Display order option and return number input."""
    print(
        """In order:
1. Alphabetical,
2. Ascending ranking,
3. Back."""
    )

    return userinput.input_a_number()


def select_tournament_number():
    """Display select tournament number and return number input."""
    print("Select a tournament number: ")

    return userinput.input_a_number()
