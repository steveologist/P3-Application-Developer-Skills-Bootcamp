"""Manage the running of a tournament."""


import datetime
from datetime import timedelta
from models.database import Database as db
from models.encoder import encode_json_to_dict
from models.player import DictToPlayer
from models.tournament import DictToTournament
from models.round import DictToRound
from controllers import errorcontroller
from controllers import roundcontroller
from controllers import matchcontroller
from controllers import systemcontroller
from controllers import databasecontroller
from controllers import playercontroller
from views import errorview
from views import matchview
from views import tournamentview
from views import playerview
from views import roundview
from views import databaseview
from views.tournamentinput import InputTournament


def prepare_new_tournament_to_start():
    """Manage creation of tournament and run it when it's complete."""
    tournament = create_tournament()
    if tournament:
        adding_player_in_tournament_process(tournament)
        tournamentview.display_start_tournament()
        databasecontroller.insert_tournament_in_db(tournament)
        run_tournament(tournament)


def create_tournament():
    """Input tournament attributs and return tournament object."""
    tournament = InputTournament()
    while True:
        try:
            if tournament.name is not False:
                pass
            else:
                tournament.input_name()
            if tournament.name == "":
                tournament.name = False
                raise errorcontroller.EmptyInputException

            if tournament.location is not False:
                pass
            else:
                tournament.input_location()
            if tournament.location == "":
                tournament.location = False
                raise errorcontroller.EmptyInputException

            if tournament.time_controller is not False:
                pass
            else:
                selected_mode = tournament.input_mode()
            if selected_mode in range(len(tournament.mode)):
                tournament.time_controller = tournament.mode[selected_mode]
            else:
                raise errorcontroller.OutOfRangeException

            if tournament.duration is not False:
                pass
            else:
                tournament.input_duration()
            if tournament.duration <= 0:
                tournament.duration = False
                raise errorcontroller.NotPositiveIntegerException

            if tournament.number_of_rounds is not False:
                pass
            else:
                choice = tournamentview.change_the_number_of_rounds()
                if systemcontroller.choice_verification(choice):
                    tournament.input_number_of_rounds()
                else:
                    tournament.number_of_rounds = 4
            if tournament.number_of_rounds <= 0:
                tournament.number_of_rounds = False
                raise errorcontroller.NotPositiveIntegerException

            if tournament.description is not False:
                pass
            else:
                choice = tournamentview.add_a_description()
                if systemcontroller.choice_verification(choice):
                    tournament.input_description()
                else:
                    tournament.description = ""

            tournamentview.display_tournament_summary(tournament)

            choice = tournamentview.validate_creation()

            if systemcontroller.choice_verification(choice):
                if tournament.duration > 1:
                    first_day = datetime.date.today()
                    last_day = first_day + timedelta(
                        days=(tournament.duration - 1)
                    )
                    tournament.date = str(first_day) + "_" + str(last_day)
                else:
                    tournament.date = str(datetime.date.today())

                delattr(tournament, "duration")

                return tournament

            else:
                break

        except ValueError:
            errorview.display_not_an_integer_message()
        except errorcontroller.EmptyInputException:
            errorview.display_its_blank_message()
        except errorcontroller.OutOfRangeException:
            errorview.display_not_in_selection_range()
        except errorcontroller.NotPositiveIntegerException:
            errorview.display_not_positive_integer()


def adding_player_in_tournament_process(tournament):
    """Call functions to add players in tournament."""
    number_of_player = create_number_of_player()
    select_and_add_player_in_tournament(tournament, number_of_player)


def create_number_of_player():
    """Choose how many player will play and return this number."""
    while True:
        try:
            number_of_player = tournamentview.how_many_player_will_play()
            if number_of_player % 2 != 0:
                raise errorcontroller.NotAnEvenNumberException
            if number_of_player > len(db.player_table):
                raise errorcontroller.NotEnoughPlayerInDatabaseException
            if number_of_player < 4:
                raise errorcontroller.NumberOfPlayerIsTooLow
            break
        except ValueError:
            errorview.display_not_an_integer_message()
        except errorcontroller.NotAnEvenNumberException:
            errorview.display_not_an_even_number()
        except errorcontroller.NotEnoughPlayerInDatabaseException:
            errorview.display_you_selected_too_much_player()
        except errorcontroller.NumberOfPlayerIsTooLow:
            errorview.display_not_enough_player()

    return number_of_player


def select_and_add_player_in_tournament(tournament, number_of_player):
    """Choose wich players will play and add it in tournament."""
    databaseview.display_player_in_db()
    selected_player = []

    while len(tournament.players_list) != number_of_player:
        try:
            player_number = tournamentview.wich_player_will_play()
            if player_number in selected_player:
                raise errorcontroller.WrongChosenPlayerException
            if player_number > len(db.player_table) or player_number <= 0:
                raise errorcontroller.OutOfRangeException
            else:
                selected_player.append(player_number)
                player = db.player_table.get(doc_id=player_number)
                player = encode_json_to_dict(player)
                player = DictToPlayer(player)
                tournament.add_player_in_players_list(player)
                playerview.display_added_player_message(player)

        except ValueError:
            errorview.display_not_an_integer_message()
        except IndexError:
            errorview.display_wrong_choice_message()
        except errorcontroller.WrongChosenPlayerException:
            errorview.display_this_player_is_already_chosen()
        except errorcontroller.OutOfRangeException:
            errorview.display_not_in_selection_range()

    tournamentview.display_player_in_tournament(tournament)

    choice = tournamentview.validate_chosen_players()

    if systemcontroller.choice_verification(choice):
        pass

    else:
        tournament.players_list = []
        adding_player_in_tournament_process(tournament)


def run_tournament(tournament):
    """Run tournament until each rounds are played."""
    if len(tournament.rounds_list) > 0:
        round_number = len(tournament.rounds_list)
    else:
        round_number = 0
    while len(tournament.rounds_list) < tournament.number_of_rounds:
        playercontroller.propose_to_change_player_rank(tournament)
        while True:
            choice = roundview.start_round(round_number)
            if systemcontroller.choice_verification(choice):
                round = roundcontroller.create_round(round_number)
                roundview.display_round_name(round)
                players_matchmaking = roundcontroller.run_matchmaking(
                    round, tournament
                )
                databasecontroller.update_tournament_in_db(tournament)
                break

        while True:
            playercontroller.propose_to_change_player_rank(tournament)
            choice = roundview.end_round(round_number)
            if systemcontroller.choice_verification(choice):
                roundcontroller.create_ending_round_date(round)
                while True:
                    results = matchcontroller.create_match_results(
                        players_matchmaking
                    )
                    choice = matchview.validate_match_result()
                    if systemcontroller.choice_verification(choice):
                        break
                match_list = matchcontroller.create_match_list(
                    results, players_matchmaking
                )
                round.match_list = match_list
                tournament.add_round_in_rounds_list(round)
                databasecontroller.update_tournament_in_db(tournament)
                round_number += 1
                break

    playercontroller.propose_to_change_player_rank(tournament)
    player_matchmaking, classement = roundcontroller.run_matchmaking(
        round, tournament, last_round=True
    )
    prepare_standings(player_matchmaking, classement)
    databasecontroller.update_tournament_in_db(tournament)


def prepare_standings(player_matchmaking, classement):
    """Prepare displaying of the standings for the end of the tournament."""
    print("\nLes résultats du tournoi sont : ")
    for i in range(len(classement)):
        tournamentview.display_standings(player_matchmaking, classement, i)


def check_if_a_tournament_is_not_over():
    """Compare number of round and round list for each tournament in db and ask for user choice.""" # noqa
    for tournament in db.tournament_table:
        if len(tournament["rounds_list"]) < tournament["number_of_rounds"]:
            choice = tournamentview.tournament_is_not_over(tournament)

            if systemcontroller.choice_verification(choice):
                prepare_tournament_to_restart(tournament)


def prepare_tournament_to_restart(tournament):
    """Call functions to recreate tournament argument in utilizable format."""
    tournament = encode_json_to_dict(tournament)
    tournament = DictToTournament(tournament)
    encode_tournament_players_list_to_object(tournament)
    encode_tournament_rounds_list_to_object(tournament)
    encode_tournament_players_in_match_list_to_object(tournament)
    run_tournament(tournament)


def encode_tournament_players_list_to_object(tournament):
    """Encode players list from dict to object."""
    players_list_in_class_format = []
    for player in tournament.players_list:
        player = DictToPlayer(player)
        players_list_in_class_format.append(player)
    delattr(tournament, "players_list")
    tournament.players_list = players_list_in_class_format


def encode_tournament_rounds_list_to_object(tournament):
    """Encode rounds list from dict to object."""
    rounds_list_in_class_format = []
    for round in tournament.rounds_list:
        round = DictToRound(round)
        rounds_list_in_class_format.append(round)
    delattr(tournament, "rounds_list")
    tournament.rounds_list = rounds_list_in_class_format


def encode_tournament_players_in_match_list_to_object(tournament):
    """Encode players in match list from dict to object."""
    for i in range(len(tournament.rounds_list)):
        for j in range(len(tournament.rounds_list[i].match_list)):
            player_one = tournament.rounds_list[i].match_list[j][0][0]
            player_one = (
                playercontroller.found_corresponding_player_object_in_list(
                    tournament, player_one
                )
            )
            del tournament.rounds_list[i].match_list[j][0][0]
            tournament.rounds_list[i].match_list[j][0].insert(0, player_one)

            player_two = tournament.rounds_list[i].match_list[j][1][0]
            player_two = (
                playercontroller.found_corresponding_player_object_in_list(
                    tournament, player_two
                )
            )
            del tournament.rounds_list[i].match_list[j][1][0]
            tournament.rounds_list[i].match_list[j][1].insert(0, player_two)
